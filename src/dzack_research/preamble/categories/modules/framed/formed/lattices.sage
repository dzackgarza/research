r"""``Lattices(R)``: projective modules carrying an $R$-valued bilinear form.

This category *is* ``SymmetricBilinearFormModules(R).Projective()``. It is
declared rather than composed: Sage models "this category, plus this axiom" as
the axiom's category class bound onto the category it refines, so a class that
names the pair and is bound with ``setattr`` is that join, under whatever name
suits it.  Both halves are the preamble's own classes, which is what the
device requires -- an axiom bound onto one of Sage's category classes is a
monkey-patch, and the module categories below are plain owned categories for
that reason.

A lattice is not a module with a bilinear form.  That is
``SymmetricBilinearFormModules(R)``, and it holds anything with a pairing.
What makes a lattice is that the module is **projective**, which is why the
axiom sits on ``Modules`` and this category is its join with the form.

Nothing here is finitely generated, integral, or nondegenerate.  Those are
three further axioms, and declining to impose them is what lets this category
hold $\ZZ^{\infty}$ with the standard form, or $SL_2(\ZZ)$ inside
$SL_2(\RR)$ with $b(x,y)=\operatorname{tr}(xy)$.

Named specimens (``Lattices.E8``, ``Lattices.U``, ...) are defined inline in
this namespace and attached after the class is bound, so the type checker sees
them and no other module patches them on.  The construction primitive lives in
``integral_lattices.sage``, which imports this class; importing it here at the
top would close the cycle, so the specimens are built at the bottom of this
module, once ``Lattices`` already names the class.
"""

from functools import cache
from typing import TYPE_CHECKING, ClassVar, TypeAlias

from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
)
from sage.matrix.constructor import matrix
from sage.matrix.special import diagonal_matrix
from sage.modules.free_module_element import vector
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)

if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.rings.ring import Ring
    from sage.structure.element import Matrix

    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import (
        FormModule,
    )
    from dzack_research.preamble.lexicon import OrderedSet

    # What the one entry point accepts: a ring naming the category, a
    # specimen's name, a root system as family and rank, or a Gram matrix.
    LatticeSpecification: TypeAlias = (
        str | int | Integer | Matrix | Category | Ring | list
    )

from dzack_research.preamble.categories.modules.pure.projective_modules import (
    ProjectiveModules,
)

# The axiom name this category is declared with.  It is registered here, where
# it is used: ``ProjectiveModules`` is an owned category, not an axiom bound
# onto Sage's ``Modules``.
if "Projective" not in all_axioms:
    all_axioms.add("Projective")


