r"""``IntegralLattices`` — a category owning the lattice-specific API.

Refine any integral lattice parent into this category to gain::

    q(x), b(x, y), div(x), get_isotropic_type(element)
    dual_basis(), I_perp_mod_I(vectors), is_isometric(other)
    with_names(spec), to_lin_comb_generators(element), sublattices
    _latex_()                   # multi-line Gram + discriminant display
    _first_ngens(count)         # generator sugar for ``L.<...> = ...``
    twist(*, names=...)         # twisted copy with optional naming
    __add__, __pow__, direct_sum      # orthogonal direct sums with subdivisions
    Aut(), invariant_lattice(action), formed_coinvariants(action),
    coinvariant_lattice(action), coinvariant_inclusion(action)

Elements gain::

    v * w   →  b(v, w)
    v ^ 2  →  q(v)
    v.q(), v.b(w), v.div()
    v.e_perp_mod_e()            # for isotropic vectors

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: from dzack_research.preamble.refine import refine
    sage: L = Lattices.U
    sage: refine(L, IntegralLattices())
    sage: L.q(L.gens()[0])
    0
"""

import re
from typing import Any, assert_never

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.matrix.special import identity_matrix
from sage.misc.latex import latex as _latex_fn
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.modules.free_module_element import vector

from sage_lattice_category_spike.objects.sets import Sets


