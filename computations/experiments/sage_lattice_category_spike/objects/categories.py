r"""Sage category classes for the owned synthetic lattice spike.

Ratified organization (M-RATIFY): two SEPARATE categories, no shared root.

- ``Lattices(R)`` -- based free ``R``-modules with a symmetric ``K``-valued form,
  on ``Modules(R).WithBasis().FiniteDimensional()``. Possibly-degenerate base;
  ``Nondegenerate`` is an axiom attached by the constructor iff ``det(G) != 0``.
- ``DiscriminantForms(R)`` -- finite abelian groups (NOT "modules over ZZ")
  carrying a finite bilinear/quadratic form valued in a quotient module.

``K`` (the form value ring) is per-object via ``value_module()``; the categories
are parameterized by the module base ring ``R`` only. Shared form predicates live
in Python mixins keyed on abstract, fail-loud ``value_module()``/``gram_matrix``
hooks -- there is deliberately no mixin-level default for those hooks.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Literal, cast

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring,
    all_axioms,
    axiom,
)
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.enumerated_sets import EnumeratedSets
from sage.categories.functor import ForgetfulFunctor
from sage.categories.homset import Hom as SageHom
from sage.categories.homset import Homset
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from ..lexicon import (
    BaseRing,
    BilinearDiscriminantForm,
    CartanType,
    DefiniteLattice,
    DiscriminantForm,
    ExactScalar,
    FiniteAbelianGroup,
    Genus,
    HyperbolicLattice,
    IndefiniteLattice,
    IntegralNondegenerateLattice,
    Lattice,
    LatticeElement,
    LatticeHomset,
    LatticeMorphism,
    LatticeName,
    LatticeSimilarity,
    NondegenerateLattice,
    PositiveDefiniteLattice,
    QuadraticDiscriminantForm,
    RawGramMatrix,
    RawMorphismMatrix,
    RootGeneratedLattice,
    SageCategory,
    SageFunctor,
    SourcedDiscriminantForm,
)

if TYPE_CHECKING:
    # Sage's abstract_method ships untyped; for type-checking use abc.abstractmethod
    # (typed, and permits the empty abstract bodies below). Runtime uses Sage's.
    from abc import abstractmethod as abstract_method

    from ..forms.discriminant_forms import PontryaginDualIdentification
else:
    from sage.misc.abstract_method import abstract_method

_FORM_AXIOMS = (
    "Nondegenerate",
    "Integral",
    "Even",
    "Unimodular",
    "Definite",
    "PositiveDefinite",
    "NegativeDefinite",
    "Indefinite",
    "Hyperbolic",
    "RootGenerated",
    "Bilinear",
    "Quadratic",
    "WithSourceLattice",
)

for _axiom_name in _FORM_AXIOMS:
    if _axiom_name not in all_axioms:
        all_axioms.add(_axiom_name)


def _own_methods(carrier: type) -> type:
    r"""Sage's category framework injects only a ParentMethods class's OWN
    attributes and warns when the class has a superclass (inherited names are
    never copied). The domain-algebra classes subclass their base class for the
    static type hierarchy, so hand Sage a derived view holding exactly that
    class's own delta — projected mechanically, never written by hand."""
    delta = {name: value for name, value in vars(carrier).items() if not name.startswith("__")}
    delta["__doc__"] = carrier.__doc__
    return type("ParentMethods", (), delta)


