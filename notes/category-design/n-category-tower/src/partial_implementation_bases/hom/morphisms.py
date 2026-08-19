# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/hom/morphisms.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# """
# Morphism_Base: Concrete implementations for Morphism_ABC.

# Implements the hierarchical morphism equality waterfall strategy.
# See docs/implementation_plan_equality.md for specification.
# """

# from __future__ import annotations

# from collections.abc import Callable
# from dataclasses import dataclass
# from typing import Any, final, override

# import sympy  # type: ignore[external-library]
# from sympy import ConditionSet, Eq, Symbol  # type: ignore[external-library]

# from src._types import (
#     BoolProof,
#     CategoryABCs,
#     CategoryBases,
#     CategoryTypeChecks,
#     SageTypeChecks,
# )

# # Constants for equality checking
# _SMALL_DOMAIN_THRESHOLD = 10**6
# _PROBABILISTIC_SAMPLE_SIZE = 10**6

# class _Morphism_Category_Cell_Container_Base(CategoryABCs.Nontrivial_TwoCategory_Cell_Container): 
#     pass

# @dataclass
# class Morphism_Base(CategoryABCs.OneMorphism, CategoryBases.EmptyCategory):
#     """
#     Base implementation for morphisms with concrete equality logic.

#     Provides:
#     - Hierarchical `is_equal_to` waterfall strategy
#     - Composition operators (@, >>, <<)
#     - Decomposition tracking for compositional equality

#     Inherits from Morphism_ABC which inherits from CatW_ABC.

#     Fields inherited from Morphism_ABC:
#         domain: Domain object
#         codomain: Codomain object
#         underlying_object: The underlying callable f: domain -> codomain
#     """

#     @override
#     @final
#     def amb(self) -> CategoryABCs.Nontrivial_TwoCategory:
#         return self.source().amb()

#     @override
#     @final
#     def is_equal_to(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Check if f == g using hierarchical waterfall strategy.

#         Uses BoolProof as accumulator with += to track attempted strategies.
#         """
#         if not CategoryTypeChecks.is_morphism(other):
#             return BoolProof.no_proof("Unable to prove equality of a morphism with a non-morphism")

#         # Early filters (these are definitive)
#         if self is other:
#             return BoolProof.true("literal identity")

#         if self.amb() is not other.amb():
#             return BoolProof.false("different ambient categories")

#         if not self.source().is_equal_to(other.source()).is_true():
#             return BoolProof.false("different domains")
#         if not self.target().is_equal_to(other.target()).is_true():
#             return BoolProof.false("different codomains")

#         # Accumulator for waterfall
#         proof = BoolProof()

#         proof += self._check_decompositions(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_small_domain(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_finitely_generated(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_additive_kernel(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_sage_symbolic(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_sympy_symbolic(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_sympy_condition_set(other)
#         if proof.is_true():
#             return proof

#         proof += self._check_probabilistic(other)

#         return proof

#     def _check_decompositions(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Recursive decomposition check.

#         If f = f1 ∘ f2 ∘ ... ∘ fn and g = g1 ∘ g2 ∘ ... ∘ gn,
#         then f == g iff f1 == g1 and f2 == g2 and ... and fn == gn.
#         """
#         if not self.compositional_decompositions() or not other.compositional_decompositions():
#             return BoolProof.no_proof("decomposition: no decompositions available")

#         for self_decomp in self.compositional_decompositions():
#             for other_decomp in other.compositional_decompositions():
#                 if len(self_decomp) != len(other_decomp):
#                     continue

#                 all_equal = True
#                 for f_i, g_i in zip(self_decomp, other_decomp, strict=True):
#                     eq_result = f_i.is_equal_to(g_i)
#                     if not eq_result.is_true():
#                         all_equal = False
#                         break

#                 if all_equal:
#                     return BoolProof.true("decomposition factors match")

#         return BoolProof.no_proof("decomposition: no matching factors")

#     def _check_small_domain(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Exhaustive check for small domains.

#         If |domain| <= threshold, check f == g by verifying
#         domain == {x in domain | f(x) == g(x)}.
#         """
#         X = self.source()
#         Xp = X.apply_forgetful_functor_to_set()
#         assert CategoryTypeChecks.is_set_object(Xp), "Coding error: domain is not a set."
#         cardinality = Xp.cardinality()

#         if cardinality > _SMALL_DOMAIN_THRESHOLD:
#             return BoolProof.no_proof(f"small domain: |X| = {cardinality} > threshold")

