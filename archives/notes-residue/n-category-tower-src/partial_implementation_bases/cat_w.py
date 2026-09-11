# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/cat_w.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# """
# CatW: Abstract base class for all ω-categories.

# Per implementation_spec.md §Cat_w (lines 232-380).

# Hierarchy:
# - Cat_{-2} = ∅ (EmptyCategory)
# - Cat_{-1} = * (TerminalCategory)
# - Cat_0 = Discrete Categories ≅ Sets
# - Cat_1 = Categories
# - Cat_2 = Cat, Fun, Hom_C
# - Cat_w = Interface for all categories (this ABC)

# Amb() chain: x → X → Set → Cat → Cat_w → *

# Operators are inherited from CategoryOperatorsMixin.
# """

# from __future__ import annotations

# import random
# from abc import ABC
# from collections.abc import Iterator, Sequence
# from dataclasses import dataclass
# from functools import reduce
# from typing import Any, Never, assert_never, cast, final, overload, override, Self

# import deal

# from src._types import BoolProof, CategoryABCs, CategoryBases, CategoryTypeChecks


# @dataclass
# class _CatW_Base(CategoryABCs.Nontrivial_TwoCategory, ABC):
#     """
#     Base class for all ω-categories, including Cat.
#     Inherit from this base, not the ABC, since this implements many extra methods.

#     The ambient category (self.amb) tracks which category this object lives in.
#     Level relationships are validated at construction time via __post_init__.

#     Examples:
#         X = Cat => amb = Cat_ω (or *)
#         X = Set => amb = Cat
#         X = a set => amb = Set
#         x = an element of a set => amb = X (the set)
#     """

#     _cell_container: CategoryBases.CellContainer

#     def __init__(self) -> None:
#         self._cell_container = CategoryBases.CellContainer() # type: ignore #TODO

#     @override
#     def cells(self) -> CategoryBases.CellContainer:
#         return self._cell_container

#     @override
#     @final
#     def is_object_C(self, x: Any) -> bool:
#         """Check if x is an object (instance of object_class) in this category."""
#         return isinstance(x, type(self).ZeroCell_category_class())


#     @override
#     @final
#     def is_morphism_C(self, x: Any) -> bool:
#         """Check if x is a morphism (instance of morphism_class) in this category."""
#         return isinstance(x, type(self).morphism_category_class())

#     @override
#     @final
#     def is_product_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a product category."""
#         return (
#             isinstance(x, type(self).product_category_class())
#             and self.is_object_C(x)
#             and self.is_slice_object_C(x)
#         )

#     @override
#     @final
#     def is_coproduct_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a coproduct category."""
#         assert self.is_object_C(x), "x must be an object in C"
#         return isinstance(x, type(self).coproduct_category_class()) and self.is_coslice_object_C(x)


#     @override
#     @final
#     def is_pullback_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a pullback category."""
#         assert self.is_object_C(x), "x must be an object in C"
#         return isinstance(x, type(self).pullback_category_class()) and self.is_slice_object_C(x)


#     @override
#     @final
#     def is_pushout_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a pushout category."""
#         assert self.is_object_C(x), "x must be an object in C"
#         return isinstance(x, type(self).pushout_category_class()) and self.is_coslice_object_C(x)


#     @override
#     @final
#     def is_direct_sum_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a direct sum category."""
#         return (
#             isinstance(x, type(self).direct_sum_category_class())
#             and self.is_coslice_object_C(x)
#             and self.is_slice_object_C(x)
#         )


#     @override
#     @final
#     def is_tensor_product_C(self, x: CategoryABCs.ZeroCell) -> bool:
#         """Check if x is a tensor product category."""
#         return isinstance(x, type(self).tensor_product_category_class())


#     # @override
#     # @final
#     # def __get_slice_structures_C__(
#     #     self, x: CategoryABCs.ZeroCell
#     # ) -> Sequence[CategoryABCs.Slice]:
#     #     """
#     #     Given x, find slice structures (y, f: y -> x) on x in C.
#     #     """
#     #     matches = [
#     #         s for s in x.structures() if isinstance(s, type(self).slice_object_class())
#     #         if s.base_object().is_equivalent_to(x).is_true()
#     #     ]
#     #     return matches