class Lattices(CategoryWithAxiom_over_base_ring):
    r"""Category of lattices over a base ring, and the named specimens.

    ``Lattices(R)`` is the category of lattices over ``R``; ``Lattices("E8")``
    is the specimen; ``Lattices.E8`` reads it as an attribute.  The specimens
    are real class attributes (see the assignment block at the foot of this
    module), so they carry their ``FormModule`` type and need no runtime patch.
    """

    _base_category_class_and_axiom = (SymmetricBilinearFormModules, "Projective")

    # Filled in below from the inline specimen assignments: the registry that
    # ``namespace`` and ``install`` read, rather than a scan for attributes that
    # look like lattices.
    if TYPE_CHECKING:
        _specimens: dict[str, "FormModule"]

        # Named specimens.  Declared here so the type checker resolves
        # ``Lattices.E8`` etc.; the runtime values are attached after the class
        # is bound (importing the constructor at the top would close a cycle).
        Zero: ClassVar["FormModule"]
        Z: ClassVar["FormModule"]
        Z_2: ClassVar["FormModule"]
        H: ClassVar["FormModule"]
        H_2: ClassVar["FormModule"]
        U: ClassVar["FormModule"]
        U_2: ClassVar["FormModule"]
        A1: ClassVar["FormModule"]
        A2: ClassVar["FormModule"]
        A3: ClassVar["FormModule"]
        A4: ClassVar["FormModule"]
        A5: ClassVar["FormModule"]
        A6: ClassVar["FormModule"]
        A7: ClassVar["FormModule"]
        A8: ClassVar["FormModule"]
        A9: ClassVar["FormModule"]
        A10: ClassVar["FormModule"]
        A11: ClassVar["FormModule"]
        A12: ClassVar["FormModule"]
        A13: ClassVar["FormModule"]
        A14: ClassVar["FormModule"]
        A15: ClassVar["FormModule"]
        A16: ClassVar["FormModule"]
        A17: ClassVar["FormModule"]
        A18: ClassVar["FormModule"]
        A19: ClassVar["FormModule"]
        A20: ClassVar["FormModule"]
        A21: ClassVar["FormModule"]
        D2: ClassVar["FormModule"]
        D3: ClassVar["FormModule"]
        D4: ClassVar["FormModule"]
        D5: ClassVar["FormModule"]
        D6: ClassVar["FormModule"]
        D7: ClassVar["FormModule"]
        D8: ClassVar["FormModule"]
        D9: ClassVar["FormModule"]
        D10: ClassVar["FormModule"]
        D11: ClassVar["FormModule"]
        D12: ClassVar["FormModule"]
        D13: ClassVar["FormModule"]
        D14: ClassVar["FormModule"]
        D15: ClassVar["FormModule"]
        D16: ClassVar["FormModule"]
        D17: ClassVar["FormModule"]
        D18: ClassVar["FormModule"]
        D19: ClassVar["FormModule"]
        D20: ClassVar["FormModule"]
        D21: ClassVar["FormModule"]
        D22: ClassVar["FormModule"]
        E6: ClassVar["FormModule"]
        E7: ClassVar["FormModule"]
        E8: ClassVar["FormModule"]
        E8_2: ClassVar["FormModule"]
        E10: ClassVar["FormModule"]
        E10_2: ClassVar["FormModule"]
        Sdp: ClassVar["FormModule"]
        SEn: ClassVar["FormModule"]
        Tco: ClassVar["FormModule"]
        Sco: ClassVar["FormModule"]
        LpNik: ClassVar["FormModule"]
        LmNik: ClassVar["FormModule"]
        LK3_2: ClassVar["FormModule"]
        LK3_4: ClassVar["FormModule"]
        LK3: ClassVar["FormModule"]
        TEn: ClassVar["FormModule"]
        TdP: ClassVar["FormModule"]
        L_20_2_0: ClassVar["FormModule"]
        BogachevKolpakovNonReflective: ClassVar["FormModule"]
        BogachevKolpakovWithoutRoots: ClassVar["FormModule"]
        Mukai: ClassVar["FormModule"]
        MukaiExtended: ClassVar["FormModule"]
        MukaiAbelian: ClassVar["FormModule"]
        MukaiAbelianExtended: ClassVar["FormModule"]

    @staticmethod
    def __classcall_private__(
        cls: type["Lattices"],
        *arguments: "LatticeSpecification",
        **keywords: "OrderedSet",
    ) -> "Lattices | FormModule":
        r"""The one entry point: dispatch on what was asked for.

        - a ring names the category of lattices over it;
        - a name names a specimen, or a root system by family and rank;
        - a Gram matrix builds the lattice carrying it.

        This is the constructor as well as the category, and it replaces
        Sage's ``IntegralLattice``.  Subcategories do not each grow an entry
        point of their own: what is specific to them is reached by delegating
        here, as the root systems are below.
        """
        from sage.categories.category import Category
        from sage.categories.rings import Rings
        from sage.structure.element import Matrix

        match arguments:
            case ((str() as family), (int() | Integer() as rank)) if family in ("A", "D", "E"):
                return cls.root_lattice(family, rank, **keywords)
            case ([str() as family, int() | Integer() as rank],) if family in ("A", "D", "E"):
                return cls.root_lattice(family, rank, **keywords)
            case (str() as name,) if name in cls._specimens and not keywords:
                return cls._specimens[name]
            case (str() as name,):
                return cls._lattice_with_names(name, **keywords)
            case (Matrix() as gram,):
                return cls._lattice_with_names(gram, **keywords)
            case (Category() as base_category,):
                # Sage builds an axiom category by calling it on the category
                # it refines; that path must reach the ordinary construction.
                return super(Lattices, cls).__classcall__(cls, base_category)
            case (base_ring,) if base_ring in Rings():
                return super(Lattices, cls).__classcall__(cls, base_ring)

        assert False, (
            f"Lattices takes a ring, a name, a root system, or a Gram matrix; "
            f"got {arguments!r}"
        )

    def extra_super_categories(self) -> list:
        r"""A lattice is a projective module.

        Named rather than left to the axiom machinery: ``Projective`` is
        declared on this preamble's own ``SymmetricBilinearFormModules``, and
        propagating it up the module chain would need it bound onto Sage's
        ``Modules`` as well, which is the monkey-patch this preamble does not
        make.  So the containment is stated here, where it is true.
        """
        return [ProjectiveModules(self.base_ring())]

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattices"

    @staticmethod
    def root_lattice(
        kind: str,
        rank: "int | Integer",
        names: "OrderedSet | None" = None,
    ) -> "FormModule":
        """Return the negative-definite root lattice of the given type.

        With ``names`` (the ``L.<generators> = ...`` sugar) a fresh lattice is
        constructed and named -- naming must never rename the shared specimen.
        """
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import (
            _apply_names,
            _integral_lattice_with_names,
        )

        assert kind in {"A", "D", "E"}, f"unknown root system family {kind!r}"
        if names is None:
            return getattr(Lattices, f"{kind}{rank}")
        return _apply_names(_integral_lattice_with_names(f"{kind}{rank}").twist(-1), names)

    @staticmethod
    def _lattice_with_names(
        described: "str | Matrix",
        names: "OrderedSet | None" = None,
        module_generating_set: "OrderedSet | None" = None,
    ) -> "FormModule":
        r"""Return the lattice a name or Gram matrix describes.

        The raw constructor the entry-point dispatch delegates to.  Imported
        here lazily so this module need not import ``integral_lattices`` at the
        top (that module imports ``Lattices`` and would close a cycle).
        """
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import (
            _integral_lattice_with_names,
        )

        return _integral_lattice_with_names(
            described, names=names, module_generating_set=module_generating_set
        )

    @staticmethod
    def IPQ(p: "Integer", q: "Integer") -> "FormModule":
        r"""Return the odd unimodular lattice $I_{p,q}$."""
        assert p >= 0 and q >= 0 and p + q > 0, f"empty signature ({p}, {q})"
        return Lattices._lattice_with_names(diagonal_matrix(SageZZ, [1] * p + [-1] * q))

    @staticmethod
    def IIPQ(p: "Integer", q: "Integer") -> "FormModule":
        r"""Return the even unimodular lattice $\mathrm{II}_{p,q}$ (indefinite).

        Milnor's classification, the hypothesis the catalogue's
        ``register_indecomposable`` header records: an indefinite even
        unimodular lattice of signature $(p,q)$ exists exactly when
        $p \equiv q \pmod 8$, and is then unique,
        $\mathrm{II}_{p,q} \cong U^{\min(p,q)} \oplus (\pm E_8)^{|p-q|/8}$ --
        with this catalogue's $E_8$ negative definite, the positive-definite
        summand is its $(-1)$-twist.

        Definite even unimodular lattices are deliberately outside this
        constructor: uniqueness fails from rank $16$ on ($E_8^2$ and
        $D_{16}^+$ share signature $(16,0)$, and rank $24$ has the $24$
        Niemeier classes), so a signature does not name one.  The source
        notebook's existence filter mis-parenthesized the congruence as
        ``p - q % 8 == 0``, which is $p - (q \bmod 8)$ and selects the wrong
        signatures.
        """
        assert p >= 1 and q >= 1, (
            f"II_({p},{q}) names the indefinite even unimodular lattice; a "
            "definite even unimodular genus holds several classes from rank "
            "16 on, so a signature does not name one"
        )
        assert (p - q) % 8 == 0, (
            f"an even unimodular lattice has signature divisible by 8; "
            f"({p}, {q}) has p - q = {p - q}"
        )
        hyperbolic_copies = Lattices.U ** min(p, q)
        if p == q:
            return hyperbolic_copies
        if p < q:
            return hyperbolic_copies + Lattices.E8 ** ((q - p) // 8)
        return hyperbolic_copies + Lattices.E8.twist(-1) ** ((p - q) // 8)

    @staticmethod
    def LK3_2d(degree: "Integer") -> "FormModule":
        r"""Return $\langle -2d\rangle \oplus U^2 \oplus E_8^2$."""
        assert degree >= 1, f"degree must be positive, got {degree}"
        return Lattices.Z.twist(-2 * degree) + Lattices.U**2 + Lattices.E8**2

    @staticmethod
    def rank_one_negative(scale: "Integer") -> "FormModule":
        r"""Return the rank-one lattice \(\langle-2\,\mathrm{scale}\rangle\)."""
        return Lattices.Z.twist(-2 * scale)

    @staticmethod
    def hyperkaehler_lattice(
        deformation_type: str, n: "Integer | int" = 2
    ) -> "FormModule":
        r"""Return the Beauville--Bogomolov--Fujiki lattice of a
        hyperkähler deformation type.

        $H^2(X,\mathbb Z)$ with the BBF form, per deformation type
        (reference construction: Hecke ``hyperkaehler_lattice``,
        ``QuadForm/Quad/ZLattices.jl``; its $-E_8$ and $-A_2$ summands are
        this catalogue's $E_8$ and $A_2$ under the negative-definite
        convention):

        - ``"K3"``: $K3^{[n]}$-type, $U^3\oplus E_8^2\oplus\langle 2-2n\rangle$;
        - ``"Kum"``: generalized Kummer, $U^3\oplus\langle -2-2n\rangle$;
        - ``"OG6"``: O'Grady dimension six, $U^3\oplus\langle-2\rangle^2$;
        - ``"OG10"``: O'Grady dimension ten, $U^3\oplus E_8^2\oplus A_2$.

        ``n`` names the deformation family for the two infinite series and
        is ignored by the O'Grady types; ``n = 1`` in the $K3^{[n]}$ series
        is the K3 lattice itself, reached as ``Lattices.LK3``.
        """
        assert deformation_type in {"K3", "Kum", "OG6", "OG10"}, (
            f"unknown hyperkähler deformation type {deformation_type!r}"
        )
        match deformation_type:
            case "K3":
                assert n >= 2, f"the K3^[n] series needs n >= 2, got {n}"
                return (
                    Lattices.U**3 + Lattices.E8**2 + Lattices.Z.twist(2 - 2 * n)
                )
            case "Kum":
                assert n >= 2, f"the Kummer series needs n >= 2, got {n}"
                return Lattices.U**3 + Lattices.Z.twist(-2 - 2 * n)
            case "OG6":
                return Lattices.U**3 + Lattices.Z.twist(-2) ** 2
            case _:
                return Lattices.U**3 + Lattices.E8**2 + Lattices.A2

    @staticmethod
    @cache
    def leech_lattice() -> "FormModule":
        r"""Return the Leech lattice $\Lambda_{24}$ (negative definite).

        Built through a Niemeier lattice, in the owned vocabulary, and
        cached (the enumeration below is paid once):

        1. $N(A_1^{24})$: the catalogue's $A_1^{24}$ glued along the
           extended binary Golay code -- each codeword names the
           discriminant class $\sum_i c_i\,e_i^\vee$, isotropic because the
           code is doubly even ($q = -\mathrm{wt}/2 \bmod 2\mathbb Z$
           vanishes for weights divisible by $8$).  The glue is even
           unimodular of rank $24$ with roots, so it is a Niemeier lattice.
        2. The holy construction (CS10 ch. 24; reference implementation
           Hecke ``leech_lattice(::ZZLat)``, ``QuadForm/Quad/ZLattices.jl``):
           with $h = 2$ the Coxeter number of $A_1$ and $\rho$ the sum of
           the components' Weyl vectors, the Leech lattice is spanned by
           the zero-coefficient-sum combinations of the extended root
           system's simple roots together with the vectors of the coset
           $\rho/h + N$ of square $2 + 2/h$ (their count squared is
           $|\!\det A_1^{24}| = 2^{24}$, asserted).  The coset enumeration
           is Fincke--Pohst, reached through PARI's ``qfcvp`` on the
           positive-regime Gram, and every returned vector is re-verified
           exactly.

        The result is asserted even, unimodular, of rank $24$, with no
        vectors of square $-2$ -- which characterizes $\Lambda_{24}$ among
        rank-$24$ even unimodular lattices (the Niemeier classification:
        every other class has roots).
        """
        from sage.coding.golay_code import GolayCode
        from sage.rings.finite_rings.finite_field_constructor import GF

        from dzack_research.preamble.utilities import zipsum

        ambient = Lattices.A1**24
        discriminant = ambient.discriminant_group()
        generators = discriminant.module_generators()
        glue_classes = [
            zipsum(
                (Integer(entry) for entry in codeword),
                generators,
                discriminant.zero(),
            )
            for codeword in GolayCode(GF(2), extended=True).generator_matrix().rows()
        ]
        niemeier = ambient.glue(*glue_classes)
        niemeier_gram = matrix(SageZZ, niemeier.gram_matrix())
        assert niemeier_gram.determinant() == 1 and niemeier.is_even(), (
            "the Golay glue of A1^24 must be even unimodular"
        )

        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        # The glue's framing labels are its basis rows in A1^24 coordinates,
        # where the positive-regime form is Q(x) = 2 sum x_i^2.
        basis = matrix(
            SageQQ, [list(label) for label in niemeier.module_generating_set()]
        )
        # rho = sum of the A1 Weyl vectors = (1/2, ..., 1/2); v = rho / h.
        coxeter_number = Integer(2)
        coset_shift = vector(SageQQ, [SageQQ(1) / 4] * 24)
        target = basis.solve_left(-coset_shift)
        coset_square = 2 + 2 / coxeter_number
        # The vectors of the coset v + N of square 2 + 2/h are the close
        # vectors of N about -v, displaced back by v; the owned enumeration
        # answers in this repo's negative regime, so the square is -(2+2/h).
        coset_rows = [
            vector(SageQQ, _coordinate_vector(element)) * basis + coset_shift
            for element, square in niemeier.close_vectors(
                list(target), -coset_square
            )
            if square == -coset_square
        ]
        assert len(coset_rows) ** 2 == 2**24, (
            "the holy construction's coset count squared is |det A1^24|"
        )

        simple_root_rows = [
            vector(SageQQ, [1 if j == i else 0 for j in range(24)])
            for i in range(24)
        ]
        extended_rows = (
            simple_root_rows
            + [-row for row in simple_root_rows]
            + coset_rows
        )
        first = extended_rows[0]
        differences = matrix(
            SageZZ,
            [[4 * entry for entry in row - first] for row in extended_rows[1:]],
        )
        hermite = differences.hermite_form(include_zero_rows=False)
        assert hermite.nrows() == 24, (
            "the zero-sum combinations of the extended system span rank 24"
        )
        leech_basis = matrix(SageQQ, hermite) / 4
        leech_gram = -2 * leech_basis * leech_basis.transpose()
        leech = Lattices._lattice_with_names(matrix(SageZZ, leech_gram))
        assert (
            matrix(SageZZ, leech_gram).determinant() == 1
            and leech.is_even()
            and not tuple(leech.vectors_of_square(-2))
        ), "even unimodular of rank 24 without roots is the Leech lattice"
        return leech

    @classmethod
    def namespace(cls) -> "dict[str, FormModule]":
        r"""Return the named lattice specimens as a ``{name: lattice}`` dict.

        Read off the registry rather than by scanning attributes for things
        that look like lattices.  The class also carries the axiom categories
        and the constructors, and ``obj in IntegralLattices(R)`` asks a class for
        its ``category()``.
        """
        return dict(cls._specimens)

    @classmethod
    def install(cls, scope: dict) -> None:
        r"""Bind catalogue specimens and named generators into *scope*.

        The owned rings are settled here too, and settled *last*.  Loading a
        further preamble script re-imports Sage's namespace into the same
        scope, which rebinds ``ZZ`` and ``QQ`` to the engine's rings behind the
        session's back -- so a notebook would find ``ZZ^3`` meaning one thing
        before the catalogue and another after it.
        """
        from dzack_research.preamble.catalogue import (
            Embeddings,
            Involutions,
            install_session_rings,
        )

        scope.update(cls._specimens)

        scope.update(
            I_dP=Involutions.I_dP,
            I_En=Involutions.I_En,
            I_Nik=Involutions.I_Nik,
        )

        # Shared short names: bind TdP after TEn so session ``e`` is TdP's.
        for lattice in (cls.TEn, cls.TdP, cls.LK3):
            lattice.inject_variables(scope, verbose=False)

        ed, fd, epd, fpd, w1, w2, w3, w4, w5, w6, w7, w8 = (
            cls.TEn.dual_lattice().module_generators()
        )
        scope.update(
            ed=ed, fd=fd, epd=epd, fpd=fpd,
            w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8,
        )

        (
            eb, fb, epb, fpb,
            w1, w2, w3, w4, w5, w6, w7, w8,
            w1t, w2t, w3t, w4t, w5t, w6t, w7t, w8t,
        ) = cls.TdP.dual_lattice().module_generators()
        scope.update(
            eb=eb, fb=fb, epb=epb, fpb=fpb,
            w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8,
            w1t=w1t, w2t=w2t, w3t=w3t, w4t=w4t,
            w5t=w5t, w6t=w6t, w7t=w7t, w8t=w8t,
        )

        install_session_rings(scope)


setattr(SymmetricBilinearFormModules, "Projective", Lattices)

# The named specimens (``Lattices.E8``, ``Lattices.U``, ...) are attached as
# real class attributes from ``catalogue.sage``.  They are declared as
# ``ClassVar`` above so the type checker resolves them; their values are built
# there because the construction primitive lives in ``integral_lattices.sage``,
# which imports this class -- importing it here would close that cycle.  One
# ``Lattices``, one name: the specimens, the category, and the constructors all
# answer under it.