#         f = self.underlying_object()
#         g = other.underlying_object()
#         equal_set = Xp.subobject_in_C_from([x for x in X if f(x) == g(x)])

#         result = Xp.is_equal_to(equal_set)
#         if result.is_true():
#             return BoolProof.true("exhaustive check on small domain")
#         if result.is_false():
#             return BoolProof.false("exhaustive check found difference")
#         return BoolProof.no_proof("small domain: equality inconclusive")

#     def _check_finitely_generated(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Check equality on generators for finitely generated domains.

#         If domain is finitely generated, it suffices to check equality on generators.
#         """
#         if not self.source().is_finitely_generated():
#             return BoolProof.no_proof("generators: domain not finitely generated")

#         f = self.underlying_object()
#         g = other.underlying_object()
#         generators = self.source().generators()

#         for gen in generators:
#             if f(gen) != g(gen):
#                 return BoolProof.false("generators differ", counterexample=gen)

#         return BoolProof.true("equal on all generators")

#     def _check_additive_kernel(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Kernel-based equality for additive categories.

#         In additive categories, f == g iff ker(f - g) == domain.
#         """
#         if not self.amb().is_additive():
#             return BoolProof.no_proof("kernel: ambient category not additive")

#         diff = self - other
#         assert CategoryTypeChecks.is_morphism(diff), "Coding error: diff is not an endomorphism"
#         ker = self.amb().kernel_C(diff)

#         result = self.source().is_equal_to(ker)
#         if result.is_true():
#             return BoolProof.true("ker(f - g) == domain")
#         if result.is_false():
#             return BoolProof.false("ker(f - g) != domain")
#         return BoolProof.no_proof("kernel: equality inconclusive")

#     def _check_sage_symbolic(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Check Sage symbolic expressions directly.

#         Only applies if underlying_object is already a Sage Expression.
#         """
#         if not SageTypeChecks.is_symbolic_expression(self.underlying_object):
#             return BoolProof.no_proof("Sage: self not symbolic")
#         if not SageTypeChecks.is_symbolic_expression(other.underlying_object):
#             return BoolProof.no_proof("Sage: other not symbolic")

#         f_expr = self.underlying_object()
#         g_expr = other.underlying_object()

#         if bool(f_expr == g_expr):
#             return BoolProof.true("Sage symbolic equality")

#         return BoolProof.no_proof("Sage: could not determine")

#     def _check_sympy_symbolic(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Check SymPy symbolic expressions.

#         Only applies if underlying_object is already a SymPy Basic.
#         """
#         if not SageTypeChecks.is_symbolic_expression(self.underlying_object):
#             return BoolProof.no_proof("SymPy: self not symbolic")
#         if not SageTypeChecks.is_symbolic_expression(other.underlying_object):
#             return BoolProof.no_proof("SymPy: other not symbolic")

#         f_expr = self.underlying_object()
#         g_expr = other.underlying_object()

#         diff = sympy.simplify(f_expr - g_expr)
#         if diff == 0:
#             return BoolProof.true("SymPy: simplify(f - g) == 0")
#         if diff.is_nonzero:
#             return BoolProof.false("SymPy: simplify(f - g) != 0")

#         return BoolProof.no_proof("SymPy: simplify inconclusive")

#     def _check_sympy_condition_set(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         SymPy ConditionSet push.

#         Construct C = ConditionSet(t, f(t) == g(t), domain) and check if C == domain.
#         """
#         domain_set = self.source().to_sympy_set()
#         t = Symbol("t")

#         f = self.underlying_object()
#         g = other.underlying_object()

#         C = ConditionSet(t, Eq(f(t), g(t)), domain_set)

#         if domain_set == C:
#             return BoolProof.true("ConditionSet equals domain")

#         diff = sympy.Complement(domain_set, C)
#         if diff.is_empty is True:
#             return BoolProof.true("complement is empty")
#         if diff.is_empty is False:
#             return BoolProof.false("complement is non-empty")

#         return BoolProof.no_proof("ConditionSet: inconclusive")

#     def _check_probabilistic(self, other: CategoryABCs.OneMorphism) -> BoolProof:
#         """
#         Probabilistic sampling for infinite domains.

#         Sample n random elements S from domain and check {s in S | f(s) == g(s)} == S.
#         If any mismatch found, return FALSE. Otherwise return PROBABILITY_PROOF.
#         """
#         f = self.underlying_object()
#         g = other.underlying_object()