class Lattices(Category_over_base_ring):
    r"""Based free ``R``-modules with a symmetric ``K``-valued form.

    Base is possibly-degenerate; ``Nondegenerate`` is an axiom subcategory.
    """

    def _repr_object_names(self) -> str:
        return f"synthetic lattices over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        # V0a-ratified leaner tree: no WithBasis — a based lattice owns its basis
        # vocabulary; the CombinatorialFreeModule element idiom must not reach
        # lattice elements. Every name the leaner tree stops inheriting is owned
        # on the concrete classes (basis/gens/gen/rank/random_element/...).
        return [Modules(self.base_ring()).FiniteDimensional()]

    def additional_structure(self) -> Lattices:
        return self

    if TYPE_CHECKING:
        # Typed axiom navigation: applying an axiom to a subcategory of
        # Lattices yields a subcategory of Lattices — the axiom tree is closed
        # under its own axioms, so every chain
        # ``Lattices(R).Nondegenerate().Integral()...`` stays in this type. At
        # runtime Sage synthesizes these methods from SubcategoryMethods; the
        # class-attribute wiring at the bottom of this module is Sage's
        # class-resolution shortcut and is runtime-only.
        def Nondegenerate(self) -> Lattices: ...
        def Integral(self) -> Lattices: ...
        def Even(self) -> Lattices: ...
        def Unimodular(self) -> Lattices: ...
        def Definite(self) -> Lattices: ...
        def PositiveDefinite(self) -> Lattices: ...
        def NegativeDefinite(self) -> Lattices: ...
        def Indefinite(self) -> Lattices: ...
        def Hyperbolic(self) -> Lattices: ...
        def RootGenerated(self) -> Lattices: ...

    class SubcategoryMethods:
        Nondegenerate = axiom("Nondegenerate")
        Integral = axiom("Integral")
        Even = axiom("Even")
        Unimodular = axiom("Unimodular")
        Definite = axiom("Definite")
        PositiveDefinite = axiom("PositiveDefinite")
        NegativeDefinite = axiom("NegativeDefinite")
        Indefinite = axiom("Indefinite")
        # signature (1, rank-1) refinement of indefinite nondegenerate lattices
        Hyperbolic = axiom("Hyperbolic")
        # even lattice generated by its roots {v : q(v) = +-2}; attached only by
        # construction provenance (section 1.3), never detected from the Gram
        RootGenerated = axiom("RootGenerated")

    ParentMethods = Lattice

    ElementMethods = LatticeElement

    def from_gram_matrix(
        self,
        gram_matrix: RawGramMatrix | LatticeName,
        label: str = "L",
        cartan_type: CartanType | Literal["composite"] | None = None,
        names: Sequence[str] | str | None = None,
    ) -> Lattice:
        r"""Section 1.4: the functor from square symmetric matrices over the
        base ring into this category — the ONLY public entry into the language.

        Asserts its domain contract (ADDD: a violation is a caller-contract
        bug) and routes the object into its mathematical subcategory; provenance
        axioms (RootGenerated) ride the ``cartan_type`` certificate, which is
        construction data — resolved here from a lattice NAME ("E8", ("A", 2)),
        never detected from a raw Gram matrix. Subcategory membership is
        output, not input: you construct E8 as a lattice and GET a
        root-generated lattice.
        """
        from ..algebra.arithmetic import as_square_qq_matrix, is_named_gram_data, named_cartan_type
        from .parents import construct_synthetic_lattice

        base_ring = self.base_ring()
        assert base_ring in (ZZ, QQ), f"lattice base ring must be ZZ or QQ; found={base_ring}; enter through Lattices(ZZ) or Lattices(QQ)"
        if cartan_type is None and is_named_gram_data(gram_matrix):
            cartan_type = named_cartan_type(gram_matrix)
        gram = as_square_qq_matrix(gram_matrix)
        return cast(
            "Lattice",
            construct_synthetic_lattice(gram, base_ring, label, cartan_type=cartan_type, names=names),
        )

    @staticmethod
    def _lattice_root(category: SageCategory) -> Lattices | None:
        r"""Return the lattice root that owns a lattice subcategory, if any."""
        for base_ring in (ZZ, QQ):
            root = Lattices(base_ring)
            if category.is_subcategory(root):
                return root
        return None

    def base_change(self, target_base_ring: BaseRing) -> SageFunctor:
        r"""Return the canonical scalar-extension functor from this root."""
        assert target_base_ring in (ZZ, QQ), f"lattice base ring must be ZZ or QQ; found={target_base_ring}"
        from .functors import LatticeBaseChangeFunctor

        return LatticeBaseChangeFunctor(self, Lattices(target_base_ring))

    def canonical_functor(self, target: SageCategory) -> SageFunctor:
        r"""Return the canonical functor from this lattice root to ``target``."""
        lattice_target = self._lattice_root(target)
        if lattice_target is not None:
            return self.base_change(lattice_target.base_ring())
        assert self.is_subcategory(target), f"no canonical functor from {self} to {target}"
        return ForgetfulFunctor(self, target)

    def from_base_change(self, source: Lattice) -> Lattice:
        r"""Construct a scalar extension through this target category root."""
        source_root = Lattices(source.base_ring())
        assert source in source_root, f"base-change source must belong to {source_root}; found={source.category()}"
        assert self.base_ring().coerce_map_from(source.base_ring()) is not None, f"base change requires a canonical map {source.base_ring()} -> {self.base_ring()}"
        if source.base_ring() == self.base_ring():
            return source
        return self.from_gram_matrix(source.gram_matrix(), label=f"base_change_to_{self.base_ring()}")

    def _transport_to(self, lattice: Lattice, category: SageCategory) -> Lattice:
        r"""Apply the canonical functor that realizes ``lattice`` in ``category``."""
        source_root = Lattices(lattice.base_ring())
        lattice_target = self._lattice_root(category)
        functor = source_root.base_change(lattice_target.base_ring()) if lattice_target is not None else source_root.canonical_functor(category)
        transported = cast(Lattice, functor(lattice))
        assert transported in category, f"canonical transport from {lattice.category()} does not land in {category}; result={transported.category()}"
        return transported

    def _default_hom_resolution(self, domain: Lattice, codomain: Lattice) -> tuple[Lattice, Lattice, SageCategory]:
        r"""Resolve a default Hom request, preferring canonical base change to
        the native meet of different base categories."""
        if domain.base_ring() == codomain.base_ring():
            return domain, codomain, domain.category()._meet_(codomain.category())
        if codomain.base_ring().coerce_map_from(domain.base_ring()) is not None:
            transported_domain = cast(Lattice, Lattices(domain.base_ring()).base_change(codomain.base_ring())(domain))
            return transported_domain, codomain, transported_domain.category()._meet_(codomain.category())
        if domain.base_ring().coerce_map_from(codomain.base_ring()) is not None:
            transported_codomain = cast(Lattice, Lattices(codomain.base_ring()).base_change(domain.base_ring())(codomain))
            return domain, transported_codomain, domain.category()._meet_(transported_codomain.category())
        return domain, codomain, domain.category()._meet_(codomain.category())

    def Hom(
        self,
        domain: Lattice,
        codomain: Lattice,
        category: SageCategory | None = None,
    ) -> LatticeHomset | Homset:
        r"""Construct a Hom through this category root.

        An explicit category means transport both arguments through their
        canonical functors before invoking Sage's standard Hom factory. Without
        an explicit category, scalar extension takes precedence over the native
        meet when it provides a common lattice category.
        """
        assert domain.base_ring() == self.base_ring(), f"enter through Lattices({domain.base_ring()}) for a Hom whose source is {domain}"
        if category is None:
            resolved_domain, resolved_codomain, resolved_category = self._default_hom_resolution(domain, codomain)
        else:
            assert isinstance(category, Category), f"Hom category must be a Sage category; found={type(category)}"
            resolved_domain = self._transport_to(domain, category)
            resolved_codomain = self._transport_to(codomain, category)
            resolved_category = category
        return cast(LatticeHomset | Homset, SageHom(resolved_domain, resolved_codomain, category=resolved_category))

    def homset_from_sage(self, domain: Lattice, codomain: Lattice, category: SageCategory | None) -> LatticeHomset | Homset:
        r"""The Sage Hom hook after Sage has selected and checked a category."""
        assert category is not None, "Sage Hom must provide its resolved category"
        lattice_root = self._lattice_root(category)
        if lattice_root is not None:
            assert domain.base_ring() == codomain.base_ring() == lattice_root.base_ring(), (
                f"a lattice homset needs one base ring; domain={domain.base_ring()}, codomain={codomain.base_ring()}, category={category}"
            )
            assert domain in category and codomain in category, f"lattice homset arguments must belong to {category}"
            return lattice_root._lattice_homset(domain, codomain, category)
        assert domain in category and codomain in category, f"generic Hom arguments must belong to {category}"
        return Homset(domain, codomain, category=category)

    def _lattice_homset(self, domain: Lattice, codomain: Lattice, category: SageCategory) -> LatticeHomset:
        r"""The single private binding from the lattice category to its homset
        implementation."""
        return Lattices.Homsets.implementation(domain, codomain, category)

    def morphism(
        self,
        domain: Lattice,
        matrix_data: RawMorphismMatrix,
        codomain: Lattice | None = None,
    ) -> LatticeMorphism:
        r"""Construct a form-preserving morphism through its category homset."""
        codomain = domain if codomain is None else codomain
        assert domain.base_ring() == codomain.base_ring() == self.base_ring(), (
            f"morphism construction needs one lattice category; domain={domain.base_ring()}, codomain={codomain.base_ring()}"
        )
        return cast(LatticeMorphism, self.Hom(domain, codomain)(matrix_data))

    def similarity(
        self,
        domain: Lattice,
        matrix_data: RawMorphismMatrix,
        codomain: Lattice,
        scalar: ExactScalar,
    ) -> LatticeSimilarity:
        r"""The private binding for lattice similarities."""
        assert domain.base_ring() == codomain.base_ring() == self.base_ring(), (
            f"similarity construction needs one lattice category; domain={domain.base_ring()}, codomain={codomain.base_ring()}"
        )
        from ..morphisms.homsets import LatticeSimilarity as Implementation

        return Implementation(domain, codomain, matrix_data, scalar)

    class MorphismMethods:
        pass

    class Homsets(HomsetsCategory):
        r"""Homsets of form-preserving lattice morphisms."""

        @staticmethod
        def implementation(domain: Lattice, codomain: Lattice, category: SageCategory) -> LatticeHomset:
            r"""The lattice category's registered homset implementation."""
            from ..morphisms.homsets import LatticeHomset as Implementation

            return Implementation(domain, codomain, category=category)

        def extra_super_categories(self) -> list[Category]:
            return [Sets()]

        class ParentMethods:
            # No from_matrix contract: morphism construction is the element
            # constructor / the lattices' public named constructors (#100 T4).
            pass

        class ElementMethods:
            @abstract_method
            def kernel(self) -> Lattice:
                r"""Return the kernel lattice of this morphism."""

            @abstract_method
            def image(self) -> Lattice:
                r"""Return the image lattice of this morphism."""


