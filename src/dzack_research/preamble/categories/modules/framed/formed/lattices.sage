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
"""

from typing import TYPE_CHECKING, TypeAlias

from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
)

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)

if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.rings.integer import Integer
    from sage.rings.ring import Ring
    from sage.structure.element import Matrix

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
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
    r"""Category of lattices over a base ring, and the named specimens."""

    _base_category_class_and_axiom = (SymmetricBilinearFormModules, "Projective")

    _specimens: dict = {}

    if TYPE_CHECKING:
        # Installed onto this class by ``catalogue.sage``, which owns the
        # named specimens and the raw constructor the dispatch delegates to.
        @staticmethod
        def root_lattice(
            family: str,
            rank: "int | Integer",
            names: "OrderedSet | None" = ...,
        ) -> "FormModule": ...

        @staticmethod
        def _lattice_with_names(
            described: "str | Matrix",
            names: "OrderedSet | None" = ...,
            module_generating_set: "OrderedSet | None" = ...,
        ) -> "FormModule": ...

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
        from sage.rings.integer import Integer
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


setattr(SymmetricBilinearFormModules, "Projective", Lattices)