#     # @override
#     # @final
#     # def __get_coslice_structures_C__(
#     #     self, x: CategoryABCs.ZeroCell,
#     # ) -> Sequence[CategoryABCs.Coslice]:
#     #     """
#     #     Given x, find coslice structures (y, f: x -> y) on x in C.
#     #     """
#     #     matches = [
#     #         s for s in x.structures() if isinstance(s, type(self).coslice_object_class())
#     #         if s.apex_object().is_equivalent_to(x).is_true()
#     #     ]
#     #     return matches


#     @override
#     @final
#     def identity_endomorphism_on_self(self) -> CategoryABCs.Endomorphism:
#         """Return id_C in End_A(C) where C is this category and A = self.amb()."""
#         return self.amb().end_C(self.as_cell()).identity_endomorphism_on_self()


#     @override
#     @final
#     def is_bicomplete(self) -> BoolProof:
#         """Complete and cocomplete."""
#         return self.is_complete() and self.is_cocomplete()

#     @override
#     @final
#     def hom(self, D: CategoryABCs.Cell) -> CategoryABCs.HomC_xy:
#         """
#         If this category is C and C is an object of A,
#         self.hom(D) := Hom_A(C, D).
#         """
#         HomC_xy = self.amb().hom_C(self.as_cell(), D)
#         assert CategoryTypeChecks.is_HomC_xy_category(HomC_xy)
#         return HomC_xy


#     @override
#     @final
#     def end(self) -> CategoryABCs.EndC_x | CategoryABCs.EndC:
#         """
#         self.end() := End_C(self)
#         """
#         return self.amb().end_C(self.as_cell())


#     @override
#     @final
#     def aut(self) -> CategoryABCs.AutC_x | CategoryABCs.AutC:
#         """
#         self.aut() := Aut_C(self)
#         """
#         return self.amb().aut_C(self.as_cell())


#     @override
#     @final
#     @deal.ensure(
#         lambda self, result: self.is_object(result)
#         and result.is_terminal_object()
#         and result.is_initial_object()
#         and result.is_zero_object(),
#         message="Result must be a terminal and initial object in C",
#     )
#     def zero_object_C(self) -> CategoryABCs.ZeroCell:
#         """0 in C if C is pointed."""
#         if not self.is_pointed().is_true():
#             raise ValueError("Category is not provably pointed, so no zero object exists.")
#         return self.initial_object_C()

#     @override
#     @final
#     def product(self, other: Self) -> CategoryABCs.ZeroCell:
#         return self.amb().product_C([self.as_zero_cell(), other.as_zero_cell()])


#     @override
#     @final
#     def coproduct(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         return self.amb().coproduct_C([self.as_zero_cell(), other.as_zero_cell()])


#     @override
#     @final
#     def underlying_set(self) -> CategoryABCs.SetObject:
#         """The set underlying this category, i.e. U(C)."""
#         FX = self.amb().forgetful_functor_to_set().apply_on_object(self)
#         assert CategoryTypeChecks.is_set_object(FX)
#         return FX

#     # Constructing n-cells/morphisms for n >= 1
#     @final
#     @override
#     def object_C_from(self, **cell_data: Any) -> CategoryABCs.ZeroCell:
#         return self.zero_cell_from(**cell_data)

#     @final
#     @override
#     def morphism_C_from(self, **cell_data: Any) -> CategoryABCs.OneMorphism:
#         return self.one_cell_from(**cell_data)

#     # @final
#     # @override
#     # def category_of_elements(self) -> CategoryABCs.Nontrivial_TwoCategory:
#     #     """
#     #     C^{-1}: the set underlying the category of elements of the forgetful functor U: C -> Set.
#     #     Objects: ∐_{X in ob(C)} ∐_{x_ij in X} {x_ij}
#     #     Morphisms: x_1->x_2 iff there exists a morphism f: X_1->X_2 in C such that f(x_1) = x_2
#     #     Construction:
#     #         s = {x_i -> f(x_i) | x_i in X, f: X->Y in C}
#     #     Just return a 1-category for now.
#     #     TODO: figure out how to incorporate higher cells from C.
#     #     """
#     #     one_cells = []
#     #     for f in self.cells().get_n_cells(1):
#     #         assert CategoryTypeChecks.is_morphism(f)
#     #         X = f.source()
#     #         Y = f.target()
#     #         one_cells.append(self.morphism_C_from(
#     #             domain=X,
#     #             codomain=Y,
#     #             data=f
#     #         ))