class DiscriminantForms(Category_over_base_ring):
    r"""Finite abelian groups with a discriminant bilinear/quadratic form.

    Typed as a finite abelian group (fixing Sage's "modules over ZZ" mis-typing);
    the form is extra structure layered on the group.
    """

    def _repr_object_names(self) -> str:
        return f"synthetic discriminant forms over {self.base_ring()}"

    def from_form_data(
        self,
        gram_matrix: RawGramMatrix,
        quadratic_modulus: int = 2,
        invariants: Sequence[int] | None = None,
    ) -> DiscriminantForm:
        r"""Section 1.4: the finite-side functor — the ONLY constructor
        from form data (a quadratic generator Gram, its value modulus, and
        optionally an explicit group presentation) into this category. The
        lattice-side functor ``discriminant_group`` lands in its image, and
        the Sage-compatible ``TorsionQuadraticForm`` factory routes here."""
        from ..forms.discriminant_forms import SyntheticQuadraticDiscriminantForm

        return SyntheticQuadraticDiscriminantForm(gram_matrix, quadratic_modulus=quadratic_modulus, invariants=invariants)

    def super_categories(self) -> list[Category]:
        return [CommutativeAdditiveGroups().Finite()]

    def additional_structure(self) -> DiscriminantForms:
        return self

    if TYPE_CHECKING:
        # Typed axiom navigation; see the Lattices declaration above.
        def Bilinear(self) -> DiscriminantForms: ...
        def Quadratic(self) -> DiscriminantForms: ...
        def Nondegenerate(self) -> DiscriminantForms: ...
        def Even(self) -> DiscriminantForms: ...
        def WithSourceLattice(self) -> DiscriminantForms: ...

    class SubcategoryMethods:
        Bilinear = axiom("Bilinear")
        Quadratic = axiom("Quadratic")
        Nondegenerate = axiom("Nondegenerate")
        Even = axiom("Even")
        WithSourceLattice = axiom("WithSourceLattice")

    # The domain-algebra class IS this base category's ParentMethods (direct
    # assignment; the finite-quotient parent subsumes the former four abstract
    # stubs). Concrete parents inherit the class and shadow its declared
    # methods with real implementations.
    ParentMethods = FiniteAbelianGroup

    class MorphismMethods:
        pass