#         samples = self.source().random_objects(_PROBABILISTIC_SAMPLE_SIZE)

#         for s in samples:
#             if f(s) != g(s):
#                 return BoolProof.false("probabilistic sampling", counterexample=s)

#         return BoolProof.probability_proof(
#             witness_strategy=f"f(s) == g(s) for {len(samples)} samples",
#             probability=1.0 - 1.0 / len(samples),
#             sample_size=len(samples),
#         )

#     # ============================================================
#     # _Morphism_ABC Abstract Method Implementations
#     # ============================================================

#     @override
#     @final
#     def range(self) -> CategoryABCs.Object:
#         """Alias for image()."""
#         return self.image()

#     @override
#     @final
#     def to_graph_of_function(self) -> frozenset[tuple[CategoryABCs.Object, CategoryABCs.Object]]:
#         """
#         Return a graph of a function R ⊂ X×Y representing the morphism.
#         Todo: return a proper subobject of the product.
#         """
#         return self.to_relation()

#     @override
#     @final
#     def to_tuple(self) -> tuple[CategoryABCs.Object, ...]:
#         """tuple(to_list())."""
#         return tuple(self.to_list())

#     @override
#     @final
#     def evaluate_at(self, x: CategoryABCs.Object) -> CategoryABCs.Object:
#         """Evaluate the morphism at x, i.e., f(x)."""
#         callable_f = self.underlying_object()
#         return callable_f(x)

#     @override
#     @final
#     def on_n_cells(self, n: int) -> Callable[[CategoryABCs.OneMorphism], CategoryABCs.OneMorphism]:
#         """F_n: Mor^n(X) → Mor^n(Y)."""
#         def apply_to_cell(x: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#             result = self.evaluate_at(x)
#             assert CategoryTypeChecks.is_morphism(result), "Expected morphism result"
#             return result
#         return apply_to_cell

#     @override
#     @final
#     def compose(self, g: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """f ∘ g if codomain(g) == domain(f), else NotWellDefinedError."""
#         assert g.target().is_equal_to(self.source()).is_true(), "Cannot compose: codomain(g) != domain(f)"
        
#         result = self.base_category().morphism_C_from(
#             domain=g.source(),
#             codomain=self.target(),
#             _underlying_object=lambda x: self.evaluate_at(g.evaluate_at(x)),
#         )

#         new_decomps = [
#             list(d1) + list(d2) 
#             for d1 in self.compositional_decompositions() 
#             for d2 in g.compositional_decompositions()
#         ]
#         result._add_compositional_decompositions(new_decomps)

#         return result

#     @override
#     @final
#     def to_callable(self) -> Callable[[Any], Any]:
#         """Return a callable f: X → Y representing the morphism."""
#         return self.underlying_object()

#     @override
#     @final
#     def to_dict(self) -> dict[CategoryABCs.Object, CategoryABCs.Object]:
#         """Return a dict representing the morphism."""
#         return {x: self.evaluate_at(x) for x in self.source().objects()}

#     @override
#     @final
#     def to_relation(self) -> frozenset[tuple[CategoryABCs.Object, CategoryABCs.Object]]:
#         """Return a relation R ⊂ X×Y representing the morphism."""
#         return frozenset((x, self.evaluate_at(x)) for x in self.source().objects())

#     @override
#     @final
#     def to_list(self) -> list[CategoryABCs.Object]:
#         """Return [f(x_i) for x_i in X]."""
#         return [self.evaluate_at(x) for x in self.source().objects()]

#     @override
#     @final
#     def is_endomorphism(self) -> BoolProof:
#         """Check if morphism is an endomorphism."""
#         if self.source().is_equal_to(self.target()).is_true():
#             return BoolProof.true("domain == codomain")
#         return BoolProof.false("domain != codomain")

#     @override
#     @final
#     def is_automorphism(self) -> BoolProof:
#         """Check if morphism is an automorphism."""
#         if not self.is_endomorphism().is_true():
#             return BoolProof.false("not an endomorphism")
#         return self.is_invertible()

#     @override
#     @final
#     def is_identity(self) -> BoolProof:
#         """Check if morphism is identity."""
#         if not self.is_endomorphism().is_true():
#             return BoolProof.false("not an endomorphism")
#         return BoolProof.no_proof("not determined")

#     # === Equality ===

#     @override
#     @final
#     def __hash__(self) -> int: # type: ignore[override-okay]
#         """Hash based on domain, codomain, and underlying object."""
#         return hash((id(self.domain), id(self.codomain), id(self)))

