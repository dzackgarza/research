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

        * Rank or signature mismatch: empty, unconditionally.
        * Degenerate: $\operatorname{rad}(L)$ is a summand pairing to zero,
          so $L\cong 0^{r}\oplus L/\operatorname{rad}(L)$; equal signature
          pairs force equal radical ranks and the nondegenerate quotients
          recurse.
        * Rank $\le 1$: $\operatorname{diag}(a)\cong\operatorname{diag}(b)$
          iff $a=b$ (the units of $\mathbb Z$ are $\pm1$, acting by squares).
        * Definite: the engine decision (PARI ``qfisom``) on the *doubled*,
          sign-normalized Gram matrices -- ``QuadraticForm`` reads its
          matrix as the Hessian $2G$.
        * Indefinite rank $\ge 3$: Eichler (SPLAG ch. 15 Thm 14, CS10,
          Zotero T2WVLTDB): the class is the improper spinor genus, so when
          the shared genus carries a single improper spinor genus, genus
          equality decides.  A genus that splits into several improper
          spinor genera is a stated gap -- Sage enumerates spinor genera
          but cannot *place* a form into one -- and the answer is the
          three-valued ``Unknown``.
        * Indefinite rank $2$: Gauss-composition territory, no theorem this
          method owns; ``Unknown``.
        """
        from sage.misc.unknown import Unknown
        from sage.quadratic_forms.genera.genus import Genus as _sage_genus
        from sage.quadratic_forms.quadratic_form import QuadraticForm

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
        if left.rank() <= 1:
            return bool(
                matrix(SageZZ, left.gram_matrix())
                != matrix(SageZZ, right.gram_matrix())
            )
        if positive == 0 or negative == 0:
            sign = 1 if negative == 0 else -1
            return not bool(
                QuadraticForm(
                    SageZZ, 2 * sign * matrix(SageZZ, left.gram_matrix())
                ).is_globally_equivalent_to(
                    QuadraticForm(
                        SageZZ, 2 * sign * matrix(SageZZ, right.gram_matrix())
                    )
                )
            )
        if left.rank() == 2:
            return Unknown
        genus_left = _sage_genus(matrix(SageZZ, left.gram_matrix()))
        if genus_left != _sage_genus(matrix(SageZZ, right.gram_matrix())):
            return True
        if not genus_left.spinor_generators(proper=False):
            # One improper spinor genus: genus equality IS isometry (Eichler).
            return False
        return Unknown

    def an_element(self) -> "Morphism":
        r"""A distinguished isometry; defined exactly when nonempty.

        The identity when the ends are one object; otherwise the witness is
        the engine's transformation (PARI ``qfisom``), implemented on the
        definite regime -- Sage's stack carries no witness engine elsewhere,
        and that absence is stated by name, never padded over.
        """
        from sage.quadratic_forms.quadratic_form import QuadraticForm

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
        assert positive == 0 or negative == 0, (
            "an explicit isometry witness is implemented on the definite "
            "regime (PARI qfisom); Sage's stack has no witness engine for "
            f"indefinite lattices; signature={left.signature_pair()}"
        )
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.utilities import zipsum
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
    enumeration.  Indefinite existence is the Nikulin embedding engine,
    issue #24 -- a stated absence, asserted by name at this boundary.
    """

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
            "short-vector engine's); indefinite existence is issue #24's "
            "Nikulin engine"
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
        for _ in self:
            return False
        return True

    def an_element(self) -> "Morphism":
        for embedding in self:
            return embedding
        assert False, (
            f"Emb({self.domain()}, {self.codomain()}) is empty; existence "
            "is the homset's emptiness question"
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
