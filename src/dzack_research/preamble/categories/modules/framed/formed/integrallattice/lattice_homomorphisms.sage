r"""Form-preserving homomorphisms of integral lattices."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormHomset
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism

from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.sets.owned_sets import Sets


if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from typing import TypeAlias

    from sage.categories.morphism import SetMorphism
    from sage.misc.unknown import Unknown
    from sage.structure.element import Element
    from sage.structure.parent import MembershipInput

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism

    # How a lattice map may be named: an assignment on the framing labels, an
    # ordered list of images, an existing morphism, or a function on the
    # framing set.
    LatticeMapSpecification: TypeAlias = (
        SetMorphism | dict | list | tuple | Callable
    )

    class LatticeHomsetParent(Protocol):
        r"""What a lattice homset offers: the lattice its morphisms leave."""

        def domain(self) -> "Module": ...


class LatticeHomomorphisms(Category):
    r"""Native form morphisms between integral lattices."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def __call__(
            self: "LatticeHomsetParent",
            images: "LatticeMapSpecification",
        ) -> "Morphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobjects
            from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import _expand_direct_sum_hom_dict
            match images:
                case FormMorphism():
                    assert images.parent() is self, (
                        "an existing morphism belongs only to its own homset"
                    )
                    morphism: "Morphism" = images
                    return morphism
                case dict():
                    match any(source in Subobjects() for source in images):
                        case True:
                            expanded = _expand_direct_sum_hom_dict(
                                self.domain(),
                                images,
                            )
                            assignment = dict(
                                zip(
                                    self.domain().module_generating_set(),
                                    expanded,
                                    strict=True,
                                )
                            )
                        case False:
                            assignment = images
                case list() | tuple():
                    assert len(images) == self.domain().number_of_module_generators(), (
                        "the number of images does not match the framing set"
                    )
                    assignment = dict(
                        zip(self.domain().module_generating_set(), images)
                    )
                case _:
                    assert False, (
                        "a lattice morphism is declared by images of the "
                        "domain's framing labels"
                    )
            declared: "Morphism" = FormHomset._element_constructor_(self, assignment)
            return declared