class Genera(Category_over_base_ring):
    r"""Genera of nondegenerate integral lattices: an object is the finite set of
    isometry classes sharing a signature and discriminant quadratic form
    (Nikulin 1.10.1). Its cardinality is the class number.

    Parity is the ``Even`` axiom, acquired as OUTPUT from the discriminant form
    (a quadratic form of value modulus 2 is even), never a construction input.
    """

    def _repr_object_names(self) -> str:
        return f"synthetic genera over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        # A genus IS the finite set of its isometry classes: the finite-set API
        # (cardinality, iteration) is INHERITED from this super-category, never
        # re-declared on the genus contract or a concrete parent.
        return [EnumeratedSets().Finite()]

    def additional_structure(self) -> Genera:
        return self

    if TYPE_CHECKING:
        # Typed axiom navigation; see the Lattices declaration above.
        def Even(self) -> Genera: ...

    class SubcategoryMethods:
        Even = axiom("Even")

    # The genus noun IS this base category's ParentMethods; the concrete
    # SyntheticGenus parent inherits it and shadows the abstract methods.
    ParentMethods = Genus


class NondegenerateLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Nondegenerate")

    ParentMethods = _own_methods(NondegenerateLattice)


class IntegralLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Integral")


class IntegralNondegenerateLattices(CategoryWithAxiom_over_base_ring):
    # Section 1.2: home of the discriminant/genus vocabulary (section 2.4). That
    # vocabulary is installed here in T1c; the class is declared now so the tree
    # and its routing exist.
    _base_category_class_and_axiom = (IntegralLattices, "Nondegenerate")

    ParentMethods = _own_methods(IntegralNondegenerateLattice)


class EvenLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Even")

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (Lattices(self.base_ring()).Integral(),)


class RootGeneratedLattices(CategoryWithAxiom_over_base_ring):
    # Section 1.2: even integral lattice generated by its roots {v : q(v) = +-2}.
    _base_category_class_and_axiom = (EvenLattices, "RootGenerated")

    ParentMethods = _own_methods(RootGeneratedLattice)


class UnimodularLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Unimodular")

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (Lattices(self.base_ring()).Integral(),)


class DefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Definite")

    ParentMethods = _own_methods(DefiniteLattice)


class PositiveDefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "PositiveDefinite")

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (Lattices(self.base_ring()).Definite(),)

    ParentMethods = _own_methods(PositiveDefiniteLattice)


class NegativeDefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "NegativeDefinite")

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (Lattices(self.base_ring()).Definite(),)


class IndefiniteLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Lattices, "Indefinite")

    ParentMethods = _own_methods(IndefiniteLattice)


class HyperbolicLattices(CategoryWithAxiom_over_base_ring):
    # Section 1.2: signature_pair == (1, rank-1), rank >= 2 (Nikulin convention:
    # one positive square). Refines indefinite nondegenerate lattices.
    _base_category_class_and_axiom = (IndefiniteLattices, "Hyperbolic")

    ParentMethods = _own_methods(HyperbolicLattice)

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (Lattices(self.base_ring()).Indefinite().Nondegenerate(),)


class BilinearDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Bilinear")

    ParentMethods = _own_methods(BilinearDiscriminantForm)


class QuadraticDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Quadratic")

    ParentMethods = _own_methods(QuadraticDiscriminantForm)

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (DiscriminantForms(self.base_ring()).Bilinear(),)


class NondegenerateDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Nondegenerate")

    class ParentMethods:
        def pontryagin_dual(self) -> PontryaginDualIdentification:
            r"""The canonical identification ``A ~ Hom(A, QQ/ZZ)`` as a typed
            object: index by an element to get its character. Placed on the
            Nondegenerate subcategory (spec section 4) — the identification along
            ``b`` exists exactly there, so definedness is placement, not a
            runtime guard."""
            from ..forms.discriminant_forms import PontryaginDualIdentification

            return PontryaginDualIdentification(self)


class EvenDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "Even")

    def extra_super_categories(self) -> tuple[Category_over_base_ring, ...]:
        return (DiscriminantForms(self.base_ring()).Quadratic(),)


class WithSourceLatticeDiscriminantForms(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantForms, "WithSourceLattice")

    ParentMethods = _own_methods(SourcedDiscriminantForm)


class EvenGenera(CategoryWithAxiom_over_base_ring):
    # Genera of even lattices: parity acquired as output (Phase B adds the odd
    # branch; until then a non-even genus fails loud at construction).
    _base_category_class_and_axiom = (Genera, "Even")


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut: the axiom category class must be
    # reachable as `<BaseCategory>.<Axiom>` for `_base_category_class_and_axiom`
    # to resolve. Runtime-only wiring; the typed surface of these names is the
    # axiom-navigation method declarations on the category classes above.
    Lattices.Nondegenerate = NondegenerateLattices
    Lattices.Integral = IntegralLattices
    Lattices.Even = EvenLattices
    Lattices.Unimodular = UnimodularLattices
    Lattices.Definite = DefiniteLattices
    Lattices.PositiveDefinite = PositiveDefiniteLattices
    Lattices.NegativeDefinite = NegativeDefiniteLattices
    Lattices.Indefinite = IndefiniteLattices

    IntegralLattices.Nondegenerate = IntegralNondegenerateLattices
    EvenLattices.RootGenerated = RootGeneratedLattices
    IndefiniteLattices.Hyperbolic = HyperbolicLattices

    DiscriminantForms.Bilinear = BilinearDiscriminantForms
    DiscriminantForms.Quadratic = QuadraticDiscriminantForms
    DiscriminantForms.Nondegenerate = NondegenerateDiscriminantForms
    DiscriminantForms.Even = EvenDiscriminantForms
    DiscriminantForms.WithSourceLattice = WithSourceLatticeDiscriminantForms

    Genera.Even = EvenGenera
