# Outstanding work in the preamble

## Genuine mathematical errors

Each item below is a statement or construction that is mathematically false as
written, verified against the cited source line on 2026-08-14. Fixing an item
means correcting the mathematics, not renaming or documenting it. The Lean
formalization in `lean-categories` treats these as defects to fix, never as
conventions to import; corrected definitions flow back down to this preamble.

### False statements and wrong values

- [ ] `categories/sets/sets.sage:463` — `ℵ[1]` returns the continuum. This
  hard-codes the continuum hypothesis into the cardinal vocabulary; `ℵ₁` and
  `2^ℵ₀` are provably-distinct notions whose equality is independent of ZFC.
  Also asserts false for every index `n ≥ 2`.
- [ ] `categories/group/profinite/absolute_galois_group.sage:262` —
  `is_abelian` returns `True` whenever `char K > 0`. False: the absolute
  Galois group of `𝔽_p(t)` is nonabelian. Only finite fields give `Ẑ`.
- [ ] `categories/group/profinite/absolute_galois_group.sage:355` — the
  finite-field Frobenius is built from the *characteristic* `p`, i.e.
  `x ↦ x^p`. For `𝔽_q` with `q = p^k`, the canonical topological generator of
  `G_{𝔽_q}` is `x ↦ x^q`.
- [ ] `categories/group/profinite/absolute_galois_groups.sage:194` — the
  quadratic character's extension is built from `K.gen()**2 - a`. Over
  `K = ℚ` the generator is `1`, so this is the constant `1 - a`, not
  `x² - a`; the extension `K(√a)` is never constructed.
- [ ] `categories/modules/fractional_ideals.sage:156` — `__contains__` tests
  `x/g ∈ R` for *some* generator, which is membership in the union of the
  principal ideals `(g_i)`, not in their sum. Over `ℤ`, `1 ∈ (2,3)` is
  reported false.
- [ ] `categories/modules/module_morphisms/module_morphisms.sage:720` —
  `index` returns `1` for any full-rank image over a non-`ℤ` base with a
  non-presented codomain. Correct over a field; wrong over every other PID
  (over `k[t]`, `[N : f(M)]` is not `1` for a proper full-rank sublattice).
- [ ] `categories/modules/framed/finitely_generated/finitely_presented_modules.sage:437`
  — `is_torsion_free` returns `True` unconditionally when the base ring is
  not `ℤ`.
- [ ] `categories/modules/framed/finitely_generated/finitely_presented_modules.sage:461`
  — `cardinality` returns `ℵ₀` for every non-torsion module. False over any
  uncountable base field (`ℝ`, `ℂ`).
- [ ] `categories/modules/framed/finitely_generated/finitely_presented_modules.sage:471`
  — `exponent` returns `1` when there are no invariant factors, so a nonzero
  free module is reported to be annihilated by `1`.
- [ ] `categories/modules/framed/formed/integrallattice/lattice_isometries.sage:163`
  — `is_countable` reads countability off finiteness, answering `False` for
  an infinite `O(L)`. Every `O(L) ≤ GL_n(ℤ)` is countable.
- [ ] `categories/forms/forms.sage:741` — `BilinearFormMorphism.polar_form`
  returns the form itself. The polar form of the norm `q(x) = b(x,x)` is
  `2b`, not `b`; as written the method is the identity under a false name.
- [ ] `categories/schemes/varieties.sage:154` — `arithmetic_genus` and
  `geometric_genus` both return the engine's `genus()`. The two invariants
  differ exactly on singular curves, which is the case that makes them two
  notions.
- [ ] `categories/schemes/schemes.sage:165,175,227,237` — `Pic(𝔸ⁿ) = 0`,
  `Cl(𝔸ⁿ) = 0`, `Pic(ℙⁿ) = ℤ`, `Cl(ℙⁿ) = ℤ` are pinned over an arbitrary
  base ring. True over a regular (resp. UFD) base; over general `S`,
  `Pic(ℙⁿ_S) ≅ Pic(S) × ℤ`. The four groups are also built as unrelated free
  modules with no `Pic → Cl` comparison and no `𝒪(1)` generator identified.
- [ ] `categories/modules/framed/formed/integrallattice/integral_lattices.sage:443-470`
  — `is_isometric` fuses three wrong or overreaching branches: the definite
  branch feeds `QuadraticForm(±G)` with the undoubled Gram matrix (ill-formed
  for odd lattices; `lattice_isometries.sage` doubles to `2G` for the same
  engine); the rank-2 branch asserts even diagonals, rejecting odd binary
  lattices; the fallback `genus() == genus()` concludes isometry from genus
  equality, valid only under Eichler's hypotheses (indefinite, rank ≥ 3, not
  spinor-exceptional).