#     # === Product/Coproduct of morphisms ===

#     @override
#     @final
#     def __and__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: # type: ignore[override-okay]
#         """f & g := f ∏ g or pairing ⟨f, g⟩."""
#         if not CategoryTypeChecks.is_morphism(other):
#             raise TypeError(f"Expected morphism, got {type(other)}")
#         if self.source().is_equal_to(other.source()).is_true():
#             return self._pairing(other)
#         else:
#             return self._product_morphism(other)

#     @override
#     @final
#     def __or__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: # type: ignore[override-okay]
#         """f | g := f ∐ g or copairing [f, g]."""
#         if not CategoryTypeChecks.is_morphism(other):
#             raise TypeError(f"Expected morphism, got {type(other)}")
#         if self.target().is_equal_to(other.target()).is_true():
#             return self._copairing(other)
#         else:
#             return self._coproduct_morphism(other)

#     def _pairing(self, other: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """⟨f, g⟩: X → Y_1 ∏ Y_2."""
#         product = self.source().product(other.source())
#         return self.base_category().morphism_C_from(
#             domain=self.source(),
#             codomain=product,
#             data=lambda x: (self.evaluate_at(x), other.evaluate_at(x)),
#         )

#     def _copairing(self, other: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """[f, g]: X_1 ∐ X_2 → Y."""
#         coproduct = self.source().coproduct(other.source())

#         def copair_func(x: CategoryABCs.Object) -> CategoryABCs.Object:
#             if x in self.source().objects():
#                 return self.evaluate_at(x)
#             return other.evaluate_at(x)

#         return self.base_category().morphism_C_from(
#             domain=coproduct,
#             codomain=self.target(),
#             data=copair_func,
#         )

#     def _product_morphism(self, other: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """f ∏ g: X_1 ∏ X_2 → Y_1 ∏ Y_2."""
#         domain_prod = self.source().product(other.source())
#         codomain_prod = self.target().product(other.target())
#         return self.base_category().morphism_C_from(
#             domain=domain_prod,
#             codomain=codomain_prod,
#             data=lambda pair: (
#                 self.evaluate_at(pair[0]),
#                 other.evaluate_at(pair[1]),
#             ),
#         )

#     def _coproduct_morphism(self, other: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """f ∐ g: X_1 ∐ X_2 → Y_1 ∐ Y_2."""
#         domain_coprod = self.source().coproduct(other.source())
#         codomain_coprod = self.target().coproduct(other.target())

#         def coprod_func(x: CategoryABCs.Object) -> CategoryABCs.Object:
#             if x in self.source().objects():
#                 return self.evaluate_at(x)
#             return other.evaluate_at(x)

#         return self.base_category().morphism_C_from(
#             domain=domain_coprod,
#             codomain=codomain_coprod,
#             data=coprod_func,
#         )

#     # === Composition ===

#     @override
#     @final
#     def __rshift__(self, other: CategoryABCs.Object) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """f >> g := g ∘ f."""
#         assert CategoryTypeChecks.is_morphism(other), "Expected morphism"
#         return other.compose(self)

#     @override
#     @final
#     def __lshift__(self, other: CategoryABCs.Object) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """f << g := f ∘ g."""
#         assert CategoryTypeChecks.is_morphism(other), "Expected morphism"
#         return self.compose(other)

#     @override
#     @final
#     def __matmul__(self, other: CategoryABCs.Object) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """f @ g := f ∘ g."""
#         assert CategoryTypeChecks.is_morphism(other), "Expected morphism"
#         return self.compose(other)


#     # === Addition ===

#     @override
#     @final
#     def __add__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: # type: ignore[override-okay]
#         """f + g := f ∐ g by default."""
#         assert CategoryTypeChecks.is_morphism(other), "Expected morphism"
#         return self._coproduct_morphism(other)

#     # === Multiplication ===

#     @override
#     @final
#     def __mul__(self, other: CategoryABCs.Object | int) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """f * g := f ∏ g, or n * f := n * f(x)."""
#         match other:
#             case int():
#                 return self._scalar_multiply(other)
#             case CategoryABCs.OneMorphism():
#                 return self._product_morphism(other)
#             case _:
#                 raise TypeError(f"Expected morphism or int, got {type(other)}")

#     @override
#     @final
#     def __rmul__(self, other: int) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """n * f := n * f(x)."""
#         return self._scalar_multiply(other)

