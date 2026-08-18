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

from typing import TYPE_CHECKING, ClassVar, TypeAlias

from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
)
from sage.matrix.special import diagonal_matrix
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ

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
    def LK3_2d(degree: "Integer") -> "FormModule":
        r"""Return $\langle -2d\rangle \oplus U^2 \oplus E_8^2$."""
        assert degree >= 1, f"degree must be positive, got {degree}"
        return Lattices.Z.twist(-2 * degree) + Lattices.U**2 + Lattices.E8**2

    @staticmethod
    def rank_one_negative(scale: "Integer") -> "FormModule":
        r"""Return the rank-one lattice \(\langle-2\,\mathrm{scale}\rangle\)."""
        return Lattices.Z.twist(-2 * scale)

    @classmethod
    def namespace(cls) -> "dict[str, FormModule]":
        r"""Return the named lattice specimens as a ``{name: lattice}`` dict.

        Read off the registry rather than by scanning attributes for things
        that look like lattices.  The class also carries the axiom categories
        and the constructors, and ``obj in IntegralLattices()`` asks a class for
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