class IntegralLattices(Category):
    r"""Category of integral lattices with enriched computational methods.

    Unlike Sage's default::

        - quadratic and bilinear forms via ``q`` / ``b`` / ``div``
        - dual basis, isotropic quotients, isometry checking
        - basis naming, linear-combination display, LaTeX with discriminant-group info
        - orthogonal direct sums with automatic Gram-matrix subdivisions
        - lattice-element arithmetic: multiplication -> bilinear pairing, exponentiation -> q
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "integral lattices"

    def super_categories(self) -> list:
        r"""Return the free form modules, of which lattices are the integral ones.

        Everything a lattice has by having a form on a free module -- the
        pairing, the norm, the rank, the basis, $v*w$ -- it has from there, and
        this category is only what integrality adds.
        """
        return [
            FinitelyGeneratedFreeFormModules(),
            SymmetricBilinearFormModules(),
        ]

    class ParentMethods:
        r"""Methods available on every integral lattice parent refined into this category."""

        # ---- bilinear / quadratic API ----

        def decomposition(self: Any) -> Any:
            r"""Return the chosen block decomposition, or ``None``."""
            return self._orthogonal_decomposition

        def summands(self: Any) -> tuple:
            decomposition = self.decomposition()
            assert decomposition is not None, (
                "this lattice has no chosen nontrivial block decomposition"
            )
            return decomposition.summands()

        def is_decomposable(self: Any) -> bool:
            return self.decomposition() is not None

        def q(self: Any, x: Any) -> Any:
            r"""Return the quadratic form $q(x) = \langle x, x\rangle$."""
            return x.norm()

        def b(self: Any, x: Any, y: Any) -> Any:
            r"""Return the pairing $\langle x, y\rangle$, asked of the two elements."""
            return x.b(y)

        def div(self: Any, x: Any) -> Any:
            r"""Return the positive generator of $\{\langle x, y\rangle : y \in L\}$."""
            pairings = [self.b(x, v) for v in self.basis()]
            return abs(gcd(pairings))

        def gram_of(self: Any, vectors: Any) -> Any:
            r"""Return the Gram matrix $[b(x_i, x_j)]$ of a finite family of vectors."""
            vectors = tuple(vectors)
            return matrix(ZZ, [[self.b(x, y) for y in vectors] for x in vectors])

        def get_isotropic_type(self: Any, isotropic_element: Any) -> str:
            r"""Classify a primitive isotropic element by its cusp type.

            Divisibility 1 gives ``"Odd"``. Divisibility 2 is distinguished
            by whether $e^* = e/2 \in A_L$ is characteristic.
            """
            assert isotropic_element in self, (
                f"get_isotropic_type is about an element of {self}, and this is "
                f"{isotropic_element!r}"
            )
            assert self.q(isotropic_element) == 0, (
                f"expected an isotropic element, got square {self.q(isotropic_element)}"
            )
            assert isotropic_element.is_primitive(), "expected a primitive element"
            divisibility = self.div(isotropic_element)
            assert divisibility in (1, 2), (
                f"expected divisibility 1 or 2 in a 2-elementary lattice, "
                f"got {divisibility}"
            )
            if divisibility == 1:
                return "Odd"
            if divisibility == 2:
                divided_class = self.divided_discriminant_class(isotropic_element)
                if divided_class.is_characteristic():
                    return "Even characteristic"
                return "Even ordinary"
            assert_never(divisibility)

        # ---- dual basis ----

        def dual_basis(self: Any) -> Any:
            r"""Return the dual generators $e_i^\vee$, which are elements of $L^\vee$.

            Defined by $\langle e_i, e_j^\vee\rangle=\delta_{ij}$, and that
            pairing is $L^\vee$'s: $c$ carries $e_i$ there and the form of
            $L^\vee$ pairs the two.  Which is why these are not vectors of
            $L\otimes\mathbb Q$ -- there is no space here containing both $L$
            and its dual for a pairing to happen in, and writing $e_i+e_j^\vee$
            means applying $c$ first.
            """
            dual = self.dual()
            correlation = self.correlation()
            generators = dual.gens()
            for i, v in enumerate(self.gens()):
                for j, w in enumerate(generators):
                    expected = 1 if i == j else 0
                    assert correlation(v).b(w) == expected, (
                        f"dual basis is wrong at ({i}, {j})"
                    )
            return generators

        # ---- isotropic quotients ----

        def I_perp_mod_I(self: Any, vectors: Any) -> Any:
            r"""Return $I^\perp/I$ for the isotropic subobject ``vectors`` span.

            The isotropic reduction of that subobject, under the name this
            category has always called it by.
            """
            return self.subobject_on(vectors).isotropic_reduction()

        # ---- overlattices ----

        def dual_lattice_element(self: Any, coordinates: Any) -> Any:
            r"""Return the element of $L^\vee$ written in $L$'s basis by ``coordinates``.

            The catalogue displays glue vectors as rational coordinates in
            $L$'s own basis, which is how they appear in the literature.  An
            element of $L^\vee$ is written in the dual basis, and
            $\sum_i a_i e_i^\vee = \sum_j v_j e_j$ gives $a = vG$ -- so the
            conversion is by the Gram matrix, and the coordinates come out
            integral exactly when the vector lies in $L^\vee$ at all.
            """
            in_dual_basis = vector(QQ, coordinates) * self.gram_matrix()
            assert all(entry in ZZ for entry in in_dual_basis), (
                f"{tuple(coordinates)} does not lie in L^v: it pairs to "
                f"{tuple(in_dual_basis)} with L's basis, and L^v is where those "
                "pairings are integral"
            )
            return self.dual().linear_combination(in_dual_basis)

        def dual_lattice_generators(self: Any) -> Any:
            r"""Return the explicit module generators of $L^*$."""
            return self.dual().gens()

        def dual_embedding(self: Any) -> Any:
            r"""Return the inclusion morphism $L\to L^*$."""
            return self.correlation()

        def discriminant_projection(self: Any) -> Any:
            r"""Return the quotient morphism $\pi: L^* \to A_L=L^*/L$."""
            return self.discriminant_group().projection()

        def project_to_discriminant_group(self: Any, element: Any) -> Any:
            r"""Project an element of $L^*$ to its class in $A_L$.

            This method applies the stored quotient morphism
            $\pi: L^*\to A_L$.  It does not accept coordinate rows; construct
            elements of $L^*$ first with :meth:`dual_lattice_element`.
            """
            projection = self.discriminant_projection()
            assert (
                isinstance(element, FormModuleElement)
                and element.parent() is projection.domain()
            ), (
                f"pi is defined on {projection.domain()}, and this is "
                f"{element!r}. An element of L^v written in L's own basis is "
                "built with dual_lattice_element(...), which converts by the "
                "Gram matrix; a coordinate vector is named with the dual's "
                "linear_combination."
            )
            return projection(element)

        def divided_discriminant_class(self: Any, element: Any) -> Any:
            r"""Return the discriminant element represented by $e/\operatorname{div}(e)$."""
            assert element in self, "divided_discriminant_class expects an element of this lattice"
            divisibility = self.div(element)
            dual_element = self.correlation()(element) / QQ(divisibility)
            return self.discriminant_projection()(dual_element)

        def glue(self: Any, *elements: Any) -> Any:
            r"""Return the even overlattice glued along discriminant elements.

            The inputs are elements of the discriminant group $A_L = L^\vee/L$.
            Their lifts in $L^\vee$ generate the overlattice together with the
            original lattice.  Catalogue entries should construct elements of
            $L^*$ and project them to $A_L$ before calling this method.
            """
            rank = self.rank()
            rational_rows = [
                [QQ.one() if i == j else QQ.zero() for j in range(rank)]
                for i in range(rank)
            ]
            rational_rows.extend(
                _discriminant_lift_row(element, rank) for element in elements
            )

            denominator = ZZ.one()
            for row in rational_rows:
                for coordinate in row:
                    denominator = denominator.lcm(coordinate.denominator())

            scaled = matrix(
                ZZ,
                [
                    [ZZ(denominator * coordinate) for coordinate in row]
                    for row in rational_rows
                ],
            )
            hermite_rows = [
                row
                for row in scaled.hermite_form().rows()
                if any(coordinate != 0 for coordinate in row)
            ]
            basis = matrix(QQ, hermite_rows[:rank]) / denominator
            gram = basis * self.gram_matrix() * basis.transpose()
            generating_set = finite_ordered_set(
                tuple(tuple(row) for row in basis.rows())
            )
            return _lattice_with_gram(
                matrix(ZZ, gram),
                generating_set,
            )

        # ---- isometry ----

        def is_isometric(self: Any, other: Any) -> bool:
            r"""Return whether two integral lattices are isometric."""
            from sage.quadratic_forms.binary_qf import BinaryQF
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            if self.rank() != other.rank():
                return False
            if self.signature_pair() != other.signature_pair():
                return False

            pos, neg = self.signature_pair()
            if pos == 0 or neg == 0:
                sign = 1 if neg == 0 else -1
                return bool(
                    QuadraticForm(sign * self.gram_matrix())
                    .is_globally_equivalent_to(
                        QuadraticForm(sign * other.gram_matrix())
                    )
                )

            if self.rank() == 2:

                def _binary(L):
                    g = L.gram_matrix()
                    assert g[0, 0] % 2 == 0 and g[1, 1] % 2 == 0
                    return BinaryQF([g[0, 0] // 2, g[0, 1], g[1, 1] // 2])

                return bool(_binary(self).is_equivalent(_binary(other)))

            return bool(self.genus() == other.genus())

        def _sub_form_module(
            self: Any,
            gram: Matrix,
            generating_set: Any,
        ) -> Any:
            r"""Return the lattice on ``gram``: a sublattice of a lattice is one.

            The form restricted to a subobject is still $\mathbb Z$-valued, so
            what it makes is a lattice, refined and decomposed like any other.
            """
            return _lattice_with_gram(gram, generating_set)

        # ---- the radical, and the axioms defined by it ----

        @cached_method
        def dual_module(self: Any) -> Any:
            r"""Return $\operatorname{Hom}(L,\mathbb Z)$, free on the dual basis.

            The dual as a *module*, which every lattice has: $\operatorname{Hom}$
            into $\mathbb Z$ of a free module of rank $n$ is free of rank $n$,
            with no condition on the form.  It carries no form -- the one on
            $L^\vee$ is $G^{-1}$, and that is where nondegeneracy is needed.
            """
            return BasedFreeModule(ZZ, self.generating_set())

        @cached_method
        def correlation_morphism(self: Any) -> Any:
            r"""Return $c: L\to\operatorname{Hom}(L,\mathbb Z)$, $v\mapsto b(v,-)$.

            Always defined, and the map the radical and nondegeneracy are
            about: $b(v,-)$ is a functional on $L$ whatever the form does, and
            its matrix in the dual basis is $G$.  :meth:`correlation` is this
            same map with $\operatorname{Hom}(L,\mathbb Z)$ carrying the form
            that makes it $L^\vee$, which exists only when $c$ is injective.
            """
            dual_module = self.dual_module()
            assignment = dict(
                zip(
                    self.generating_set(),
                    (
                        dual_module.linear_combination(row)
                        for row in self.gram_matrix().rows()
                    ),
                )
            )
            homset = module_homset(self, dual_module)
            return homset.zero() if not assignment else homset(assignment)

        @cached_method
        def radical(self: Any) -> Subobject:
            r"""Return $\operatorname{rad}(L)=\ker(c)$, as a subobject.

            $\{v: b(v,w)=0 \text{ for all } w\}$ is by definition the set of
            $v$ killed by $v\mapsto b(v,-)$, so the radical is that map's
            kernel and is computed as one -- not as a Gram-matrix kernel that
            happens to agree with it.
            """
            return self.correlation_morphism().kernel()

        def is_nondegenerate(self: Any) -> bool:
            r"""Return whether $\operatorname{rad}(L)=0$, i.e. $c$ is injective.

            The radical being the zero object, asked of it.  Not that it has
            rank $0$ -- a nonzero torsion module has rank $0$ too, and a kernel
            is not obliged to be free.
            """
            return self.radical().is_zero()

        def is_unimodular(self: Any) -> bool:
            r"""Return whether $c: L\to L^\vee$ is an isomorphism.

            Injective and surjective, which are the two conditions separately:
            $\operatorname{rad}(L)=0$ is $\ker c=0$, and $A_L=\operatorname{coker}c$
            being trivial is the rest.  Unimodular is not "nondegenerate with
            $|\det|=1$" here -- it is $c$ being invertible, and these are the
            kernel and cokernel that say so.
            """
            return self.is_nondegenerate() and self.discriminant_group().cardinality() == 1

        # ---- invariants of the form, computed by the realization ----

        def signature_pair(self: Any) -> tuple:
            r"""Return $(p,q)$: the positive and negative indices of inertia.

            Sylvester's law over $\mathbb Q$, which is a fact about the form
            and needs nothing else -- in particular not nondegeneracy, so a
            degenerate lattice has one too, with a radical of dimension
            $n-p-q$.
            """
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            positive, negative, _radical = QuadraticForm(
                QQ, matrix(QQ, self.gram_matrix())
            ).signature_vector()
            return (positive, negative)

        def is_even(self: Any) -> bool:
            r"""Return whether $q(x)\in 2\mathbb Z$ for every $x$.

            Checked on the generators, which is all of them:
            $q(\sum a_ie_i)=\sum a_i^2q(e_i)+2\sum_{i<j}a_ia_jb(e_i,e_j)$, and
            the second sum is even whatever the lattice is, so $q$ is even
            exactly when every $q(e_i)$ is.
            """
            return all(generator.q() % 2 == 0 for generator in self.gens())

        def genus(self: Any) -> Any:
            r"""Return the genus symbol: the local data of the form at every place.

            Conway and Sloane's symbol, computed by Sage from the Gram matrix.
            An algorithm, and a matrix is all it takes -- so this is a call to
            it, not a passage into Sage's lattice objects.
            """
            from sage.quadratic_forms.genera.genus import Genus

            gram = matrix(ZZ, self.gram_matrix())
            assert gram.det() != 0, (
                f"{self} is degenerate, and a genus is the data of a "
                "nondegenerate form at each place. A degenerate form has a "
                "radical, and the question is probably about the quotient by it."
            )
            return Genus(gram)

        # ---- Nikulin / signature predicates ----

        @cached_method
        def dual(self: Any) -> "FormModule":
            r"""Return $L^\vee$: free on the dual generators, Gram $G^{-1}$.

            An object, not a set of vectors.  Sage's ``dual_lattice`` returns
            $\{x\in L\otimes\mathbb Q:\langle x,L\rangle\subseteq\mathbb Z\}$,
            which makes the correlation look like an inclusion and the form look
            like a property of a shared ambient.
            """
            assert self.is_nondegenerate(), (
                f"{self} is degenerate, so it has no $L^\\vee$: the form on the "
                "dual is $G^{-1}$, and $c$ is not injective here. The dual as a "
                "module is dual_module(), which always exists, and the "
                "obstruction is radical()."
            )
            gram = self.gram_matrix().inverse()
            return BilinearForm(
                BasedFreeModule(ZZ, self.generating_set()),
                QQ,
                gram,
            )

        @cached_method
        def correlation(self: Any) -> "FormMorphism":
            r"""Return $c: L\to L^\vee$, $v\mapsto\langle v,-\rangle$, matrix $G$.

            Nondegeneracy is injectivity of $c$, unimodularity is $c$ being an
            isomorphism, and $A_L=\operatorname{coker} c$.
            """
            # Cached because $L^\vee$ is an object, not a value: two calls have
            # to return the same one or its elements would have different
            # parents and nothing could be composed with $c$.
            return correlation_of(self)

        def discriminant_bilinear_form(self: Any) -> "FormModule":
            r"""Return $(A_L, b)$ with $b: A_L\times A_L\to\mathbb Q/\mathbb Z$.

            The always-defined discriminant form: $b$ needs nothing of $L$
            beyond nondegeneracy, whereas $q$ needs $L$ even.  It is the
            cokernel of :meth:`correlation`.
            """
            return DiscriminantBilinearModules().cokernel(self.correlation())

        def discriminant_quadratic_form(self: Any) -> Any:
            r"""Return $(A_L, q)$ with $q: A_L\to\mathbb Q/2\mathbb Z$.

            Gated on evenness: moving a lift by $\ell\in L$ shifts
            $b(\tilde x,\tilde x)$ by $b(\ell,\ell)$, which lies in
            $2\mathbb Z$ exactly when $L$ is even.  For an odd $L$ there is no
            such $q$, and :meth:`discriminant_bilinear_form` is all there is.
            """
            return DiscriminantQuadraticModules().cokernel(self.correlation())

        def discriminant_group(
            self: Any, s: Any = 0, *, reduce_trivial: bool = False
        ) -> Any:
            r"""Return $A_L=\operatorname{coker}(c: L\to L^\vee)$ with the form $L$ supports.

            $q$ when $L$ is even, $b$ alone when it is odd -- two different
            categories, so which one comes back is a fact about $L$ and not a
            flag on the answer.

            The generators are the dual basis and the relations are the ones
            $c$ induces, so this is the cokernel on the nose.  A unimodular
            summand of $L$ still contributes its generators; the relations kill
            them, and they appear as trivial components and zero blocks rather
            than vanishing.  ``reduce_trivial`` drops them, which is a
            *different* object -- a different finitely presented group -- not
            another view of this one.

            The invariant-factor basis is likewise a different object, reached
            by an isometry: see ``invariant_factor_form``, alongside
            ``normal_form``.

            Three distinct things are in play.

            * ``self.gens()`` are the basis vectors $e_i$ of $L$.
            * :meth:`dual_lattice_generators` are the $e_i^\vee$ of $L^\vee$.
            * :meth:`dual_embedding` is $c$ itself, whose matrix is $G$ -- in
              the $e_i^\vee$ basis it is generally not the identity; for
              $A_1(-1)^n$ it is $2I$.

            A displayed row in the catalogue is therefore turned into an element
            of $L^\vee$ with :meth:`dual_lattice_element` first, and only then
            projected.
            """
            cache = f"_preamble_discriminant_group_{bool(reduce_trivial)}"
            cached = self.__dict__.get(cache)
            if ZZ(s) == 0 and cached is not None:
                return cached

            correlation = self.correlation()
            # Which form A_L carries is a fact about L, not a flag on the answer.
            category = (
                DiscriminantQuadraticModules()
                if self.is_even()
                else DiscriminantBilinearModules()
            )
            form = category.cokernel(correlation)
            if reduce_trivial:
                # Keep the surviving generators as they are: regenerating on the
                # Smith basis would be a different object again, not this one
                # with the trivial components dropped.
                surviving = [
                    generator for generator in form.gens() if generator.order() != 1
                ]
                form = form.regenerate(surviving)
            if ZZ(s) != 0:
                return form.primary_part(s)
            setattr(self, cache, form)
            return form

        def is_coeven(self: Any) -> bool:
            r"""Return whether the discriminant form is integer-valued ($\delta=0$)."""
            from sage.rings.infinity import Infinity
            from sage.rings.rational_field import QQ

            disc = self.discriminant_group()
            assert disc.cardinality() < Infinity, (
                "discriminant group is infinite; the lattice must be nondegenerate"
            )
            return all(QQ(element.q()).denominator() == 1 for element in disc)

        def is_coodd(self: Any) -> bool:
            """Return the negation of :meth:`is_coeven`."""
            return not self.is_coeven()

        def delta(self: Any) -> Integer:
            r"""Return Nikulin's invariant $\delta\in\{0,1\}$."""
            return Integer(0) if self.is_coeven() else Integer(1)

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether the discriminant group $A_L$ is elementary abelian of exponent $p$.

            Defers to :meth:`DiscriminantQuadraticModules.ParentMethods.is_p_elementary`
            on ``self.discriminant_group()``.
            """
            disc = self.discriminant_group()
            return bool(disc.is_p_elementary(p))

        def is_elliptic(self: Any) -> bool:
            """Return whether the lattice is negative definite."""
            return bool((-self.gram_matrix()).is_positive_definite())

        def is_parabolic(self: Any) -> bool:
            """Return whether the lattice is negative semidefinite."""
            return bool((-self.gram_matrix()).is_positive_semidefinite())

        # ---- naming and display ----

        def with_names(self: Any, spec: str) -> Any:
            r"""Attach basis names from a compact spec and return the lattice.

            EXAMPLES::

                sage: from dzack_research.preamble import catalogue
                sage: Lattices.E8.with_names("a1..a8").variable_names()
                ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8')
            """
            self._assign_names(_expand_names(spec, self.rank()))
            return self

        def to_lin_comb_generators(self: Any, element: Any) -> str:
            r"""Return an element as a linear combination of the named basis."""
            names = self.variable_names()
            coords = element._coordinates()
            terms = []
            for name, c in zip(names, coords, strict=True):
                if c == 0:
                    continue
                if c == 1:
                    terms.append(name)
                elif c == -1:
                    terms.append(f"-{name}")
                else:
                    terms.append(f"{c}*{name}")
            return " + ".join(terms).replace("+ -", "- ") if terms else "0"

        @property
        def sublattices(self: Any) -> dict:
            r"""Return the per-instance dictionary of named sublattices."""
            existing = self.__dict__.get("_sublattices")
            if existing is None:
                existing = {}
                self._sublattices = existing
            return existing

        # ---- orthogonal direct sum / twist ----

        def direct_sum(
            self: Any,
            *others: Any,
            names: Any = None,
        ) -> Any:
            r"""Construct an orthogonal direct sum with its ordered subobjects.

            Orthogonal means the Gram matrix is block diagonal in the
            generators of the summands laid end to end, which is the whole
            construction: the sum is the lattice on that matrix, and its
            decomposition is found the way every lattice's is.
            """
            if not others:
                return self

            result = self
            for other in others:
                expected = _summand_ranks(result) + _summand_ranks(other)
                generating_set = _direct_sum_framing_set(result, other)
                result = _lattice_with_gram(
                    block_diagonal_matrix(
                        [matrix(ZZ, result.gram_matrix()), matrix(ZZ, other.gram_matrix())]
                    ),
                    generating_set,
                )
                # Both operands were split on their own construction, and the
                # summed Gram is block diagonal across them, so the sum's
                # components are exactly the two lists concatenated -- nothing
                # to search for, only to check.
                assert _summand_ranks(result) == expected, (
                    "direct sum disagrees with its summands: "
                    f"{_summand_ranks(result)} != {expected}"
                )

            return _apply_names(result, names) if names is not None else result

        def twist(self: Any, scale: Any, names: Any = None) -> Any:
            r"""Return $L(n)$: the same module with the form scaled by ``scale``.

            Scaling the Gram leaves the generators and their orthogonality
            alone, so the twist splits exactly where ``self`` does; its own
            construction finds that, and each summand comes back twisted.
            """
            result = BilinearForm(
                self.forget_form(),
                ZZ,
                ZZ(scale) * matrix(ZZ, self.gram_matrix()),
            )
            assert _summand_ranks(result) == _summand_ranks(self), (
                "twisting changed the decomposition: "
                f"{_summand_ranks(result)} != {_summand_ranks(self)}"
            )
            if names is not None:
                result = _apply_names(result, names)
            return result

        # ---- morphisms / automorphisms ----

        def Hom(self: Any, codomain: Any) -> Any:
            r"""Return $\mathrm{Hom}(L,M)$, whose elements are form-preserving.

            A form morphism is one already: :class:`FormMorphism` is built from
            where the generators go and checks $f^*b_M=b_L$ on construction, so
            the homset's job is only to say which maps it is the set of, and to
            read the several ways a caller names one.
            """
            return lattice_homset(self, codomain)

        def Aut(self: Any) -> Any:
            r"""Return $\mathrm{Aut}(L)=O(L)$ as an endomorphism Homset.

            Elements are constructed by their images on the framing labels.
            """
            cached = self.__dict__.get("_preamble_Aut")
            if cached is not None:
                return cached
            # An automorphism group is the endomorphism homset with one more
            # condition on its elements, so it is built the same way and
            # refined once more.
            refined = refine(
                FormAutomorphismGroup(self),
                [LatticeHomomorphisms(), LatticeIsometries()],
            )
            self._preamble_Aut = refined
            return refined

        def with_action(self: Any, group: Any, generator_images: Any) -> Any:
            r"""Return this lattice carrying the $G$-action these isometries generate."""
            action = GroupAction.from_generators(
                group,
                self,
                tuple(generator_images),
            )
            return group_lattice(self, action)

        def _acted_on_by(self: Any, action: Any) -> Any:
            r"""Return this lattice with the group ``action`` generates acting on it.

            ``action`` is an isometry or a finite literal subgroup of \(O(L)\).
            """
            match action:
                case FormMorphism() if action in self.Aut():
                    subgroup = action.cyclic_subgroup()
                case LatticeIsometrySubgroup() if action.domain() is self:
                    subgroup = action
                case _:
                    raise TypeError(
                        "a lattice action is an isometry or a literal subgroup "
                        "of its isometry homset"
                    )
            images = [
                self.Aut()(
                    {
                        label: generator(self.generator(label))
                        for label in self.generating_set()
                    }
                )
                for generator in subgroup.gens()
            ]
            return self.with_action(subgroup, images)

        def invariant_lattice(self: Any, action: Any) -> Any:
            r"""Return $L^G\hookrightarrow L$, the fixed sublattice.

            The trivial isotypic component of the $\mathbb Z[G]$-module, with
            the form restricted to it -- see
            :meth:`GroupLattices.ParentMethods.invariant_lattice`.  Not
            $\ker(g-\mathrm{id})$: that is one way to compute this component,
            and computing it that way here would state the method as the
            definition.
            """
            return self._acted_on_by(action).invariant_lattice()

        def coinvariant_lattice(self: Any, action: Any) -> Any:
            r"""Return the formed coinvariants $(L^G)^{\perp L}\hookrightarrow L$."""
            return self.formed_coinvariants(action)

        def formed_coinvariants(self: Any, action: Any) -> Any:
            r"""Return $(L^G)^{\perp L}\hookrightarrow L$."""
            return self._acted_on_by(action).formed_coinvariants()

        def coinvariant_inclusion(self: Any, action: Any) -> Any:
            r"""Return the primitive inclusion $(L^G)^{\perp}\hookrightarrow L$.

            Which is the coinvariant subobject's own structure morphism: a
            subobject is an object equipped with its inclusion, so there is
            nothing here to build.
            """
            return self.coinvariant_lattice(action).embedding()

        def _induced_lattice(self: Any, coordinate_basis: Any) -> Any:
            """Return the integral lattice with Gram form induced on ``coordinate_basis``."""
            basis = list(coordinate_basis)
            if not basis:
                return None
            gram = self.gram_matrix()
            induced = matrix(
                ZZ,
                [[u * gram * v for v in basis] for u in basis],
            )
            assert induced.is_symmetric(), (
                "induced form on the sublattice is not symmetric"
            )
            generators = tuple(
                self.linear_combination(row)
                for row in basis
            )
            return _lattice_with_gram(
                induced,
                finite_ordered_set(generators),
            )

        # ---- constructor sugar ----

        def _first_ngens(self: Any, count: int) -> tuple[Any, ...]:
            r"""Return generators matching the declared name slots."""
            generators = self.gens()
            spec = getattr(self, "_ellipsis_spec", None)
            if spec is None or len(spec) != count:
                return tuple(generators[:count])
            names = list(self.variable_names())
            return tuple(
                Ellipsis if slot == "Ellipsis" else generators[names.index(slot)]
                for slot in spec
            )

        def __add__(self: Any, other: Any) -> Any:
            r"""``L + M`` as the orthogonal direct sum (for ``sum([...])``)."""
            return self.direct_sum(other)

        def __radd__(self: Any, other: Any) -> Any:
            """Allow ``sum([L, M, ...])`` (Python starts from ``0``)."""
            if other == 0:
                return self
            return NotImplemented

        def __pow__(self: Any, exponent: Any, names: Any = None) -> Any:
            r"""``L ^ n`` as the ``n``-fold orthogonal direct sum."""
            n = int(exponent)
            assert n >= 1, f"lattice power needs a positive exponent, got {exponent}"
            result = self
            for _ in range(n - 1):
                result = result.direct_sum(self)
            if names is not None:
                result = _apply_names(result, names)
            return result

        def _repr_(self: Any) -> str:
            pos, neg = self.signature_pair()
            return (
                f"Integral lattice of rank {self.rank()} and signature "
                f"({pos}, {neg})"
            )

        # ---- LaTeX ----

        def _latex_(self: Any) -> str:
            r"""Multi-line LaTeX with rank, signature, discriminant, Gram, discriminant group."""
            rank = self.rank()
            pos, neg = self.signature_pair()
            disc = self.gram_matrix().det()
            disc_latex = _format_disc_latex(disc)
            gram_latex = str(_latex_fn(self.gram_matrix()))
            if _zero_dots():
                gram_latex = re.sub(r"\b0\b", lambda m: r"\cdot", gram_latex)

            A = self.discriminant_group()
            A_latex = str(_latex_fn(A))
            A_lines = [line for line in A_latex.splitlines() if line]
            assert A_lines[0].strip() == r"\begin{gathered}"
            assert A_lines[-1].strip() == r"\end{gathered}"
            A_lines = A_lines[1:-1]

            header = [
                r"\begin{gathered}",
                (
                    f"L \\in \\mathrm{{Lattices}}(\\mathbb{{Z}}), "
                    f"\\quad \\mathrm{{rk}}(L) = {rank}, "
                    f"\\quad \\mathrm{{sig}}(L) = ({pos}, {neg}), "
                    f"\\quad \\mathrm{{disc}}(L) = {disc_latex} \\\\"
                ),
            ]

            # Equality, not isometry: the summands are this lattice's own
            # generators, partitioned.
            decomposition = _decomposition_latex(self)
            if decomposition is None and not self.is_decomposable():
                decomposition = _summand_name(self)
            if decomposition is not None:
                header.append(f"L = {decomposition} \\\\")

            header.append(f"G_L = {gram_latex} \\\\")
            return "\n".join(header + A_lines + [r"\end{gathered}"])

    class ElementMethods:
        r"""What a lattice vector adds to being an element of a form module.

        The pairing, the norm and $v*w$ are :class:`FormModules`', because they
        are what having a form means.  What is here is the vocabulary a lattice
        vector is asked in -- $q$ for the norm, divisibility, primitivity -- and
        the constructions that need $L$ to be integral.
        """

        def q(self: Any) -> Any:
            r"""Return $q(v) = \langle v, v\rangle$: the norm, under its name here."""
            return self.norm()

        def div(self: Any) -> Any:
            r"""Return the divisibility of this vector."""
            return self.parent().div(self)

        def is_primitive(self: Any) -> bool:
            r"""Return whether $L/\mathbb Zv$ is torsion free.

            Equivalently, whether the coordinates of $v$ have no common factor:
            $v=nw$ for some $w\in L$ exactly when $n$ divides all of them.
            """
            return abs(gcd(list(self._coordinates()))) == 1

        def __pow__(self: Any, exponent: Any, mod: Any = None) -> Any:
            r"""``v ^ 2`` -> $q(v)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

        def e_perp_mod_e(self: Any) -> Any:
            r"""$e^\perp/\langle e\rangle$, which is this element's isotropic reduction."""
            return self.isotropic_reduction()


