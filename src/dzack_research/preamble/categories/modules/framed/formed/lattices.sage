r"""``Lattices(R)``: projective modules carrying an $R$-valued bilinear form.

This category *is* ``SymmetricBilinearFormModules(R).Projective()``. It is
declared rather than composed: Sage models "this category, plus this axiom" as
the axiom's category class bound onto the category it refines, so a class that
names the pair and is bound with ``setattr`` is that join, under whatever name
suits it.  ``FramedModules`` is ``Modules(R).Framed()`` by the same device.

A lattice is not a module with a bilinear form.  That is
``SymmetricBilinearFormModules(R)``, and it holds anything with a pairing.
What makes a lattice is that the module is **projective**, which is why the
axiom sits on ``Modules`` and this category is its join with the form.

Nothing here is finitely generated, integral, or nondegenerate.  Those are
three further axioms, and declining to impose them is what lets this category
hold $\ZZ^{\infty}$ with the standard form, or $SL_2(\ZZ)$ inside
$SL_2(\RR)$ with $b(x,y)=\operatorname{tr}(xy)$.
"""

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)

# Imported for the registration and binding of the ``Projective`` axiom, which
# is what makes the declaration below resolve.
from dzack_research.preamble.categories.modules.pure.projective_modules import (  # noqa: F401
    ProjectiveModules,
)


class Lattices(CategoryWithAxiom_over_base_ring):
    r"""Category of lattices over a base ring, and the named specimens."""

    _base_category_class_and_axiom = (SymmetricBilinearFormModules, "Projective")

    _specimens: dict = {}

    @staticmethod
    def __classcall_private__(cls, *arguments, **keywords):
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

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattices"


setattr(SymmetricBilinearFormModules, "Projective", Lattices)