#     def _scalar_multiply(self, n: int) -> CategoryABCs.OneMorphism:
#         """(n*f)(x) := n * f(x)."""
#         return self.amb().morphism_C_from(
#             domain=self.domain,
#             codomain=self.codomain,
#             data=lambda x: n * self.evaluate_at(x),  # type: ignore[user-decision]
#         )

#     # === Negation ===

#     @override
#     @final
#     def __neg__(self) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """(-f)(x) := -f(x)."""
#         return self._negate()

#     def _negate(self) -> CategoryABCs.OneMorphism:
#         """(-f)(x) := -f(x)."""
#         return self.amb().morphism_C_from(
#             domain=self.domain,
#             codomain=self.codomain,
#             data=lambda x: -self.evaluate_at(x),  # type: ignore[user-decision]
#         )

#     @override
#     @final
#     def __sub__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: # type: ignore[override-okay]
#         """(f - g)(x) := f(x) - g(x)."""
#         result = self + (-other)  # type: ignore[user-decision]
#         assert CategoryTypeChecks.is_morphism(result)
#         return result

#     # === Inverse ===

#     @override
#     @final
#     def __invert__(self) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """~f := f^{-1}."""
#         return self.inverse()

#     @override
#     @final
#     def __truediv__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: # type: ignore[override-okay]
#         """(f / g)(x) := f(x) * (g(x))^{-1}."""
#         if not CategoryTypeChecks.is_morphism(other):
#             raise TypeError(f"Expected morphism, got {type(other)}")
#         return self._pointwise_divide(other)

#     def _pointwise_divide(self, other: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#         """(f / g)(x) := f(x) * (g(x))^{-1}."""
#         return self.amb().morphism_C_from(
#             domain=self.domain,
#             codomain=self.codomain,
#             data=lambda x: self.evaluate_at(x) * ~other.evaluate_at(x),  # type: ignore[user-decision]
#         )

#     # === Exponentiation ===

#     @override
#     @final
#     def __pow__(self, n: int) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """f^n := f ∘ f ∘ ... ∘ f (n times)."""
#         assert self.source().is_equal_to(
#             self.target()
#         ).is_true(), "Exponentiation only for endomorphisms"
#         if n == 0:
#             return self.amb().identity_endomorphism_on_self()
#         elif n < 0:
#             inv_result = self.inverse() ** (-n)  # type: ignore[user-decision]
#             assert CategoryTypeChecks.is_morphism(inv_result)
#             return inv_result
#         else:
#             result: CategoryABCs.OneMorphism = self
#             for _ in range(n - 1):
#                 result = result.compose(self)
#             return result

#     # === Comparison ===

#     @override
#     @final
#     def __le__(self, other: CategoryABCs.Object) -> bool: # type: ignore[override-okay]
#         """f <= g if ∃ 2-morphism α: f ⇒ g."""
#         if not CategoryTypeChecks.is_morphism(other):
#             raise TypeError(f"Expected morphism, got {type(other)}")
#         return self._has_2morphism_to(other)

#     def _has_2morphism_to(self, other: CategoryABCs.OneMorphism) -> bool:
#         """Check for 2-morphism α: f ⇒ g."""
#         hom_fg = self.amb().hom_C(self, other)
#         return len(list(hom_fg.objects())) > 0

#     # ============================================================
#     # _CatW_ABC Abstract Method Implementations for Morphisms
#     # ============================================================

#     @override
#     @final
#     def dual(self, additive: bool = False) -> CategoryABCs.OneMorphism: # type: ignore[override-okay]
#         """
#         If f ∈ Hom_C(X,Y), then f^* ∈ Hom_C(Y^*, X^*) is given by f^*(ψ) = ψ ∘ f.
#         This differs from the definition of X^* := Hom_C(X, 1) when X is an ordinary object.
#         """
#         Xp = self.source().dual()
#         Yp = self.target().dual()
#         def dual_f(psi: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
#             return psi.compose(self)
#         return Xp.amb().morphism_C_from(
#             domain=Yp,
#             codomain=Xp,
#             data=dual_f,
#         )

#     # 


# class Endomorphism_Base(CategoryABCs.Endomorphism, Morphism_Base):  # type: ignore[misc]
#     """Base class for endomorphisms."""
#     ...


# class Automorphism_Base(CategoryABCs.Automorphism, Endomorphism_Base):  # type: ignore[misc]
#     """Base class for automorphisms."""
#     ...