#     #     # TODO: Replace with DigraphCategory
#     #     return Categories.FromOneCells(one_cells)

    

#     @final
#     @override
#     def objects(self) -> Sequence[CategoryABCs.ZeroCell]:
#         """Objects of this category (n_cells(0))."""
#         return self.cells().get_zero_cells()

#     @final
#     @override
#     def morphisms(self) -> Sequence[CategoryABCs.OneMorphism]:
#         """Morphisms of this category (n_cells(1))."""
#         return self.cells().get_one_cells()

#     # === Constructions ===
#     @override
#     @final
#     def diagonal_morphism_C(self, x: CategoryABCs.ZeroCell) -> CategoryABCs.OneMorphism:
#         """Returns the diagonal morphism Δ: X → X × X."""
#         P = self.product_C([x, x])
#         assert CategoryTypeChecks.is_product(P)
#         Delta = P.lift_morphisms([x.identity_endomorphism_on_self(), x.identity_endomorphism_on_self()])
#         assert CategoryTypeChecks.is_object(P)
#         return Delta

#     @final
#     @override
#     def codiagonal_morphism_C(self, x: CategoryABCs.ZeroCell) -> CategoryABCs.OneMorphism:
#         """Returns the codiagonal morphism ∇: X + X → X."""
#         C = self.coproduct_C([x, x])
#         assert CategoryTypeChecks.is_coproduct(C)
#         Eta = C.colift_morphisms([x.identity_endomorphism_on_self(), x.identity_endomorphism_on_self()])
#         assert CategoryTypeChecks.is_object(C)
#         return Eta

#     # === Hom ===

#     @overload
#     def hom_C(self) -> CategoryABCs.HomC: ...

#     @overload
#     def hom_C(self, x: CategoryABCs.ZeroCell, y: CategoryABCs.ZeroCell) -> CategoryABCs.HomC_xy: ...

#     @final
#     @override
#     def hom_C(
#         self, x: CategoryABCs.ZeroCell | None = None, y: CategoryABCs.ZeroCell | None = None
#     ) -> CategoryABCs.HomC | CategoryABCs.HomC_xy:
#         """
#         hom_C() returns the full Hom_C category.
#         hom_C(x, y) returns Hom_C(x, y).
#         """
#         HomC = self.homC_category_class()(self)
#         assert CategoryTypeChecks.is_HomC_category(
#             HomC
#         ), "Coding error: hom_category_class did not return HomC"
#         if x is None or y is None:
#             return HomC
#         HomC_xy = HomC.__object_from_domain_and_codomain__(x, y)
#         assert CategoryTypeChecks.is_HomC_xy_category(
#             HomC_xy
#         ), "Coding error: __object_from_domain_and_codomain__ did not return HomC_xy"
#         return HomC_xy

#     # Do not mark overloads with @final or @override, only the implementation.
#     @overload
#     def end_C(self) -> CategoryABCs.EndC: ...

#     # Do not mark overloads with @final or @override, only the implementation.
#     @overload
#     def end_C(self, x: CategoryABCs.ZeroCell) -> CategoryABCs.EndC_x: ...

#     @final
#     @override
#     def end_C(
#         self, x: CategoryABCs.ZeroCell | None = None
#     ) -> CategoryABCs.EndC_x | CategoryABCs.EndC:
#         """End_C or End_C(X) as an object in End_C."""
#         EndC = self.endC_category_class()(self)
#         assert CategoryTypeChecks.is_EndC_category(
#             EndC
#         ), "Coding error: end_category_class did not return EndC"
#         if x is None:
#             return EndC
#         EndC_x = EndC.ZeroCell_C_from(domain=x, codomain=x)
#         assert CategoryTypeChecks.is_EndC_x_category(
#             EndC_x
#         ), "Coding error: object_from did not return EndC_x"
#         return EndC_x

#     # Do not mark overloads with @final or @override, only the implementation.
#     @overload
#     def aut_C(self) -> CategoryABCs.AutC: ...

