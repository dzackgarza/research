r"""Orbits of non-isotropic vectors under $O(L)$ and its subgroups
containing $\ker\varphi$.

The sibling of :mod:`isotropic_orbits`.  There the objects are primitive
totally isotropic sublattices and the whole theory runs through the engine's
isotropic machinery; here the object is a single vector $w$ with
$q(w)\neq 0$, and the mathematics is Nikulin's gluing theory applied to the
primitive extension $w$ cuts out,

.. math::

    \mathbb Z w \oplus w^{\perp}\ \subseteq\ L ,

together with Dawes' three algorithms over it (Dawes 2021, *Orbits of
vectors in lattices*, sec. 2; transcribed in the migrated glossary
``notes/topics/coble-enriques-lattice-theory/``).

Three questions, three routes, all sited on the owned surfaces:

* **The decision, for a $\Gamma\le O(L)$ containing $\ker\varphi$.**  The
  isometries carrying $w_1$ to $w_2$ are the coset
  $\operatorname{Stab}_{O(L)}(w_2)\cdot W$ of one $O(L)$-witness $W$, so
  $\Gamma$ meets it exactly when $\varphi(W)$ lies in the identity double
  coset of $\varphi(\Gamma)\backslash\varphi(O(L))/
  \varphi(\operatorname{Stab}(w_2))$ in the finite quotient
  $\varphi=(\rho_L,\det,\operatorname{sn}_{\mathbb R})$ that
  :class:`isotropic_orbits.OrthogonalPredicateSubgroups` already carries.
  Every character cutting such a subgroup out factors through that finite
  quotient, so the test is a decision and not a search --
  ``vectors_are_equivalent`` on that subgroup
  is where it is asked.

* **Algorithm 2.1, the definite-complement route.**  When $w^{\perp}$ is
  definite its isometry group is finite, $\operatorname{Isom}(w_1^{\perp},
  w_2^{\perp})$ is an enumerable $O(w_2^{\perp})$-torsor, and each of its
  elements extends by $w_1\mapsto w_2$ to a rational map of $L$ that is an
  isometry exactly when it is integral.  This route *constructs* witnesses
  and needs no engine: :func:`definite_complement_extensions`.

* **Algorithms 2.2/2.3, the gluing route.**  When $w^{\perp}$ is indefinite
  no such enumeration exists, and the question moves to the discriminant
  forms: $L$ is an even overlattice of $M=\mathbb Zw\oplus w^{\perp}$, named
  by the isotropic gluing subgroup $H=L/M\le A_M$ (Nik80 Prop. 1.4.1), and
  $A_L=H^{\perp}/H$.  A pair of discriminant-form isometries, one of the
  line factor and one of the complement factor, assembles to an isometry of
  $A_M$; the pairs carrying $H_1$ to $H_2$ are exactly the ones descending
  to $A_L$, and the classes they induce there are what
  :func:`gluing_route_discriminant_classes` returns.

Three errors recorded against the source corpus's backend are corrected
here, and the corrected mathematics is what lands:

1. *The line factor was restricted to $\pm\mathrm{id}$.*  A cyclic
   discriminant form $\mathbb Z/m$ with $q(g)=a/m$ admits multiplication by
   every unit $u$ with $(u^{2}-1)a\equiv 0 \pmod{2m}$, which is more than
   $\pm1$: for $q(w)=12$, $u=5$ satisfies $25\cdot\frac1{12}=\frac1{12}+2$.
   Restricting to $\pm1$ can miss an admissible gluing and answer "no" when
   the answer is yes.  Nothing here special-cases the rank-one factor: both
   factors range over the *owned* $O(A)$ of their discriminant form, which
   is the general notion, and the missing units come back with it.

2. *The claimed splitting of the direct-sum discriminant was never checked*
   (the source's ``_assert_direct_sum_generator_split`` had an empty body,
   while every later step assumed what it named).  Here the two injections
   $A_{\mathbb Zw}\to A_M$ and $A_{w^{\perp}}\to A_M$ are built as owned
   morphisms -- so the receiving homset verifies that each preserves the
   form -- and the splitting is asserted positively in
   :class:`VectorPrimitiveExtension`: the images generate $A_M$, $|H|$ is
   the index $[L:M]$, $H$ is isotropic, and $\det G_M=\det G_L\,[L:M]^2$.

3. *A bounded search reported "no" for "not found".*  The source adjusted a
   witness by products of at most two reflections in roots drawn from the
   engine plus a scan of the coefficient box $[-6,6]^{\mathrm{rk}}$, and
   reported ``False`` when that search came up empty -- neither bound being
   a theorem.  That search is not reproduced.  The decision is the finite
   quotient's double coset, which is complete; and the reflections
   themselves land as what they actually are, a named family inside the
   stable orthogonal group (:func:`stable_complement_root_reflections`),
   never as a fallback whose failure is reported as an answer.

Convention: matrices act on coordinate rows on the right, the preamble's
morphism-matrix convention throughout.
"""

