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

from typing import Any

from sage.matrix.matrix0 import Matrix
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.groups import Groups
from sage.categories.modules import Modules
from sage.matrix.special import diagonal_matrix


def _is_additive(group: Any) -> bool:
    r"""Return whether ``group`` is written additively, asked of its category."""
    from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups

    return group.category().is_subcategory(CommutativeAdditiveGroups())


class FinitelyPresentedTorsionModules(Category_over_base_ring):
    r"""Finitely presented torsion modules with a chosen generating set over a base ring $R$."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        match base_ring:
            case None:
                return super().__classcall__(cls, ZZ)
            case _ if base_ring is ZZ:
                return super().__classcall__(cls, ZZ)
            case _:
                raise TypeError(
                    "this finite-presentation implementation is over ZZ"
                )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented torsion modules"

    def super_categories(self) -> list:
        return [
            TorsionModules(self.base_ring()),
            FinitelyPresentedModules(self.base_ring()),
        ]

    def direct_sum_of_cyclics(self, orders: Any) -> "TorsionModule":
        r"""Return $\bigoplus_i\mathbb Z/d_i$ on one generator per summand.

        The orders are taken as given and not normalized: $[2,3]$ builds a
        module on *two* generators, not $\mathbb Z/6$ on one.  Those two are
        isomorphic and are not equal, and which one this is matters to
        everything written on the generating set afterwards.
        """
        orders = [ZZ(d) for d in orders]
        assert all(d > 1 for d in orders), (
            f"each summand needs an order greater than 1, got {orders}"
        )
        return self.from_relations(diagonal_matrix(ZZ, orders))

    def from_abelian_group(self, group: Any) -> "TorsionModule":
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
        generators = tuple(group.gens())
        if not generators:
            return self.from_relations(
                matrix(ZZ, 0, 0),
                Sets.Δ[-1],
            )
        orders = [ZZ(generator.order()) for generator in generators]
        size = prod(orders)
        assert size <= 10 ** 6, (
            f"{group}'s generators have orders {orders}, whose product {size} "
            "is too large to search for relations; build the module from a "
            "presentation instead"
        )

        combine, identity = self._group_arithmetic(group)
        from sage.misc.mrange import cartesian_product_iterator

        found = [
            vector(ZZ, exponents)
            for exponents in cartesian_product_iterator([range(d) for d in orders])
            if combine(generators, exponents) == identity
        ]
        relations = matrix(ZZ, found).stack(diagonal_matrix(ZZ, orders))
        # Square again: the relation lattice has full rank, so its Hermite form
        # has one nonzero row per generator and the rest are padding.
        reduced = relations.hermite_form()
        return self.from_relations(
            reduced[: len(orders), :],
            finite_ordered_set(generators),
        )

    def _group_arithmetic(self, group: Any) -> tuple:
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
                lambda gens, exps: sum(
                    (ZZ(a) * g for a, g in zip(exps, gens)), identity
                ),
                identity,
            )
        identity = group.one()
        return (
            lambda gens, exps: prod(
                (g ** ZZ(a) for a, g in zip(exps, gens)), identity
            ),
            identity,
        )

    def from_relations(
        self,
        relations: Any,
        generating_set: Any = None,
    ) -> "TorsionModule":
        r"""Return the module presented by ``relations``, as a morphism.

        The matrix is turned into the morphism it is the matrix of, because
        that is what a presentation is; nothing downstream sees the matrix
        except the linear algebra.
        """
        relations = matrix(ZZ, relations)
        domain = BasedFreeModule(ZZ, Sets.Δ[relations.nrows() - 1])
        match generating_set:
            case None:
                generating_set = Sets.Δ[relations.ncols() - 1]
            case _:
                generating_set = finite_ordered_set(generating_set)
                assert generating_set.cardinality() == relations.ncols(), (
                    "the generating set and presentation have different widths"
                )
        codomain = BasedFreeModule(ZZ, generating_set)
        return TorsionModule(
            _module_morphism(
                domain,
                codomain,
                dict(
                    zip(
                        domain.generating_set(),
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

        def order(self: Any) -> Any:
            r"""Return the generator of $\operatorname{Ann}(a)\subseteq\mathbb Z$.

            The least $k\ge 1$ with $ka=0$, which exists because this module is
            torsion -- in a free module the same ideal is zero and there is
            nothing to return.  It agrees numerically with the element's order
            in the underlying group, and is not that statement.
            """
            parent = self.parent()
            coordinates = self._coordinates()
            if coordinates.is_zero():
                return ZZ.one()
            for k in ZZ(parent.exponent()).divisors():
                if parent.reduce(k * coordinates).is_zero():
                    return k
            assert False, "an element of a finite torsion module has finite order"

    class ParentMethods:
        r"""What a torsion module is asked, none of which involves a form."""

        def abelian_group(self: Any) -> Any:
            r"""Return this module as a Sage finite abelian group."""
            from sage.groups.abelian_gps.abelian_group import AbelianGroup

            return refine(
                own_group_types(AbelianGroup(list(self.invariants()))),
                OwnedFiniteGroups(),
            )

        def permutation_group(self: Any) -> Any:
            r"""Return a permutation representation of this module."""
            return self.abelian_group().permutation_group()

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether this module is elementary abelian of exponent $p$."""
            p = ZZ(p)
            assert p.is_prime(), f"p must be prime, got {p}"
            group = self.permutation_group()
            if not group.is_elementary_abelian():
                return False
            return group.order() == 1 or group.exponent() == p

        def primary_decomposition(self: Any) -> dict:
            r"""Return the primary decomposition as $\{p: \text{orders}\}$.

            An invariant of the isomorphism class, read off the invariant
            factors: $\mathbb Z/d\cong\bigoplus_p\mathbb Z/p^{v_p(d)}$.
            """
            decomposition: dict = {}
            for factor_ in self.invariants():
                for prime, exponent in ZZ(factor_).factor():
                    decomposition.setdefault(prime, []).append(prime ** exponent)
            return {p: tuple(sorted(orders)) for p, orders in decomposition.items()}

        def as_finitely_presented_group(self: Any) -> Any:
            r"""Return this module as a finitely presented abelian group."""
            from sage.groups.free_group import FreeGroup
            from sage.misc.misc_c import prod

            relations = self.relation_matrix()
            size = relations.ncols()
            if size == 0:
                return FreeGroup(0, "e").quotient([])
            free = FreeGroup([f"e{i + 1}" for i in range(size)])
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
            return free.quotient(words)

        def __iter__(self: Any):
            from sage.misc.mrange import cartesian_product_iterator

            hermite = self.relation_matrix().hermite_form(
                include_zero_rows=False
            )
            bounds = [hermite[i, i] for i in range(self.ngens())]
            for point in cartesian_product_iterator(
                [range(bound) for bound in bounds]
            ):
                yield self._from_coordinates(point)

        def annihilator(self: Any) -> Any:
            r"""Return the ideal generated by the module exponent."""
            return ZZ.ideal(self.exponent())

        def smith_form_gens(self: Any) -> Any:
            r"""Return generators realizing the invariant-factor decomposition."""
            smith, _, right = self.relation_matrix().smith_form()
            inverse = right.inverse().change_ring(ZZ)
            return finite_ordered_set(
                tuple(
                    self._from_coordinates(inverse.row(i))
                    for i, entry in enumerate(smith.diagonal())
                    if entry != ZZ.one()
                )
            )


def TorsionModule(presentation: Any) -> FinitelyPresentedModule:
    r"""Return the cokernel of ``presentation``, refined as torsion."""
    module = FinitelyPresentedModule(presentation)
    assert module in FinitelyPresentedTorsionModules(module.base_ring()), (
        "the presentation does not have torsion cokernel"
    )
    return module