#     # Do not mark overloads with @final or @override, only the implementation.
#     @overload
#     def aut_C(self, x: CategoryABCs.ZeroCell) -> CategoryABCs.AutC_x: ...

#     @final
#     @override
#     def aut_C(
#         self, x: CategoryABCs.ZeroCell | None = None
#     ) -> CategoryABCs.AutC_x | CategoryABCs.AutC:
#         """Aut_C or Aut_C(X) as an object in Aut_C."""
#         AutC = self.autC_category_class()(self)
#         assert CategoryTypeChecks.is_AutC_category(
#             AutC
#         ), "Coding error: aut_category_class did not return AutC"
#         if x is None:
#             return AutC
#         AutC_x = AutC.ZeroCell_C_from(domain=x, codomain=x)
#         assert CategoryTypeChecks.is_AutC_x_category(
#             AutC_x
#         ), "Coding error: object_from did not return AutC_x"
#         return AutC_x

#     # === Structure ===

#     @final
#     @override
#     def dual_C(self, x: CategoryABCs.ZeroCell, additive: bool = False) -> CategoryABCs.HomC_xy:
#         """
#         X.dual() := ~X := Hom_C(X, C.multiplicative_unit()) if additive is False.
#         X.dual(True) := -X := Hom_C(X, C.additive_unit()).

#         E.g. for C = RMod, X.dual() = Hom_R(X, R) and X.dual(True) = ⟨0⟩_R.
#         """
#         unit = self.additive_unit_C() if additive else self.multiplicative_unit_C()
#         return self.hom(unit)

#     # === Subcategories ===
#     @final
#     @override
#     def self_as_subobject(self) -> CategoryABCs.Nontrivial_TwoCategory:
#         """Return self.amb().subobject_from([self])."""
#         assert CategoryTypeChecks.is_category(self)
#         return self.amb().subobject_C([self])

#     # === Predicates (class-level structural properties) ===

#     @final
#     @override
#     def is_op_category(self) -> bool:
#         """
#         False for ordinary categories. True for opcategories C^op.

#         Override to return True in OpCategory subclasses.
#         """
#         return False

#     # === Equivalence checks ===

#     @final
#     @override
#     def is_isomorphic_to(self, other: CategoryABCs.ZeroCell) -> BoolProof:
#         """
#         X ≅ Y BoolProof.
#         """
#         return self.is_equivalent_to(other)

#     @final
#     @override
#     def is_equivalent_to(self, other: CategoryABCs.ZeroCell) -> BoolProof:
#         """
#         X ≃ Y: check for equivalence via morphisms and higher cells.

#         Looks for f: X -> Y, g: Y -> X in amb, then 2-cells
#         α: g∘f ≃ id_X and β: f∘g ≃ id_Y, and so on up to self.level.
#         """
#         if self.amb() != other.amb():
#             return BoolProof.no_proof("Objects are in different categories")
#         if self.level() == 0:
#             return self.is_equal_to(other)

#         C = self.amb()

#         # Find pairs (f, g) in Hom(X,Y) × Hom(Y,X)
#         hom_xy = C.hom_C(self, other)
#         hom_yx = C.hom_C(other, self)
#         hom_product = C.product_C([hom_xy, hom_yx])

#         end_x = C.end_C(self)
#         end_y = C.end_C(other)
#         assert CategoryTypeChecks.is_EndC_x_category(end_x), "end_C(self) must return EndC_x"
#         assert CategoryTypeChecks.is_EndC_x_category(end_y), "end_C(other) must return EndC_x"
#         id_x = end_x.identity_endomorphism_on_self()
#         id_y = end_y.identity_endomorphism_on_self()

#         for fg_pair in hom_product.ZeroCells():
#             f, g = fg_pair
#             assert CategoryTypeChecks.is_morphism(f), "f must be a morphism"
#             assert CategoryTypeChecks.is_morphism(g), "g must be a morphism"
#             gf = g.compose(f)
#             fg = f.compose(g)

#             # Check g∘f ≃ id_X and f∘g ≃ id_Y (recurses down to equality at level 0)
#             if gf.is_equivalent_to(id_x) and fg.is_equivalent_to(id_y):
#                 return BoolProof.true("Found equivalence via morphism pair")

#         return BoolProof.no_proof("No equivalence found")