# ---- helper utilities ----

_ZERO_DOTS: bool = True

def set_zero_dots(enabled: bool = True) -> None:
    r"""Toggle replacing 0 entries with $\cdot$ in lattice LaTeX."""
    global _ZERO_DOTS
    _ZERO_DOTS = bool(enabled)

def _zero_dots() -> bool:
    return _ZERO_DOTS

def _lattice_with_gram(
    gram: Any,
    generating_set: Any = None,
) -> "FormModule":
    r"""Return the integral lattice on ``gram``, refined and decomposed.

    The one construction: a Gram matrix becomes a form on $\mathbb Z^n$, the
    form becomes the lattice, and the lattice finds its own decomposition.
    Everything that produces a lattice from a matrix -- a direct sum, a twist,
    an induced form on a sublattice, a quotient, an overlattice -- comes
    through here, so there is one place where a lattice is born.
    """
    gram = matrix(ZZ, gram)
    match generating_set:
        case None:
            generating_set = Sets.Δ[gram.nrows() - 1]
        case _:
            generating_set = finite_ordered_set(generating_set)
            assert generating_set.cardinality() == gram.nrows(), (
                "the framing set and Gram matrix have different cardinalities"
            )
    lattice = BilinearForm(
        BasedFreeModule(
            ZZ,
            generating_set,
        ),
        ZZ,
        gram,
    )
    return lattice


