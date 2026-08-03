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
from sage.modules.free_module_element import FreeModuleElement
from sage.categories.category import Category
from sage.categories.groups import Groups
from sage.categories.modules import Modules
from sage.matrix.special import diagonal_matrix
from sage.structure.element import Element, Vector
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp



def _is_additive(group: Any) -> bool:
    r"""Return whether ``group`` is written additively, asked of its category."""
    from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups

    return group.category().is_subcategory(CommutativeAdditiveGroups())


class FinitelyPresentedTorsionModules(Category):
    r"""Finitely presented torsion $\mathbb Z$-modules with a chosen generating set.

    The underlying group of a torsion bilinear or quadratic form, as an object
    of this universe rather than a conversion out of it.  Everything here is an
    invariant of the module -- of its isomorphism class, mostly -- and none of
    it involves a form: the invariant factors, the primary decomposition, the
    exponent, the order, and the presentations and permutation representations
    a group is expected to offer.

    That division is the point.  A framed bilinear module $(G,b)$ is not
    determined by $G$, and two of them with isometric forms may have different
    $G$; but every question that is about $G$ alone belongs here, where it can
    be asked and cached once, instead of on each form that happens to carry it.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented torsion modules"

    def super_categories(self) -> list:
        r"""Return $\mathbb Z\text{-Mod}$.

        A module, not a group with extra methods.  Sage has no notion that a
        finite abelian group is a $\mathbb Z$-module -- it does not refine
        their categories or impose the action -- so an object of this category
        that inherited from a group category would get $a+b$ as the group
        operation and would have no $na$ at all except by accident of what the
        concrete class happens to implement.  Being finite abelian is a
        consequence of being a finitely presented torsion module, not the other
        way around.
        """
        return [Modules(ZZ)]

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
        assert generators, f"{group} has no generators to present it on"
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
        return self.from_relations(reduced[: len(orders), :])

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
                lambda gens, exps: zipsum(
                    exps,
                    gens,
                    identity,
                    strict=True,
                    term=lambda exponent, generator: exponent * generator,
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

    def from_relations(self, relations: Any) -> "TorsionModule":
        r"""Return the module presented by ``relations``, as a morphism.

        The matrix is turned into the morphism it is the matrix of, because
        that is what a presentation is; nothing downstream sees the matrix
        except the linear algebra.
        """
        from sage.modules.free_module import FreeModule

        relations = matrix(ZZ, relations)
        domain = FreeModule(ZZ, relations.nrows())
        codomain = FreeModule(ZZ, relations.ncols())
        return TorsionModule(
            ModuleMorphism(
                dict(
                    zip(
                        domain.gens(),
                        (_combination(codomain, row) for row in relations.rows()),
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
            if self._coordinates.is_zero():
                return ZZ.one()
            for k in ZZ(parent.exponent()).divisors():
                if parent.reduce(k * self._coordinates).is_zero():
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


class TorsionModuleElement(Element):
    r"""A class $\bar x\in\operatorname{coker} f$, held by a canonical lift."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        Element.__init__(self, parent)
        self._coordinates = parent.reduce(coordinates)

    def _lift(self) -> FreeModuleElement:
        r"""Return the canonical representative of this class.  Private: see
        :meth:`FormModuleElement._coordinates`."""
        return self._coordinates

    def _repr_(self) -> str:
        return repr(self._coordinates)

    # Z-Mod's structure, realized for this representation.  The operations are
    # the category's; what is here is only how adding and scaling are carried
    # out on stored coordinate vectors, which is what Sage's coercion model
    # dispatches to.

    def _add_(self, other: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(self._coordinates + other._coordinates)

    def _sub_(self, other: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(self._coordinates - other._coordinates)

    def _neg_(self) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(-self._coordinates)

    def _lmul_(self, factor: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(ZZ(factor) * self._coordinates)

    _rmul_ = _lmul_

    # The module structure.  Implemented here rather than on a category
    # because what these do is add coordinate vectors, which is a fact about
    # this class's storage; what they *mean* is Modules(ZZ)'s, and no
    # subcategory of it restates them.

    def _add_(self, other: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(self._coordinates + other._coordinates)

    def _sub_(self, other: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(self._coordinates - other._coordinates)

    def _neg_(self) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(-self._coordinates)

    def _lmul_(self, factor: Any) -> "TorsionModuleElement":
        return self.parent()._from_coordinates(ZZ(factor) * self._coordinates)

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates, other._coordinates, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates))


class TorsionModule(Parent):
    r"""$\operatorname{coker} f$ for $f: A\to B$ a morphism of free modules.

    Presented by the morphism itself: the generating set is $B$'s and the
    relations are $f$'s rows.  Nothing here is a submodule of anything.
    """

    Element = TorsionModuleElement

    def __init__(self, presentation: Any) -> None:
        relations = matrix(ZZ, presentation.matrix())
        assert relations.det() != 0, (
            "the presentation must have nonzero determinant, or its cokernel "
            "is not torsion"
        )
        Parent.__init__(self, base=ZZ)
        self._presentation = presentation
        self._relations = relations
        self._hermite = relations.hermite_form()
        refine(self, FinitelyPresentedTorsionModules())

    def presentation(self) -> Any:
        r"""Return $p:\mathbb Z^n\to\mathbb Z^m$, the morphism this is the cokernel of.

        Every finitely presented module is one, so this is not a mark of
        special provenance: it is what "finitely presented" says.  There is no
        relation matrix here beside it -- a relation is a generator of the
        domain, and the matrix below is $p$ read in the two generating sets,
        which is a reading and not a second datum.
        """
        return self._presentation

    def relation_matrix(self) -> Matrix:
        r"""Return $p$'s matrix: the images of its generators, one per row.

        A reading of :meth:`presentation`, kept because the linear algebra
        this module does -- Hermite reduction, Smith form, solving -- is
        matrix work, and this is where the morphism is handed to it.
        """
        return self._relations

    def reduce(self, coordinates: Any) -> FreeModuleElement:
        r"""Return the canonical representative of this class in $B$.

        Reduction against the Hermite form: each pivot in turn, subtracting the
        multiple of its row that brings that coordinate into range.  The result
        depends only on the class, which is what makes equality and hashing
        decidable rather than a search.
        """
        # Taken as coordinates, not as an element: what arrives may belong to a
        # module carrying a form or an inner product, and the reduction below
        # subtracts plain rows of the Hermite form.
        coordinates = vector(ZZ, list(coordinates))
        for row in self._hermite.rows():
            pivot = next(i for i, entry in enumerate(row) if entry != 0)
            coordinates -= (coordinates[pivot] // row[pivot]) * row
        return coordinates

    def _element_constructor_(self, x: Any) -> TorsionModuleElement:
        r"""Return ``x``, which has to be an element of this quotient already.

        A coordinate vector is not an element of anything: it becomes one only
        against a stated generating set, and stating one is what
        :meth:`linear_combination` is for.
        """
        assert isinstance(x, TorsionModuleElement) and x.parent() is self, (
            f"{x} is not an element of {self}; a class here is built from this "
            "quotient's own generators, with linear_combination or by adding "
            "and scaling them"
        )
        return x

    def __contains__(self, x: Any) -> bool:
        r"""Return whether ``x`` is a class in this quotient, which is parenthood."""
        return isinstance(x, TorsionModuleElement) and x.parent() is self

    def _from_coordinates(self, coordinates: Any) -> TorsionModuleElement:
        r"""Return the class of ``coordinates``, read in this quotient's generators.

        Private, and the only route from a bare vector to an element: the
        object's own construction of its generators and their arithmetic goes
        through here, and everything else states what it means through
        :meth:`linear_combination`.
        """
        return self.element_class(self, coordinates)

    def zero(self) -> TorsionModuleElement:
        return self._from_coordinates([ZZ.zero()] * self.num_module_generators())

    def linear_combination(self, coefficients: Any) -> TorsionModuleElement:
        r"""Return $\sum_i a_i g_i$ for ``coefficients`` $=(a_i)$."""
        coefficients = tuple(coefficients)
        generators = self.gens()
        assert len(coefficients) == len(generators), (
            f"this quotient has {len(generators)} generators, got "
            f"{len(coefficients)} coefficients"
        )
        total = self.zero()
        for coefficient, generator in zip(coefficients, generators):
            # Cast rather than coerce: a coefficient outside the base ring is
            # not a scalar here, and saying so loudly beats a silent product.
            total += ZZ(coefficient) * generator
        return total

    def gens(self) -> tuple[TorsionModuleElement, ...]:
        r"""Return the images of $B$'s generators."""
        size = self._relations.ncols()
        return tuple(
            self._from_coordinates([ZZ(i == j) for j in range(size)])
            for i in range(size)
        )

    def as_finitely_presented_group(self) -> Any:
        r"""Return this module as an object of :class:`FinitelyPresentedGroups`.

        The same group, said in the vocabulary of presentations: generators
        $e_i$, commuting, subject to the relations this module was built from.
        It belongs here because it is built from nothing but them -- a form
        module carrying this one has no say in what group it is, and asking it
        was asking the wrong object.

        Sage's finitely presented groups are refined into the owned category on
        construction, so what comes back already displays the owned way.
        """
        from sage.groups.free_group import FreeGroup
        from sage.misc.misc_c import prod

        relations = self._relations
        size = relations.nrows()
        if size == 0:
            return FreeGroup(0, "e").quotient([])
        free = FreeGroup([f"e{i + 1}" for i in range(size)])
        generators = free.gens()
        words = [
            generators[i] * generators[j] * (generators[i] ^ -1) * (generators[j] ^ -1)
            for i in range(size)
            for j in range(i + 1, size)
        ]
        words.extend(
            prod((generators[j] ^ int(relations[j, k])) for j in range(size))
            for k in range(size)
        )
        return free.quotient(words)

    def invariants(self) -> tuple:
        r"""Return the invariant factors, from the Smith form of the relations."""
        smith = self._relations.smith_form()[0]
        return tuple(
            entry for entry in smith.diagonal() if entry not in (ZZ.one(), ZZ.zero())
        )

    def exponent(self) -> Any:
        r"""Return the exponent: the largest invariant factor, or 1."""
        invariants = self.invariants()
        return invariants[-1] if invariants else ZZ.one()

    def cardinality(self) -> Any:
        r"""Return $|\operatorname{coker} f| = |\det f|$."""
        return abs(self._relations.det())

    def __iter__(self):
        from sage.misc.mrange import cartesian_product_iterator

        size = self._relations.ncols()
        bounds = [self._hermite[i, i] for i in range(size)]
        for point in cartesian_product_iterator([range(b) for b in bounds]):
            yield self._from_coordinates(point)

    def annihilator(self) -> Any:
        r"""Return the ideal killing every element: $(\text{exponent})$."""
        return ZZ.ideal(self.exponent())

    def smith_form_gens(self) -> tuple[TorsionModuleElement, ...]:
        r"""Return generators realizing the invariant factor decomposition.

        With $D=UMV$ the Smith form of the relations, $x\mapsto xV$ carries
        $\operatorname{coker} M$ onto $\mathbb Z^m/\operatorname{row} D$, whose
        standard generators pull back to the rows of $V^{-1}$.  Those with
        $d_i=1$ die, so they are dropped.
        """
        smith, _, right = self._relations.smith_form()
        inverse = right.inverse().change_ring(ZZ)
        return tuple(
            self._from_coordinates(inverse.row(i))
            for i, entry in enumerate(smith.diagonal())
            if entry != ZZ.one()
        )

    def rank(self) -> Any:
        r"""Return 0: a cokernel of an injective map of free modules is torsion."""
        return ZZ.zero()

    def ngens(self) -> int:
        return self._relations.ncols()

    def _repr_(self) -> str:
        return (
            f"Torsion module on {self.num_module_generators()} generators, "
            f"invariants {self.invariants()}"
        )