#     # === Fiber/Kernel/Cofiber constructions ===

#     @override
#     @final
#     def fiber_C(self, y: CategoryABCs.Point, f: CategoryABCs.OneMorphism) -> CategoryABCs.ZeroCell:
#         """Fib_y(f: X → Y) := X ×_Y *."""
#         return self.pullback_C(f, y)

#     @final
#     @override
#     def kernel_C(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.ZeroCell:
#         """ker(f) := Fib_*(f) where * is the terminal object of codomain."""
#         term_Y = f.target().terminal_object_C()
#         term_C = self.amb().terminal_object_C()
#         p = self.amb().morphism_C_from(
#             domain=term_C,
#             codomain=f.target(),
#             data=term_Y,
#         )
#         return self.fiber_C(p, f)

#     @final
#     @override
#     def cofiber_C(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.ZeroCell:
#         """Cof(f) := * +^X Y (Pushout of initial object map)."""
#         init_C = self.amb().initial_object_C()
#         assert CategoryTypeChecks.is_initial(
#             init_C
#         ), "initial_object_C must return an initial object"
#         init_X = init_C.unique_morphism_to(f.source())
#         return self.pushout_C(init_X, f)

#     @override
#     @final
#     def quotient_C(
#         self,
#         data: CategoryABCs.ZeroCell | CategoryABCs.OneMorphism,
#     ) -> CategoryABCs.ZeroCell:
#         """
#         Quotient construction. Inputs:
#             - A (mono)morphism f: X -> Y
#             - An object Y with a slice structure (Y, f: X -> Y)
#             - An object X with a coslice structure (X, f: X -> Y)

#         Returns a coslice object (X/Y, q: Y-> X/Y)in C_{Y/}.
#         """
#         if self.is_morphism_C(data):
#             f = data
#             assert CategoryTypeChecks.is_morphism(f)
#             return self.cofiber_C(f)
#         elif self.is_object_C(data):
#             if self.is_slice_object_C(data):
#                 # (Y, f: X -> Y) => (Y/X, q: Y -> Y/X)
#                 Y = data
#                 # Get first slice structure for this object
#                 slice_structs = [
#                     s for s in Y.structures() if isinstance(s, self.slice_object_class())
#                 ]
#                 if not slice_structs:
#                     raise ValueError("No slice structure found")
#                 slice_struct = slice_structs[0]
#                 return self.quotient_C(slice_struct.structure_morphism())
#             elif self.is_coslice_object_C(data):
#                 # (X, f: X -> Y) => (Y/X, q: Y -> Y/X)
#                 X = data
#                 # Get first coslice structure for this object
#                 coslice_structs = [
#                     s for s in X.structures() if isinstance(s, self.coslice_object_class())
#                 ]
#                 if not coslice_structs:
#                     raise ValueError("No coslice structure found")
#                 coslice_struct = coslice_structs[0]
#                 return self.quotient_C(coslice_struct.structure_morphism())
#         raise ValueError("Invalid quotient data")

#     # === Sampling methods ===

#     @final
#     @override
#     def an_object(self) -> CategoryABCs.ZeroCell:
#         return next(iter(self.ZeroCells()))

#     @final
#     @override
#     def a_morphism(self) -> CategoryABCs.OneMorphism:
#         return next(iter(self.morphisms()))

#     @final
#     @override
#     def some_objects(self, n: int | None = 5) -> Sequence[CategoryABCs.ZeroCell]:
#         return list(self.ZeroCells())[:n]

#     @final
#     @override
#     def some_morphisms(self, n: int | None = 5) -> Sequence[CategoryABCs.OneMorphism]:
#         return list(self.morphisms())[:n]

#     @final
#     @override
#     def random_object(self) -> CategoryABCs.ZeroCell:
#         return random.choice(list(self.ZeroCells()))

#     @final
#     @override
#     def random_morphism(self) -> CategoryABCs.OneMorphism:
#         return random.choice(list(self.morphisms()))

#     @final
#     @override
#     def random_objects(self, n: int | None = 5) -> Sequence[CategoryABCs.ZeroCell]:
#         return random.sample(list(self.ZeroCells()), n or 5)