def _direct_sum_framing_set(left: Any, right: Any) -> Any:
    r"""Return the ordered coproduct of two finite framing sets."""
    labels = tuple(
        (0, label) for label in left.generating_set()
    ) + tuple(
        (1, label) for label in right.generating_set()
    )
    return finite_ordered_set(labels)

def _discriminant_lift_row(element: Any, rank: int) -> list[Any]:
    r"""Return a representative row in $L^*$ for a discriminant-group element."""
    assert isinstance(element, FormModuleElement), (
        f"glue is defined on classes in A_L, and this is {element!r}. Build an "
        "element of L^v with dual_lattice_element(...), then project it with "
        "project_to_discriminant_group(...); a coordinate vector is not a "
        "discriminant class until someone says which combination of generators "
        "it names."
    )
    lift = element.parent().projection().lift(element)
    row = [QQ(coordinate) for coordinate in lift._coordinates()]
    assert len(row) == rank, (
        f"discriminant element lift has rank {len(row)}, expected {rank}"
    )
    return row

def _expand_names(spec: str, rank: int) -> tuple[str, ...]:
    r"""Expand indexed ranges in a basis-name specification."""
    names: list[str] = []
    for piece in (p.strip() for p in spec.split(",")):
        assert piece, f"empty name in spec {spec!r}"
        match = re.fullmatch(r"([A-Za-z_]+)(\d+)\.\.\1?(\d+)", piece)
        if match:
            stem, start, stop = match.group(1), int(match.group(2)), int(match.group(3))
            names.extend(f"{stem}{i}" for i in range(start, stop + 1))
        else:
            assert re.fullmatch(r"[A-Za-z_]\w*", piece), f"invalid name: {piece!r}"
            names.append(piece)

    assert len(names) == rank, (
        f"spec {spec!r} gives {len(names)} names but rank is {rank}"
    )
    assert len(set(names)) == rank, f"duplicate names in {spec!r}"
    return tuple(names)