from typing import TYPE_CHECKING

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    from collections.abc import Iterator

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModule,
        FormMorphism,
    )
    from dzack_research.preamble.lexicon import Element


# ---- the O(L) layer: engine data, validated against the owned lattice ----


def _held(lattice: "FormModule", element: "Element") -> "Element":
    return element if element.parent() is lattice else lattice(element)


def _validated_anisotropic_vector(
    lattice: "FormModule", element: "Element"
) -> "Element":
    r"""Assert what a vector-orbit representative is; return it unchanged.

    Non-isotropic, because the isotropic theory is a different one and lives
    in :mod:`isotropic_orbits`; and primitive, because $dv$ and $v$ are
    carried by the same isometries, so the orbit question on $dv$ *is* the
    orbit question on $v$ and asking it twice would be two spellings.
    """
    held = _held(lattice, element)
    assert held.q() != 0, (
        f"{held} is isotropic; the orbits of isotropic vectors are lines, "
        "asked of isotropic_line_orbit_representatives"
    )
    assert held.is_primitive(), (
        f"{held} is not primitive.  An isometry carries $dv$ to $dw$ exactly "
        "when it carries $v$ to $w$, so ask the question of the primitive "
        "vector $v$"
    )
    return held


def _coordinate_row(lattice: "FormModule", element: "Element") -> list:
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
    return [int(entry) for entry in _coordinate_vector(_held(lattice, element))]


def orthogonal_group_vector_equivalence_witness(
    lattice: "FormModule", left: "Element", right: "Element"
) -> "FormMorphism | None":
    r"""Return $g\in O(L)$ with $g(v)=w$, or ``None`` when there is none.

    The engine's vector equivalence
    (:func:`engines.vector_equivalence_witness`,
    ``INDEF_FORM_TestEquivalenceVector``), crossed back as a morphism of
    $O(L)$ whose constructor re-asserts form preservation.  Unlike the line
    question this is asked at one sign only: $v$ and $-v$ are different
    vectors, and an isometry carrying one to the other is a different
    element of the orbit.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import vector_equivalence_witness
    source = _validated_anisotropic_vector(lattice, left)
    target = _validated_anisotropic_vector(lattice, right)
    if source.q() != target.q():
        return None
    witness = vector_equivalence_witness(
        matrix(SageZZ, lattice.gram_matrix()),
        _coordinate_row(lattice, source),
        _coordinate_row(lattice, target),
    )
    if witness is None:
        return None
    isometry = lattice.Aut()._isometry_on_rows(witness.rows())
    assert isometry(source) == target, (
        "the engine's witness does not carry the source vector to the target"
    )
    return isometry


def orthogonal_group_vector_stabilizer_generators(
    lattice: "FormModule", element: "Element"
) -> tuple:
    r"""Return generators of $\operatorname{Stab}_{O(L)}(v)$, as isometries.

    Engine generators (``INDEF_FORM_StabilizerVector``) crossed back as
    morphisms; each is verified here to fix the vector, and that they
    generate the whole pointwise stabilizer is the engine's contract, which
    is what makes the double-coset decision on
    :class:`isotropic_orbits.OrthogonalPredicateSubgroups` a decision.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import vector_stabilizer_generator_matrices
    held = _validated_anisotropic_vector(lattice, element)
    generators = tuple(
        lattice.Aut()._isometry_on_rows(generator.rows())
        for generator in vector_stabilizer_generator_matrices(
            matrix(SageZZ, lattice.gram_matrix()),
            _coordinate_row(lattice, held),
        )
    )
    assert all(generator(held) == held for generator in generators), (
        "an engine stabilizer generator moves the vector it must fix"
    )
    return generators