#     @final
#     @override
#     def random_morphisms(self, n: int | None = 5) -> Sequence[CategoryABCs.OneMorphism]:
#         return random.sample(list(self.morphisms()), n or 5)

#     @final
#     @override
#     def is_zero_object_C(self, x: CategoryABCs.ZeroCell) -> BoolProof:
#         """Check if x is a zero object in C."""
#         if not self.is_pointed().is_true():
#             if self.is_pointed().is_false():
#                 return BoolProof.false("C is not pointed, so has no zero objects")
#             return BoolProof.no_proof("No proof that C is not pointed, so has no zero objects")
#         is_initial = self.is_initial_object_C(x).is_true()
#         is_terminal = self.is_terminal_object_C(x).is_true()
#         if is_initial and is_terminal:
#             return BoolProof.true("x is a zero object")
#         return BoolProof.no_proof("x is not a zero object")

#     # =========================================================================
#     # Category Operators (merged from CategoryOperators_Base)
#     # =========================================================================

#     # === Products and Coproducts ===

#     @override
#     @final
#     def __and__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X & Y := X ∏ Y in C."""
#         return self.product(other)

#     @override
#     @final
#     def __or__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X | Y := X ∐ Y in C."""
#         return self.coproduct(other)

#     # === Hom ===

#     @override
#     @final
#     def __rshift__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.HomC_xy:
#         """X >> Y := Hom_C(X, Y)."""
#         return self.hom(other)

#     @override
#     @final
#     def __lshift__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.HomC_xy:
#         """X << Y := Hom_C(Y, X)."""
#         return other.hom(self)

#     # === Containment ===

#     @override
#     @final
#     def __contains__(self, other: CategoryABCs.ZeroCell) -> bool:
#         """Y in C ⇔ Y is an object of C."""
#         return other in self.cells()

#     # === Addition ===

#     @override
#     @final
#     def __add__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X + Y := X ∐ Y by default."""
#         return self.coproduct(other)

#     # === Multiplication ===

#     @overload
#     def __mul__(self, other: int) -> CategoryABCs.ZeroCell: ...

#     @overload
#     def __mul__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell: ...

#     @final
#     def __mul__(self, other: CategoryABCs.ZeroCell | int) -> CategoryABCs.ZeroCell:
#         """X * Y := X ∏ Y; n * X := X + X + ... + X (n times)."""
#         n = other
#         match other:
#             case n if isinstance(n, int):
#                 match n:
#                     case n if n== 0:
#                         return self.amb().additive_unit_C()
#                     case n if n < 0:
#                         return (-n) * (-self)
#                     case n if n > 0:
#                         return reduce(lambda a, b: a + b, n *  [self])
#                     case _:
#                         assert_never(cast("Never", n))
#             case n if isinstance(n, CategoryABCs.ZeroCell):
#                 return self.amb().product_C([self, n])
#             case _:
#                 raise TypeError("Invalid type for multiplication")



#     @override
#     @final
#     def __rmul__(self, other: int) -> CategoryABCs.ZeroCell:
#         """n * X := X + X + ... + X (n times)."""
#         return self.__mul__(other)

#     # === Matmul ===

#     @override
#     @final
#     def __matmul__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X @ Y := X * Y by default."""
#         return self.amb().product_C([self, other])

#     # === Negation/Duality ===

#     @override
#     @final
#     def __neg__(self) -> CategoryABCs.ZeroCell:
#         """-X := Hom_C(X, 0) = additive dual."""
#         return self.dual(additive=True)

#     @override
#     @final
#     def __sub__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X - Y := X + (-Y)."""
#         return self + (-other)  # type: ignore[user-decision]

#     @override
#     @final
#     def __invert__(self) -> CategoryABCs.HomC_xy:
#         """~X := Hom_C(X, 1) = multiplicative dual."""
#         Xp = self.dual(additive=False)
#         assert CategoryTypeChecks.is_HomC_xy_category(Xp)
#         return Xp

#     @override
#     @final
#     def __truediv__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X / Y := X * (~Y)."""
#         return self * (~other)  # type: ignore[user-decision]

#     # === Exponentiation ===

#     @overload
#     def __pow__(self, other: int) -> CategoryABCs.ZeroCell: ...

#     @overload
#     def __pow__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.HomC_xy: ...