def _expand_ellipsis_names(names: tuple[str, ...]) -> tuple[str, ...]:
    r"""Expand ``('a1','Ellipsis','a8')`` through ``'a8'``."""
    expanded: list[str] = []
    for i, name in enumerate(names):
        if name != "Ellipsis":
            expanded.append(name)
            continue
        assert 0 < i < len(names) - 1, (
            f"'...' needs a name on each side; got {names}"
        )
        before, after = expanded[-1], names[i + 1]
        # Allow an alphabetic suffix so ``a1t, ..., a8t`` expands.
        left = re.fullmatch(r"([A-Za-z_]+)(\d+)([A-Za-z_]*)", before)
        right = re.fullmatch(r"([A-Za-z_]+)(\d+)([A-Za-z_]*)", after)
        assert left and right, f"'...' needs indexed names: {before}, {after}"
        assert left.group(1) == right.group(1) and left.group(3) == right.group(3), (
            f"'...' between different stems: {before} and {after}"
        )
        start, stop = int(left.group(2)), int(right.group(2))
        assert stop > start, f"'...' range does not ascend: {before}..{after}"
        stem, suffix = left.group(1), left.group(3)
        expanded.extend(f"{stem}{i}{suffix}" for i in range(start + 1, stop))
    return tuple(expanded)