# ---- the primitive extension a non-isotropic vector cuts out ----


class VectorPrimitiveExtension:
    r"""The primitive extension $\mathbb Zw\oplus w^{\perp}\subseteq L$.

    Nikulin's data (Nik80 §§1.4--1.5, Zotero TTY9FFJS) for one anisotropic
    primitive $w$: the line $S=\mathbb Zw$ and its orthogonal complement
    $R=w^{\perp}$ are primitive and mutually orthogonal of complementary
    rank, so $M=S\oplus R$ sits in $L$ with finite index and $L$ is the
    integral overlattice of $M$ glued along the isotropic subgroup
    $H=L/M\le A_M$, with $A_L\cong H^{\perp}/H$.  Which form $A_M$ carries
    follows $M$ -- $q$ when $L$ is even, $b$ alone when it is odd -- and the
    correspondence covers the integral overlattices either way; only the
    gluing *route* below asks for evenness, where it ranges over isometries
    of discriminant quadratic forms.

    Everything below is computed once at construction and asserted there.
    The attributes are the mathematics: two summands, their sum, the
    inclusion, the two discriminant injections, the gluing subgroup, and the
    representatives in $A_M$ of $A_L$'s generators.

    The class of $x\in L$ in $A_M$ is read off the form and not off a
    coordinate inversion: $A_M$ is generated by the classes of $M^{\vee}$'s
    dual generators, dual to $M$'s own, so the class of $x$ has dual
    coordinates $(b(x,m_1),\dots,b(x,m_n))$ -- integral exactly because
    $M\subseteq L$ and the form of $L$ is integral.
    """

    def __init__(self, lattice: "FormModule", element: "Element") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.sets.cardinals import cardinal
        from dzack_research.preamble.utilities import zipsum

        vector = _validated_anisotropic_vector(lattice, element)
        line = lattice.subobject_on((vector,))
        complement = line.embedding().orthogonal_complement()
        assert complement.rank() >= 1, (
            f"{lattice} has rank one, where w spans it rationally and two "
            "primitive vectors of equal square differ by a sign; there is no "
            "gluing theory to run"
        )
        assert line.rank() + complement.rank() == lattice.rank(), (
            "the orthogonal complement of an anisotropic line has "
            "complementary rank; a degenerate form is the only way out"
        )
        sum_lattice = line.direct_sum((complement,))

        inclusion_rows = matrix(SageZZ, line.embedding().matrix()).stack(
            matrix(SageZZ, complement.embedding().matrix())
        )
        index = abs(SageZZ(inclusion_rows.determinant()))
        assert index != 0, "the two summands do not span L rationally"
        assert (
            matrix(SageZZ, sum_lattice.gram_matrix()).determinant()
            == matrix(SageZZ, lattice.gram_matrix()).determinant() * index**2
        ), (
            "det(M) = det(L) [L : M]^2 fails; the summands do not carry the "
            "whole extension"
        )

        sum_form = sum_lattice.discriminant_group()
        line_form = line.discriminant_group()
        complement_form = complement.discriminant_group()
        sum_generators = tuple(sum_form.module_generators())
        line_injection = line_form.Hom(sum_form)(
            dict(
                zip(
                    line_form.module_generating_set(),
                    sum_generators[: line.rank()],
                    strict=True,
                )
            )
        )
        complement_injection = complement_form.Hom(sum_form)(
            dict(
                zip(
                    complement_form.module_generating_set(),
                    sum_generators[line.rank():],
                    strict=True,
                )
            )
        )
        # The splitting A_M = A_S (+) A_R, asserted rather than assumed: the
        # two homsets have already verified that each injection preserves the
        # form, and what is left is that the images fill A_M and meet only in
        # zero -- one statement, since |A_S| |A_R| = |A_M| holds by the block
        # diagonal Gram.
        images = tuple(
            line_injection(generator)
            for generator in line_form.module_generators()
        ) + tuple(
            complement_injection(generator)
            for generator in complement_form.module_generators()
        )
        assert (
            sum_form.subobject_generated_by(images).cardinality()
            == sum_form.cardinality()
        ), "the two discriminant injections do not generate A_M"

        embedded_generators = tuple(
            zipsum(row, lattice.module_generators(), lattice.zero())
            for row in inclusion_rows.rows()
        )
        sum_dual = sum_form.projection().domain()

        def sum_class(dual_row: tuple) -> "Element":
            return sum_form.projection()(
                zipsum(
                    tuple(SageZZ(entry) for entry in dual_row),
                    sum_dual.module_generators(),
                    sum_dual.zero(),
                )
            )

        gluing_subobject = sum_form.subobject_generated_by(
            tuple(
                sum_class(
                    tuple(
                        generator.b(embedded)
                        for embedded in embedded_generators
                    )
                )
                for generator in lattice.module_generators()
            )
        )
        assert gluing_subobject.cardinality() == cardinal(index), (
            "the gluing subgroup L/M must have order [L : M]"
        )
        assert sum_form.form_vanishes_on(
            tuple(_subobject_images(gluing_subobject))
        ), "the gluing subgroup of an even overlattice is isotropic (Nik80 1.4.1)"

        # A_L -> A_M/H: the class of L's i-th dual generator has dual
        # coordinates the i-th column of the inclusion rows, because the
        # pairing of e_i^dual with the j-th generator of M is that
        # generator's i-th coordinate in L's framing.  Well defined only
        # modulo H, which is why it is kept as representatives.
        discriminant_form = lattice.discriminant_group()
        discriminant_representatives = tuple(
            sum_class(tuple(inclusion_rows.column(position)))
            for position in range(lattice.rank())
        )
        gluing_images = _subobject_images(gluing_subobject)
        assert all(
            representative.b(glued) == 0
            for representative in discriminant_representatives
            for glued in gluing_images
        ), "the representatives of A_L must lie in H-perp"

        self.lattice = lattice
        self.vector = vector
        self.line = line
        self.complement = complement
        self.sum_lattice = sum_lattice
        self.sum_form = sum_form
        self.line_form = line_form
        self.complement_form = complement_form
        self.line_injection = line_injection
        self.complement_injection = complement_injection
        self.inclusion_rows = inclusion_rows
        self.index = index
        self.gluing_subobject = gluing_subobject
        self.gluing_images = gluing_images
        self.discriminant_form = discriminant_form
        self.discriminant_representatives = discriminant_representatives

    def _representative_table(self) -> dict:
        r"""Return the lookup $H^{\perp}\to A_L$, built once and on demand.

        Ranging over $A_L$ and over $H$, so it is paid for only by the
        callers that invert the correspondence -- the gluing route -- and not
        by the ones that only want the summands or the index.
        """
        table = self.__dict__.get("_representative_table_cache")
        if table is not None:
            return table
        table = {}
        for discriminant_class in self.discriminant_form:
            representative = self.representative_of(discriminant_class)
            for glued in self.gluing_images:
                table[representative + glued] = discriminant_class
        assert (
            len(table)
            == abs(matrix(SageZZ, self.lattice.gram_matrix()).determinant())
            * self.index
        ), (
            "A_L -> A_M/H is not injective; the cosets of H hit by the "
            "representatives overlap"
        )
        self._representative_table_cache = table
        return table

    def representative_of(self, discriminant_class: "Element") -> "Element":
        r"""Return a representative in $A_M$ of a class of $A_L$."""
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _coordinates_in_module_generators
        from dzack_research.preamble.utilities import zipsum
        return zipsum(
            _coordinates_in_module_generators(
                self.discriminant_form(discriminant_class),
                self.discriminant_form.module_generating_set(),
            ),
            self.discriminant_representatives,
            self.sum_form.zero(),
        )

    def class_of_representative(self, element: "Element") -> "Element":
        r"""Return the class of $A_L$ an element of $H^{\perp}$ represents.

        The inverse of :meth:`representative_of`, which is a bijection
        $A_L\to H^{\perp}/H$; a lookup failure means the element was not in
        $H^{\perp}$ to begin with.
        """
        table = self._representative_table()
        assert element in table, (
            f"{element} lies outside H-perp, so it represents no class of A_L"
        )
        return table[element]

    def complement_is_definite(self) -> bool:
        r"""Return whether $w^{\perp}$ is definite: which route decides."""
        positive, negative = self.complement.signature_pair()
        return positive == 0 or negative == 0

    def __repr__(self) -> str:
        return (
            f"Primitive extension of {self.vector} in {self.lattice} "
            f"of index {self.index}"
        )