### Wrong constructions (the object produced is not the object named)

- [ ] `categories/functors/base_change_adjunction.sage` —
  `RestrictionOfScalarsFunctor._apply_functor` returns
  `BasedFreeModule(R, module.module_generating_set())`: the free `R`-module
  on the module's generating labels, not the module read over `R` through
  the ring map. Its own docstring says `G(F(L))` is `L ⊗ ℚ` read additively
  over `ℤ` "and explicitly not `L`"; the code returns exactly the free
  module on `L`'s labels. The adjunction `F ⊣ G` in the same file is stated
  over this broken `G`.
- [ ] `sterk.sage:251` — `involute` is `x ↦ x + s_{v₂₂}(x)`, the
  symmetrization (twice the orthogonal projection onto `v₂₂^⊥`), not an
  involution: it is not invertible and does not square to the identity.
- [ ] `categories/algebras/framed_free_algebras.sage:980` (`subs`, and the
  same pattern in `_extend_to_monomials`) — substitution raises generator
  images to plain powers. For the divided-power flavor this is wrong:
  `γ_e(s) ↦ f(s)^e = e!·γ_e(f(s)) ≠ γ_e(f(s))`, so the extension is not the
  divided-power extension it must be.
- [ ] `categories/functors/free_forgetful_adjunction.sage` —
  `DividedPowerAlgebraFunctor` is grouped with `T`, `Sym`, `Λ` as a "free
  algebra functor" carrying the same unit `M → U(Γ M)`. `Γ` is not left
  adjoint to any forgetful functor to modules (it is the graded dual of
  `Sym`, coinciding with it only in characteristic 0), so the shared unit
  and the adjunction framing are wrong for this flavor.
- [ ] `categories/forms/forms.sage` (`_degree_construction`) — `Γ^n` of a
  presented module is computed by the generators-modulo-relations quotient
  formula, which is a right-exactness argument. `Γ^n` is not right exact,
  so for a non-free presented module the constructed object is not `Γ^n M`.
- [ ] `categories/algebras/framed_free_algebras.sage:641,650` —
  `is_integral_domain` (degree-additivity argument) and `krull_dimension`
  (`dim R + |S|`) sit on the shared free-algebra parent and are inherited by
  the alternating flavor, where `x∧x = 0` gives zero divisors and the
  algebra is finite over `R`, and by the noncommutative tensor flavor, where
  the polynomial dimension formula does not apply.

### Internal contradictions (one of the two sides must yield)

- [ ] `categories/modules/framed/formed/integrallattice/integral_lattices.sage`
  — `discriminant` computes the signed determinant
  `(−1)^{n(n−1)/2} det G` while `_latex_` displays `det G`; one word denotes
  two numbers in one file.
- [ ] `categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage`
  — `minimal_edge_lattices` proves there is no triple edge for roots of
  norms `−2`/`−4` (correct: `b² ∈ {3, 6, 12}` has no integer solution), yet
  the drawing convention and `_tikz_edge_style` still render a triple edge
  for `m = 6`. The vestigial rendering contradicts the theorem.
- [ ] `categories/modules/group_modules/` — "coinvariants" names two
  different objects: `module_coinvariants` is the quotient `M/⟨gv − v⟩`,
  `coinvariant_lattice` is the orthogonal complement `(L^G)^⊥`. They agree
  only up to finite index and only under hypotheses stated nowhere.
- [ ] `categories/modules/module_morphisms/module_morphisms.sage`
  (`GroupAction`) asserts `G` finite and stores a complete value table,
  while `group_lattices.sage` documents support for infinite-order
  isometries and checks equivariance on generators precisely so that
  finiteness is unnecessary. The promised infinite-group generality is
  unreachable through the only action constructor.
- [ ] `categories/modules/framed/formed/integrallattice/integral_lattices.sage`
  (`_gram_from_name`) builds ADE root lattices positive definite (diagonal
  `+2`) while `catalogue.sage` twists every named root lattice to negative
  definite; both signs circulate under the same names. The decided
  convention (negative definite, constructed from root realizations) must
  be enforced at the single construction site.
- [ ] `categories/modules/framed/formed/integrallattice/integral_lattices.sage`
  (`Aut` docstring) — finite presentation of `O(L)` for indefinite `L` is
  attributed to Borel–Harish-Chandra, which gives arithmeticity and finite
  generation; finite presentation is Borel–Serre / Raghunathan.

## Gaps

New mathematical gaps belong here only after a concrete object, morphism, or
property is shown to be absent from the current preamble.