def _apply_names(lattice: Any, names: Any) -> Any:
    r"""Expand a declared name tuple onto a lattice, checking rank."""
    declared = tuple(names)
    expanded = _expand_ellipsis_names(declared)
    assert len(expanded) == lattice.rank(), (
        f"{declared} expands to {len(expanded)} names but rank is {lattice.rank()}"
    )
    lattice._assign_names(expanded)
    lattice._ellipsis_spec = declared
    return lattice

def _subdivide_gram(L: Any, *cuts: Any) -> None:
    r"""Subdivide a lattice's Gram matrix, handling immutability."""
    form = L.form()
    gram = form.gram_matrix()
    if gram.is_immutable():
        from copy import copy

        gram = copy(gram)
        form._gram_matrix = gram
    gram.subdivide(*cuts)

def _decompose_lattice(L: Any) -> None:
    r"""Split \(L\) along its generators and record the summands.

    Decomposability here is a property of the chosen generating set: \(L\)
    *equals* a direct sum exactly when its Gram matrix is block diagonal in the
    generators it was built with.  A splitting that would need the generators
    permuted is a different object, and
    :func:`_matrix_connected_component_cuts` declines it.

    The direct-sum structure is a separate object.  It is not grafted onto
    \(L\), so another decomposition may coexist with this one.
    """
    gram = L.gram_matrix()
    cuts = _matrix_connected_component_cuts(gram)
    if not cuts:
        L._orthogonal_decomposition = None
        return

    bounds = list(zip([0] + cuts, cuts + [gram.nrows()]))
    labels = tuple(L.generating_set())
    blocks = [
        _lattice_with_gram(
            gram.submatrix(start, start, end - start, end - start),
            finite_ordered_set(labels[start:end]),
        )
        for start, end in bounds
    ]

    _subdivide_gram(L, cuts, cuts)
    generators = tuple(L.gens())
    summands = tuple(
        Subobject(block.Hom(L)(generators[start:end]))
        for block, (start, end) in zip(blocks, bounds)
    )
    L._orthogonal_decomposition = DirectSum(L, summands)