def lattice_homset(domain: "Module", codomain: "Module") -> FormHomset:
    r"""Return the canonical lattice homset for ``domain`` and ``codomain``."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
    from dzack_research.preamble.refine import refine
    homset = FormModules.ParentMethods.Hom(domain, codomain)
    return refine(homset, LatticeHomomorphisms())


class IsometryHomset(FormHomset):
    r"""$\operatorname{Isom}(L, M)$: the possibly-empty set of isometries.

    Existence questions live on homsets as first-class parents (ratified
    method placement): emptiness owns the isometry decision, and
    ``IntegralLattices.ParentMethods.is_isometric`` is this homset's
    emptiness router.  When nonempty the homset is a torsor under
    $O(M)$ by postcomposition, which answers cardinality and enumeration
    exactly where $O(M)$ carries a grounded finiteness answer.
    """

    def __init__(self, domain: "Module", codomain: "Module") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        assert domain in IntegralLattices() and codomain in IntegralLattices(), (
            "Isom(L, M) is sited between integral lattices; base-change "
            "explicitly before asking for isometries of anything else"
        )
        FormHomset.__init__(
            self,
            domain,
            codomain,
            FormModules(domain.base_ring()),
        )

    def _repr_(self) -> str:
        return f"Isometries from {self.domain()} to {self.codomain()}"

    def is_empty(self) -> "bool | Unknown":
        r"""The isometry decision: every branch states the theorem it runs on.

        An obstruction ladder ordered by cost, cheap global invariants before
        local ones before decisions -- each screen is a necessary condition,
        so a failed screen answers *empty* outright and a passed screen only
        hands the question down.  This order is the implemented order; there
        is no second, documented-only order (the source corpus's backend
        documented one order and ran another, a recorded error corrected
        here).

        Screens, in order:

        * Rank, then signature pair (Sylvester): mismatch is empty.
        * Degenerate: $\operatorname{rad}(L)$ is a summand pairing to zero,
          so $L\cong 0^{r}\oplus L/\operatorname{rad}(L)$; equal signature
          pairs force equal radical ranks and the nondegenerate quotients
          recurse.
        * Rank $\le 1$: $\operatorname{diag}(a)\cong\operatorname{diag}(b)$
          iff $a=b$ (the units of $\mathbb Z$ are $\pm1$, acting by squares).
        * Parity: an even lattice is never isometric to an odd one -- $q$'s
          image in $\mathbb Z/2$ is an invariant.
        * Discriminant $d_\pm$: an isometry carries one Gram matrix to the
          other by a $GL_n(\mathbb Z)$ matrix, whose square determinant
          fixes $\det G$; the sign is a Witt-class invariant.
        * Discriminant-group isomorphism: $A_L=\operatorname{coker}(c)$ is
          functorial, so its invariant factors match.
        * Rational isometry: Hasse--Minkowski over $\mathbb Q$ (signature,
          discriminant square class, Hasse invariants), the engine's
          ``is_rationally_isometric`` on the doubled Gram matrices --
          simultaneous doubling preserves the relation.
        * Local isometry at every $p\mid 2\,d$: decided on the *canonical*
          $p$-adic genus symbols (Conway--Sloane ch. 15; the engine's
          ``LocalGenusSymbol`` equality canonicalizes at $2$).  Two lattices
          with different raw Jordan decompositions at $p$ can still be
          isometric over $\mathbb Z_p$ -- $\operatorname{diag}(1,2)$ and
          $\operatorname{diag}(3,6)$ at $p=2$, witnessed by
          $M=\begin{psmallmatrix}1&-2\\1&1\end{psmallmatrix}$ of 2-adic unit
          determinant $3$ -- so the raw symbol is never compared.  At
          $p\nmid 2d$ both localizations are unimodular of equal rank and
          determinant class, hence isometric, so these primes decide all of
          them; with the signature screen this *is* genus equality.
        * Discriminant-form isometry: $q_L$ (even) or $b_L$ (odd) up to
          isometry, decided by the torsion-form categories' own
          ``is_isomorphic`` (normal-form comparison behind the engine
          boundary).

        Decisions, on survivors:

        * Definite: the engine decision (PARI ``qfisom``) on the *doubled*,
          sign-normalized Gram matrices -- ``QuadraticForm`` reads its
          matrix as the Hessian $2G$.
        * Even, indefinite, 2-elementary: nonempty.  The genus of an even
          2-elementary lattice is determined by $(\delta; t_+, t_-, a)$ and,
          when both inertia indices are positive, those invariants determine
          the isometry class (Nikulin 1979 Thm 3.6.2 -- not 1.14.2, which is
          the general even-indefinite uniqueness criterion the proof of
          3.6.2 invokes; the source corpus cited both numbers for this
          statement and 3.6.2 is the one that states it).  The surviving
          screens carried exactly those invariants, so the branch concludes.
        * Indefinite rank $\ge 3$: Eichler (SPLAG ch. 15 Thm 14, CS10,
          Zotero T2WVLTDB): the class is the improper spinor genus, so when
          the shared genus -- equality already established by the screens --
          carries a single improper spinor genus, the homset is nonempty.
        * Remaining indefinite regimes (rank $2$; a genus splitting into
          several improper spinor genera): the exact witness engine
          (polyhedral_common ``INDEF_FORM_TestEquivalence`` behind
          :mod:`engines`), whose returned matrix is verified over
          $\mathbb Z$ at the seam and stored for :meth:`an_element`.  With
          the engine unprovisioned the answer is the three-valued
          ``Unknown``.
        """
        from sage.misc.unknown import Unknown
        from sage.quadratic_forms.genera.genus import Genus as _sage_genus
        from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        from sage.quadratic_forms.quadratic_form import QuadraticForm

        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import (
            indefinite_isometry_witness,
            polyhedral_engine,
        )

        left, right = self.domain(), self.codomain()
        if left.rank() != right.rank():
            return True
        if left.signature_pair() != right.signature_pair():
            return True
        positive, negative = left.signature_pair()
        radical_rank = left.rank() - positive - negative
        if radical_rank > 0:
            return IsometryHomset(
                left.radical_quotient(), right.radical_quotient()
            ).is_empty()
        gram_left = matrix(SageZZ, left.gram_matrix())
        gram_right = matrix(SageZZ, right.gram_matrix())
        if left.rank() <= 1:
            return bool(gram_left != gram_right)
        if left.is_even() != right.is_even():
            return True
        if left.discriminant() != right.discriminant():
            return True
        if (
            left.discriminant_group().invariants()
            != right.discriminant_group().invariants()
        ):
            return True
        from sage.rings.rational_field import QQ as SageQQ
        if not QuadraticForm(
            SageQQ, 2 * matrix(SageQQ, gram_left)
        ).is_rationally_isometric(
            QuadraticForm(SageQQ, 2 * matrix(SageQQ, gram_right))
        ):
            return True
        for prime in (2 * left.discriminant()).prime_factors():
            if LocalGenusSymbol(gram_left, prime) != LocalGenusSymbol(
                gram_right, prime
            ):
                return True
        if not left.discriminant_group().is_isomorphic(
            right.discriminant_group()
        ):
            return True
        if positive == 0 or negative == 0:
            sign = 1 if negative == 0 else -1
            return not bool(
                QuadraticForm(SageZZ, 2 * sign * gram_left).is_globally_equivalent_to(
                    QuadraticForm(SageZZ, 2 * sign * gram_right)
                )
            )
        if (
            left.is_even()
            and left.is_p_elementary(2)
            and right.is_p_elementary(2)
        ):
            # Nikulin 1979 Thm 3.6.2: (delta; t+, t-, a) determine the class
            # of an even indefinite 2-elementary lattice, and the screens
            # established their equality.
            return False
        if left.rank() >= 3:
            # Genus equality holds by the signature and local screens; the
            # remaining question is the spinor-genus count (Eichler).
            if not _sage_genus(gram_left).spinor_generators(proper=False):
                return False
        if polyhedral_engine() is None:
            return Unknown
        witness = indefinite_isometry_witness(gram_left, gram_right)
        if witness is None:
            return True
        # Store the verified witness so an_element does not re-run the engine.
        self._engine_witness_rows = witness.rows()
        return False

    def an_element(self) -> "Morphism":
        r"""A distinguished isometry; defined exactly when nonempty.

        The identity when the ends are one object.  On the definite regime
        the witness is the engine's transformation (PARI ``qfisom``).  On
        the indefinite regime it is polyhedral_common's
        ``INDEF_FORM_TestEquivalence`` witness behind :mod:`engines`,
        verified over $\mathbb Z$ at the seam -- and re-used when
        :meth:`is_empty` already ran the engine.  With that engine
        unprovisioned the absence is stated by name, never padded over.
        """
        from sage.quadratic_forms.quadratic_form import QuadraticForm

        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import (
            indefinite_isometry_witness,
            polyhedral_engine,
        )
        from dzack_research.preamble.utilities import zipsum

        empty = self.is_empty()
        assert empty is False, (
            f"Isom({self.domain()}, {self.codomain()}) has no exhibited "
            f"element; emptiness decision returned {empty}"
        )
        left, right = self.domain(), self.codomain()
        if left is right:
            return lattice_homset(left, right)(
                list(left.module_generators())
            )
        positive, negative = left.signature_pair()
        if positive != 0 and negative != 0:
            witness_rows = self.__dict__.get("_engine_witness_rows")
            if witness_rows is None:
                assert polyhedral_engine() is not None, (
                    "an explicit indefinite isometry witness is the "
                    "polyhedral_common engine's (INDEF_FORM_TestEquivalence); "
                    "the engine is not provisioned -- see engines.sage"
                )
                witness = indefinite_isometry_witness(
                    matrix(SageZZ, left.gram_matrix()),
                    matrix(SageZZ, right.gram_matrix()),
                )
                assert witness is not None, (
                    "is_empty answered nonempty but the witness engine "
                    "found no isometry; one of the two is wrong"
                )
                witness_rows = witness.rows()
            # The homset's own constructor asserts form preservation, so the
            # seam's verification is re-run where the morphism is built.
            return lattice_homset(left, right)(
                [
                    zipsum(row, right.module_generators(), right.zero())
                    for row in witness_rows
                ]
            )
        sign = 1 if negative == 0 else -1
        transformation = matrix(
            SageZZ,
            QuadraticForm(
                SageZZ, 2 * sign * matrix(SageZZ, right.gram_matrix())
            ).is_globally_equivalent_to(
                QuadraticForm(
                    SageZZ, 2 * sign * matrix(SageZZ, left.gram_matrix())
                ),
                return_matrix=True,
            ),
        )
        # The homset's own constructor asserts form preservation, so an
        # engine convention mismatch fails loudly here rather than passing.
        return lattice_homset(left, right)(
            [
                zipsum(
                    transformation.column(index),
                    right.module_generators(),
                    right.zero(),
                )
                for index in range(left.rank())
            ]
        )

    def acting_group(self) -> "FormHomset":
        r"""$O(M)$: the nonempty homset is an $O(M)$-torsor by postcomposition."""
        return self.codomain().Aut()

    def cardinality(self) -> "Element | Unknown":
        r"""$0$ when empty; $|O(M)|$ when nonempty; ``Unknown`` propagates."""
        empty = self.is_empty()
        if empty is True:
            return SageZZ(0)
        if empty is False:
            return self.acting_group().cardinality()
        return empty

    def __iter__(self) -> "Iterator":
        r"""Torsor enumeration $\{g\circ f_0 : g\in O(M)\}$; implemented
        exactly where $O(M)$ is finite, asserted by name elsewhere."""
        if self.is_empty() is True:
            return
        aut = self.acting_group()
        assert aut.is_finite(), (
            f"Isom({self.domain()}, {self.codomain()}) enumerates through "
            "its O(M)-torsor structure, which requires O(M) finite; extend "
            "the group engine, do not special-case"
        )
        witness = self.an_element()
        for automorphism in aut:
            yield witness.then(automorphism)

    def transporter(self, source: "Morphism", target: "Morphism") -> "Morphism":
        r"""Return the unique $g\in O(M)$ with $g\circ\mathrm{source}=\mathrm{target}$.

        The nonempty homset is an $O(M)$-torsor by postcomposition, and a
        torsor's action is free and transitive, so the transporter exists,
        is unique, and is $g=\mathrm{target}\circ\mathrm{source}^{-1}$ --
        constructed in $O(M)$ by its images on the codomain's framing
        labels, with no search.  An isometry is invertible, so ``lift``
        through ``source`` is total and *is* $\mathrm{source}^{-1}$.
        """
        assert source in self and target in self, (
            "the transporter carries one isometry of this homset to another"
        )
        codomain = self.codomain()
        return self.acting_group()(
            {
                label: target(
                    source.lift(codomain.module_generator(label))
                )
                for label in codomain.module_generating_set()
            }
        )

    def __contains__(self, candidate: "MembershipInput") -> bool:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        return (
            isinstance(candidate, FormMorphism)
            and candidate.domain() is self.domain()
            and candidate.codomain() is self.codomain()
            and bool(candidate.matrix().is_square())
            and bool(candidate.matrix().is_invertible())
        )


class EmbeddingHomset(FormHomset):
    r"""$\operatorname{Emb}(L, M)$: the form-preserving monomorphisms.

    Enumeration is by depth-first module-generator placement where the
    codomain is integral *definite*: each module generator has finitely many
    candidate images -- the codomain's vectors of its square, delivered by
    the short-vector engine -- pruned by the pairing constraints against the
    module generators already placed.  Emptiness and the distinguished element ride on the
    enumeration.

    For an even unimodular *indefinite* codomain (issue #24, closed):
    emptiness is decided natively -- an embedding saturates to a primitive
    one, so $\operatorname{Emb}(L, M)\ne\emptyset$ exactly when some even
    overlattice of $L$ (an isotropic subgroup of $A_L$, finitely many)
    satisfies Nikulin's primitive-embedding criterion
    (:meth:`IntegralLattices.ParentMethods.embeds_in_even_unimodular`,
    Nik80 Thm 1.12.2) -- and the distinguished element is produced by the
    OSCAR/Hecke construction composed with a polyhedral_common isometry
    witness carrying its codomain onto this one (the even unimodular
    indefinite genus holds one class).  Enumeration there is still absent:
    the homset is infinite, a stated absence at this boundary.  Other
    indefinite codomains remain issue #24's residue, asserted by name.
    """

    def _codomain_is_even_unimodular_indefinite(self) -> bool:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.definite_lattices import DefiniteLattices
        codomain = self.codomain()
        positive, negative = codomain.signature_pair()
        return (
            codomain not in DefiniteLattices()
            and positive > 0
            and negative > 0
            and bool(codomain.is_even())
            and abs(matrix(SageZZ, codomain.gram_matrix()).determinant()) == 1
        )

    def _even_overlattice_inclusions(self) -> "Iterator[Morphism]":
        r"""Iterate $L\hookrightarrow L'$ over the even overlattices of $L$.

        Nik80 Prop 1.4.1: overlattices correspond to isotropic subgroups of
        the discriminant form, and for an even $L$ the quadratic form's
        isotropic subgroups name exactly the even ones.  The identity
        (the empty gluing) is included.
        """
        form = self.domain().discriminant_group()
        for subobject in form.isotropic_subobjects():
            yield form.overlattice_from_isotropic_subobject(subobject)

    def __init__(self, domain: "Module", codomain: "Module") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        assert domain in IntegralLattices() and codomain in IntegralLattices(), (
            "Emb(L, M) is sited between integral lattices"
        )
        FormHomset.__init__(
            self,
            domain,
            codomain,
            FormModules(domain.base_ring()),
        )

    def _repr_(self) -> str:
        return f"Embeddings of {self.domain()} into {self.codomain()}"

    def __iter__(self) -> "Iterator":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.definite_lattices import DefiniteLattices
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        domain, codomain = self.domain(), self.codomain()
        assert codomain in DefiniteLattices() and codomain.rank() > 0, (
            "embedding enumeration is implemented for integral definite "
            "codomains (finiteness of the module-generator engine is the "
            "short-vector engine's); an indefinite homset is infinite -- "
            "existence and a distinguished element are is_empty() and "
            "an_element(), enumeration is a stated absence"
        )
        gram = matrix(SageZZ, domain.gram_matrix())
        rank = domain.rank()
        positive, negative = codomain.signature_pair()
        wrong_sign = 1 if negative == codomain.rank() else -1
        if any(wrong_sign * gram[i, i] > 0 for i in range(rank)):
            return  # a definite form takes values of one sign only
        pools = [
            tuple(codomain.vectors_of_square(gram[i, i]))
            for i in range(rank)
        ]

        def assign(placed: list) -> "Iterator":
            position = len(placed)
            if position == rank:
                columns = matrix(
                    SageZZ,
                    [_coordinate_vector(image) for image in placed],
                )
                if columns.rank() == rank:
                    yield lattice_homset(domain, codomain)(list(placed))
                return
            for candidate in pools[position]:
                if all(
                    placed[j].b(candidate) == gram[j, position]
                    for j in range(position)
                ):
                    yield from assign([*placed, candidate])

        yield from assign([])

    def is_empty(self) -> bool:
        if self._codomain_is_even_unimodular_indefinite():
            if not self.domain().is_even():
                # An odd lattice has a generator of odd square, and every
                # vector of an even lattice has even square.
                return True
            # An embedding saturates to a primitive embedding of an even
            # overlattice, and conversely; so emptiness is the native
            # Nikulin criterion swept over the (finitely many) even
            # overlattices of the domain.
            positive, negative = self.codomain().signature_pair()
            return not any(
                inclusion.codomain().embeds_in_even_unimodular(
                    positive, negative
                )
                for inclusion in self._even_overlattice_inclusions()
            )
        for _ in self:
            return False
        return True

    def an_element(self) -> "Morphism":
        if self._codomain_is_even_unimodular_indefinite():
            return self._even_unimodular_element()
        for embedding in self:
            return embedding
        assert False, (
            f"Emb({self.domain()}, {self.codomain()}) is empty; existence "
            "is the homset's emptiness question"
        )

    def _even_unimodular_element(self) -> "Morphism":
        r"""Produce one embedding into the even unimodular indefinite codomain.

        The witness chain: an even overlattice $L'$ of $L$ satisfying
        Nikulin's criterion, its engine-built primitive embedding
        $L'\hookrightarrow M'$, and a polyhedral_common isometry witness
        $M'\to M$ (one class in the genus, so it exists); the composite is
        an element of this homset, verified by the same form-preservation
        check every morphism construction runs.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import indefinite_isometry_witness
        from dzack_research.preamble.utilities import zipsum

        codomain = self.codomain()
        assert self.domain().is_even(), (
            f"Emb({self.domain()}, {codomain}) is empty: an odd lattice "
            "has a generator of odd square, and every vector of an even "
            "lattice has even square"
        )
        positive, negative = codomain.signature_pair()
        for inclusion in self._even_overlattice_inclusions():
            overlattice = inclusion.codomain()
            if not overlattice.embeds_in_even_unimodular(positive, negative):
                continue
            primitive = overlattice.embed_in_even_unimodular(
                positive, negative
            )
            constructed = primitive.codomain()
            witness = indefinite_isometry_witness(
                matrix(SageZZ, constructed.gram_matrix()),
                matrix(SageZZ, codomain.gram_matrix()),
            )
            assert witness is not None, (
                "an indefinite even unimodular genus holds one isometry "
                "class, so the engine must produce a witness"
            )
            transport = lattice_homset(constructed, codomain)(
                [
                    zipsum(row, codomain.module_generators(), codomain.zero())
                    for row in witness.rows()
                ]
            )
            return inclusion.then(primitive).then(transport)
        assert False, (
            f"Emb({self.domain()}, {self.codomain()}) is empty: no even "
            "overlattice of the domain satisfies Nikulin's criterion "
            "(Nik80 Thm 1.12.2)"
        )

    def __contains__(self, candidate: "MembershipInput") -> bool:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        return (
            isinstance(candidate, FormMorphism)
            and candidate.domain() is self.domain()
            and candidate.codomain() is self.codomain()
            and bool(candidate.matrix().rank() == self.domain().rank())
        )