def _subobject_images(subobject: "FormModule") -> tuple:
    r"""Return a subobject's elements seen in the codomain of its embedding."""
    embedding = subobject.embedding()
    return tuple(embedding(element) for element in subobject)


def vector_primitive_extension(
    lattice: "FormModule", element: "Element"
) -> VectorPrimitiveExtension:
    r"""Return $\mathbb Zw\oplus w^{\perp}\subseteq L$ for an anisotropic $w$."""
    return VectorPrimitiveExtension(lattice, element)


# ---- Dawes Algorithm 2.1: the definite-complement route ----


def definite_complement_extensions(
    lattice: "FormModule", left: "Element", right: "Element"
) -> "Iterator[FormMorphism]":
    r"""Yield every $g\in O(L)$ with $g(w_1)=w_2$, for definite complements.

    Dawes 2021 Algorithm 2.1.  An isometry carrying $w_1$ to $w_2$ carries
    $w_1^{\perp}$ to $w_2^{\perp}$, and is determined by that restriction
    together with $w_1\mapsto w_2$; conversely a $\psi\in
    \operatorname{Isom}(w_1^{\perp},w_2^{\perp})$ extends to a rational map
    of $L$, which is an isometry of $L$ exactly when it is integral -- and
    integrality is where the finite index $[L:M]$ enters, since $\psi$ is
    free to move the gluing data.

    So the route is complete: it yields *all* of them, and a caller wanting
    the ones in a subgroup filters by membership.  It runs exactly when
    $w_1^{\perp}$ is definite, because that is what makes
    $\operatorname{Isom}(w_1^{\perp},w_2^{\perp})$ enumerable -- it is an
    $O(w_2^{\perp})$-torsor, and the isometry homset already enumerates it
    that way.  For an indefinite complement that group is infinite and the
    question moves to :func:`gluing_route_discriminant_classes`.
    """
    if _held(lattice, left).q() != _held(lattice, right).q():
        return
    source = vector_primitive_extension(lattice, left)
    target = vector_primitive_extension(lattice, right)
    assert source.complement_is_definite(), (
        f"{source.complement} is indefinite, so its isometries are not "
        "enumerable; the gluing route is what decides that regime"
    )
    inverse_rows = matrix(SageQQ, source.inclusion_rows).inverse()
    for restriction in source.complement.Isom(target.complement):
        block = matrix(SageZZ, 1, 1, [1]).block_sum(
            matrix(SageZZ, restriction.matrix())
        )
        candidate = inverse_rows * block * matrix(SageQQ, target.inclusion_rows)
        if not all(entry in SageZZ for entry in candidate.list()):
            continue
        # The group's own constructor asserts form preservation, so an
        # extension that is integral but not an isometry fails loudly here.
        isometry = lattice.Aut()._isometry_on_rows(
            candidate.change_ring(SageZZ).rows()
        )
        assert isometry(source.vector) == target.vector, (
            "the assembled extension does not carry w_1 to w_2"
        )
        yield isometry