def _summand_ranks(L: Any) -> tuple[int, ...]:
    r"""Return the ranks of \(L\)'s summands, or its own rank when indecomposable."""
    if L.is_decomposable():
        return tuple(summand.rank() for summand in L.summands())
    return (L.rank(),)

# ---- summand names ----

#: Gram matrix -> LaTeX name, for the indecomposable lattices worth naming.
#: ``catalogue.sage`` fills this in; the lookup is empty and harmless until then.
_INDECOMPOSABLE_NAMES: dict[tuple, str] = {}


def _gram_key(gram: Any) -> tuple:
    r"""Return a hashable form of a Gram matrix, ignoring any subdivisions."""
    return tuple(tuple(row) for row in gram.rows())


def register_indecomposable(name: str, lattice: Any) -> None:
    r"""Register *lattice*'s Gram matrix under the LaTeX *name*.

    Matching is Gram equality, not isometry: a block **is** the named lattice
    when the matrices agree, so nothing here asserts a theorem.  Decomposable
    entries are refused -- they can never appear as a block, so registering one
    would be dead weight that reads as if it could match.
    """
    assert not lattice.is_decomposable(), (
        f"{name} is decomposable, so it can never be a summand; "
        "name it by aggregating the summand list instead"
    )
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(lattice.gram_matrix()), name)