#     @override
#     @final
#     def __pow__(
#         self, other: CategoryABCs.ZeroCell | int
#     ) -> CategoryABCs.ZeroCell:
#         """X ** Y := Hom_C(Y, X); X ** n := X * X * ... * X (n times)."""
#         if isinstance(other, int):
#             n = other
#             if n == 0:
#                 return self.amb().multiplicative_unit_C()
#             elif n < 0:
#                 return (~self) ** (-n)  # type: ignore[user-decision]
#             else:
#                 result: CategoryABCs.ZeroCell = self
#                 for _ in range(n - 1):
#                     result = result * self  # type: ignore[user-decision]
#                 return result
#         return other.hom(self)

#     # === Quotient ===

#     @override
#     @final
#     def __mod__(self, other: CategoryABCs.ZeroCell) -> CategoryABCs.ZeroCell:
#         """X % Y := X.quotient(Y)."""
#         return self.quotient(other)

#     # === Equality ===

#     @override
#     @final
#     def __eq__(self, other: Any) -> bool:
#         """X == Y ⇔ X.is_equal_to(Y)."""
#         if not CategoryTypeChecks.is_object(other):
#             return False
#         return self.is_equal_to(other).has_proof()

#     @override
#     @final
#     def __ne__(self, other: Any) -> bool:
#         """X != Y ⇔ not X.is_equal_to(Y)."""
#         if not CategoryTypeChecks.is_category(other):
#             return True
#         return self.is_equal_to(other).is_true()

#     # === Comparison ===

#     @override
#     @final
#     def __lt__(self, other: CategoryABCs.ZeroCell) -> bool:
#         """X < Y ⇔ ∃f ∈ Hom_C(X, Y) and X != Y."""
#         return self <= other and self != other

#     @override
#     @final
#     def __le__(self, other: CategoryABCs.ZeroCell) -> bool:
#         """X <= Y ⇔ Hom_C(X, Y) != ∅."""
#         return self.hom(other).is_initial().is_false()

#     @override
#     @final
#     def __gt__(self, other: CategoryABCs.ZeroCell) -> bool:
#         """X > Y ⇔ Hom_C(Y, X) != ∅ and X != Y"""
#         return self >= other and self != other

#     @override
#     @final
#     def __ge__(self, other: CategoryABCs.ZeroCell) -> bool:
#         """X >= Y ⇔ Hom_C(Y, X) != ∅."""
#         return self.hom(other).is_initial().is_false()


#     # === Truthiness ===

#     @override
#     @final
#     def __bool__(self) -> bool:
#         """True ⇔ X != ∅."""
#         return self.is_initial().is_false()

#     # === Repr/Hash/Len/Iter ===

#     @override
#     @final
#     def __repr__(self) -> str:
#         """Default repr: category name or class name."""
#         return self.category_name()

#     @override
#     @final
#     def __hash__(self) -> int:
#         """hash(X) based on its unique id."""
#         return id(self)

#     @override
#     @final
#     def __len__(self) -> int:
#         """Returns |Ob(X)| as a cardinal."""
#         return len(list(self.ZeroCells()))

#     @override
#     @final
#     def __iter__(self) -> Iterator[CategoryABCs.ZeroCell]:
#         """Iterates over all objects in Ob(C)."""
#         return iter(self.ZeroCells())

#     @override
#     @final
#     def __next__(self) -> CategoryABCs.ZeroCell:
#         """Returns the next object in iteration."""
#         raise StopIteration

#     # === Slicing/Indexing ===

#     @overload
#     def __getitem__(self, key: int) -> CategoryABCs.ZeroCell: ...

#     @overload
#     def __getitem__(self, key: slice) -> list[CategoryABCs.ZeroCell]: ...

#     @override
#     @final
#     def __getitem__(self, key: int | slice) -> CategoryABCs.ZeroCell | list[CategoryABCs.ZeroCell]:
#         """C[i] returns i-th object; C[i:j] returns list of objects."""
#         objs = list(self.ZeroCells())
#         return objs[key]

#     # === Call ===

#     @override
#     @final
#     def __call__(self, **cell_data: Any) -> CategoryABCs.ZeroCell:
#         """Construct an object in C from cell_data."""
#         return self.ZeroCell_C_from(**cell_data)


# _ = _CatW_Base