# ---- Dawes Algorithms 2.2/2.3: the gluing route ----


def _discriminant_isometries(
    source: "FormModule", target: "FormModule", start: "FormMorphism"
) -> "Iterator[FormMorphism]":
    r"""Yield every isometry $A\to B$, as the $O(B)$-torsor on one of them.

    A nonempty set of isometries between two finite forms is a torsor under
    the codomain's orthogonal group, so one witness and the owned $O(B)$
    name all of them -- no search over generator images, and in particular
    no rank-one special case: the units $u$ with $u^2 q(g)=q(g)$ that are
    not $\pm1$ arrive as elements of $O(B)$ like every other isometry.
    """
    assert start.domain() is source and start.codomain() is target, (
        "the torsor is generated from an isometry between the two forms"
    )
    for automorphism in target.automorphism_group():
        yield start.then(automorphism)


def gluing_route_discriminant_classes(
    lattice: "FormModule", left: "Element", right: "Element"
) -> "Iterator[FormMorphism]":
    r"""Yield the classes in $O(A_L)$ induced by isometries $w_1\mapsto w_2$.

    Dawes 2021 Algorithms 2.2 and 2.3, on the owned gluing vocabulary.
    Write $M_k=\mathbb Zw_k\oplus w_k^{\perp}$ and $H_k=L/M_k\le A_{M_k}$
    (:class:`VectorPrimitiveExtension`).  An isometry of $L$ carrying $w_1$
    to $w_2$ restricts to the two summands, so it induces an isometry
    $A_{M_1}\to A_{M_2}$ splitting as a pair -- one isometry of the line
    factor's discriminant form, one of the complement's -- and it carries
    $H_1$ to $H_2$.  Conversely such a pair descends to
    $H_1^{\perp}/H_1\to H_2^{\perp}/H_2$, which is $A_{L}\to A_L$: that
    class is what this yields.

    Both factors range over the *whole* set of isometries of their
    discriminant forms, generated as a torsor under the owned $O(A)$.  The
    rank-one factor is not special-cased, which is correction (1) of the
    module docstring.

    Hypotheses, asserted rather than assumed: the complements are indefinite
    (the definite regime is Algorithm 2.1's, where witnesses are constructed
    outright), the complements are isometric as lattices (otherwise no
    isometry of $L$ can match them), and $\rho_L:O(L)\to O(A_L)$ is
    surjective -- which is what makes a class yielded here the class of an
    actual isometry of $L$, asked of the lattice by
    :meth:`IntegralLattices.ParentMethods.discriminant_representation_is_surjective`.
    """
    from sage.misc.unknown import Unknown

    assert lattice.is_even(), (
        "this route ranges over isometries of discriminant *quadratic* "
        f"forms; {lattice} is odd, the stated absence "
        "IntegralLattices.glue_map also declares"
    )
    if _held(lattice, left).q() != _held(lattice, right).q():
        return
    source = vector_primitive_extension(lattice, left)
    target = vector_primitive_extension(lattice, right)
    assert not source.complement_is_definite(), (
        "Algorithms 2.2/2.3 are stated for an indefinite complement; the "
        "definite regime is definite_complement_extensions"
    )
    assert lattice.discriminant_representation_is_surjective(), (
        f"the gluing route reads an isometry of {lattice} off a class of "
        "O(A_L), which needs rho_L surjective; it is not for this lattice"
    )
    # An isometry of $L$ carrying $w_1$ to $w_2$ restricts to one of the
    # complements, so their being isometric is necessary.  The three-valued
    # answer is kept three-valued: an undecided regime is not a negative.
    complements_agree = source.complement.is_isometric(target.complement)
    assert complements_agree is not Unknown, (
        f"whether {source.complement} and {target.complement} are isometric "
        "is undecided (indefinite binary, or a genus splitting into several "
        "improper spinor genera), so this route cannot answer either"
    )
    if complements_agree is False:
        return

    # Both line factors are the discriminant form of the same rank-one
    # lattice <q(w)>, so the generator-to-generator map is an isometry --
    # and the homset says so rather than this line claiming it.
    line_start = source.line_form.Hom(target.line_form)(
        dict(
            zip(
                source.line_form.module_generating_set(),
                target.line_form.module_generators(),
                strict=True,
            )
        )
    )
    complement_start = (
        source.complement.Isom(target.complement)
        .an_element()
        .discriminant_isometry()
    )
    discriminant_form = lattice.discriminant_group()
    sum_labels = tuple(source.sum_form.module_generating_set())
    line_rank = source.line.rank()
    target_gluing = frozenset(target.gluing_images)
    for line_isometry in _discriminant_isometries(
        source.line_form, target.line_form, line_start
    ):
        line_images = dict(
            zip(
                sum_labels[:line_rank],
                (
                    target.line_injection(line_isometry(generator))
                    for generator in source.line_form.module_generators()
                ),
                strict=True,
            )
        )
        for complement_isometry in _discriminant_isometries(
            source.complement_form, target.complement_form, complement_start
        ):
            images = dict(line_images)
            images.update(
                zip(
                    sum_labels[line_rank:],
                    (
                        target.complement_injection(
                            complement_isometry(generator)
                        )
                        for generator in source.complement_form.module_generators()
                    ),
                    strict=True,
                )
            )
            # The homset constructor is the verification that the pair
            # assembles to an isometry of the summed discriminant form.
            assembled = source.sum_form.Hom(target.sum_form)(images)
            if (
                frozenset(
                    assembled(glued) for glued in source.gluing_images
                )
                != target_gluing
            ):
                continue
            yield discriminant_form.automorphism_group()(
                {
                    label: target.class_of_representative(
                        assembled(
                            source.representative_of(
                                discriminant_form.module_generator(label)
                            )
                        )
                    )
                    for label in discriminant_form.module_generating_set()
                }
            )