def _summand_name(block: Any) -> str | None:
    r"""Return the catalogue name for *block*, or ``None`` if unrecognized.

    An exact match wins over a twisted one, and a positive scale over its
    negative, so \(\langle-2\rangle\) reports as $I_{0,1}(2)$ rather than
    $I_{1,0}(-2)$.
    """
    gram = block.gram_matrix()
    exact = _INDECOMPOSABLE_NAMES.get(_gram_key(gram))
    if exact is not None:
        return exact

    content = gcd(gram.list())
    for scale in (content, -content):
        if scale in (0, 1, -1):
            continue
        untwisted = _INDECOMPOSABLE_NAMES.get(
            _gram_key((gram / scale).change_ring(ZZ))
        )
        if untwisted is not None:
            return f"{untwisted}({scale})"

    return None


def _decomposition_latex(L: Any) -> str | None:
    r"""Return ``N_1 \oplus N_2 \oplus ...`` for *L*, or ``None`` if it has no summands.

    Unrecognized blocks fall back to a positional name; a lattice whose blocks
    are all unrecognized has nothing to say beyond its Gram matrix.
    """
    if not L.is_decomposable():
        return None
    names = [
        _summand_name(subobject)
        for subobject in L.summands()
    ]
    if all(name is None for name in names):
        return None
    return " \\oplus ".join(
        name if name is not None else f"L_{{{i + 1}}}"
        for i, name in enumerate(names)
    )


def _format_disc_latex(disc: int) -> str:
    r"""Format discriminant with prime factorization in LaTeX."""
    from sage.arith.misc import factor

    if disc in (-1, 0, 1):
        return str(disc)
    f = factor(disc)
    f_latex = str(_latex_fn(f))
    return f"{disc} = {f_latex}" if f_latex != str(disc) else str(disc)

def refine_one_lattice(lattice: Any) -> None:
    r"""Refine a single integral lattice into the appropriate categories.

    Always refines into ``IntegralLattices``.  If signature is ``(n, 1)``,
    also joins ``HyperbolicLattices``.
    """
    refine(lattice, IntegralLattices())
    pos, neg = lattice.signature_pair()
    if pos > 0 and neg > 0 and min(pos, neg) == 1:
        refine(lattice, HyperbolicLattices())

_NAMED_GRAM_MATRICES: dict[str, Any] = {
    # The two names for the hyperbolic plane; the ADE names are read below.
    "U": matrix(ZZ, [[0, 1], [1, 0]]),
    "H": matrix(ZZ, [[0, 1], [1, 0]]),
}


def _gram_from_name(name: str) -> Matrix:
    r"""Return the Gram matrix a lattice name stands for.

    A name is not a lattice: ``"A5"`` names a matrix, and which matrix is what
    the Cartan matrix of the root system says.  So this reads the name and
    hands back the matrix, and the lattice is built from it here like every
    other one.

    The convention is the root system's -- $A_n$ comes out positive definite,
    with $2$ on the diagonal -- and the catalogue twists by $-1$ where this
    project wants the negative definite one.
    """
    known = _NAMED_GRAM_MATRICES.get(name)
    if known is not None:
        return known

    match = re.fullmatch(r"([ADE])(\d+)", name)
    assert match, (
        f"{name!r} does not name a lattice here. The names are U and H for "
        "the hyperbolic plane and An, Dn, En for the root lattices; anything "
        "else is given by its Gram matrix."
    )
    from sage.combinat.root_system.cartan_matrix import CartanMatrix

    return matrix(ZZ, CartanMatrix([match.group(1), ZZ(match.group(2))]))


def _integral_lattice_with_names(
    *args: Any,
    names: Any = None,
    generating_set: Any = None,
    **kwargs: Any,
) -> Any:
    r"""Return the integral lattice these arguments describe.

    A Gram matrix or a name, which is a matrix once it is read.  Nothing here
    passes through Sage's lattice class: that class is a submodule of a
    rational ambient and imposes nondegeneracy, and neither is part of what a
    lattice is here -- a Coxeter root span with an $m=\infty$ bond is
    degenerate and is still one.
    """
    assert len(args) == 1 and not kwargs, (
        "a lattice is built from its Gram matrix, or from a name that stands "
        f"for one; got {args!r} and {kwargs!r}"
    )
    described = args[0]
    gram = described if isinstance(described, Matrix) else _gram_from_name(described)
    lattice = _lattice_with_gram(gram, generating_set)
    if names is not None:
        lattice = _apply_names(lattice, names)
    return lattice