# ---- the reflections of the complement that act trivially on A_L ----


def stable_complement_root_reflections(
    lattice: "FormModule", element: "Element"
) -> tuple:
    r"""Return the reflections in roots of $w^{\perp}$ lying in $\tilde O(L)$.

    A root $r\in w^{\perp}$ of square $\pm2$ reflects $L$ integrally --
    $2b(x,r)/q(r)=\mp b(x,r)\in\mathbb Z$ -- and $s_r$ fixes $w$, being the
    identity on $r^{\perp}\supseteq\mathbb Zw$.  Kept are the ones acting
    trivially on the discriminant form, which is membership in the stable
    orthogonal group $\tilde O(L)=\ker\rho_L$; their products therefore move
    a witness's determinant and real spinor norm without moving its
    discriminant class.

    One reflection per $O(w^{\perp})$-orbit of roots, which is what an
    indefinite complement admits: the roots themselves are infinite in
    number, the orbits are finitely many, and the engine exhibits one
    representative each.  So this is a family of examples inside
    $\tilde O(L)\cap\operatorname{Stab}(w)$ and never an enumeration of it;
    nothing here decides emptiness, and no caller may read an empty answer
    as the absence of an adjusting isometry.
    """
    held = _validated_anisotropic_vector(lattice, element)
    complement = lattice.subobject_on((held,)).embedding().orthogonal_complement()
    positive, negative = complement.signature_pair()
    assert positive != 0 and negative != 0, (
        f"{complement} is definite, where the roots are finitely many and "
        "enumerate_short_vectors lists them all; this orbit-representative "
        "family is the indefinite statement"
    )
    stable = lattice.stable_orthogonal_group()
    embedding = complement.embedding()
    reflections = []
    for square in (2, -2):
        for root in complement.Aut().vector_orbit_representatives(square):
            reflection = lattice.reflection(embedding(root))
            assert reflection(held) == held, (
                "a reflection in a root of w-perp must fix w"
            )
            if reflection in stable:
                reflections.append(reflection)
    return tuple(reflections)
