<!--
Origin: gitclones/integral_lattice/cat/docs/sage_integration.md (lines 1-55,
the authored roster; the remainder of that file is verbatim Sage source and
was not absorbed — the unmodified original is in
notes/category-design/n-category-tower/docs/sage_integration.md).
Landed 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, section R4), with the roster's three false
statements corrected as recorded below.
-->

# The lattice-category roster, corrected

The source corpus opened with a target roster of the lattice-theoretic
categories to build. The preamble
(`src/dzack_research/preamble/categories/`) now owns essentially all of it;
this document is that roster restated as a coverage check against the owned
tree, with the source's errors corrected in place and recorded at the end.

## The tower

| Roster entry | Corrected statement | Owner in the preamble |
|---|---|---|
| `fgMod_R` over a PID | finitely generated modules, with free and torsion subcategories as axioms | `modules/framed/finitely_generated/` (`finitely_presented_modules.sage`, `finitely_generated_free_modules.sage`, `finitely_presented_torsion_modules.sage`) |
| `Bil_R` | modules with a symmetric bilinear form $b: M \otimes_R M \to W$ — an element of $\operatorname{Sym}^2(M^\vee)$ when $W = R$, never of $\operatorname{Sym}^2(M)$; the value module $W$ is part of the datum | `modules/framed/formed/form_modules.sage` (`SymmetricBilinearFormModules`) |
| `Lat_R` | **projective** module with a symmetric bilinear form; nondegeneracy is a further *axiom*, not part of the definition | `modules/framed/formed/lattices.sage` (`Lattices(R)` = `SymmetricBilinearFormModules(R).Projective()`), axioms in `lattice_axioms.sage` |
| `pAdic_Lattice` | `Lat_{Z_p}` | the same category over $\mathbb Z_p$ (base-ring parameter) |
| `Lattice` | `Lat_ZZ`, integral — of **any** signature; definiteness, indefiniteness and hyperbolicity are subcategories, so the class is not defined by indefiniteness | `integrallattice/integral_lattices.sage` (`IntegralLattices`) |
| `DefiniteLattice` | signature $(n,0)$ or $(0,n)$ | `integrallattice/definite_lattices.sage` |
| `HyperbolicLattice` | signature $(1,n)$ or $(n,1)$, $n \ge 1$ | `integrallattice/hyperbolic_lattices.sage` |
| `UnimodularLattice` | the **correlation** $c: L \to L^\vee$, $v \mapsto b(v,-)$, is an isomorphism (equivalently $A_L = \operatorname{coker} c$ is trivial) — never the existence of an abstract isomorphism $L \cong L^\vee$ | `integral_lattices.sage` `is_unimodular` (decided on the correlation) |
| `p_ElementaryLattice`, `two_ElementaryLattice` | $A_L \cong (\mathbb Z/p)^a$ | `integral_lattices.sage` `is_p_elementary`; the $(r,a,\delta)$ tables in `catalogue.sage` |
| `RootLattice` | $\langle \Phi(L) \rangle_{\mathbb Z} = L$; recognition from a definite lattice is `root_sublattice()` | `integrallattice/root_lattices.sage`; recognition in `definite_lattices.sage` |
| `GLattice` | a lattice with a group morphism $\rho: G \to O(L)$, constructed by the caller | `modules/group_modules/group_lattices.sage` |
| `DiscriminantGroup` | torsion module with the discriminant form valued in $\mathbb Q/\mathbb Z$ (bilinear) or $\mathbb Q/2\mathbb Z$ (quadratic, even case) — **not** in $R$: for torsion $M$, $\operatorname{Hom}(M \otimes M, \mathbb Z) = 0$, so the roster's `torsion_Bil_ZZ` (forms valued in the base ring) holds only zero forms | `modules/framed/formed/torsionform/discriminant_{bilinear,quadratic}_modules.sage` |
| `GramMatrix` | presentation datum, crossed once at construction | `categories/forms/gram_matrices.sage` |
| `Genus_L` | the adelic isometry class, held as (signature pair, discriminant quadratic form) | `integral_lattices.sage` `class Genus` |
| `CoxeterData` / `CoxeterDiagram` | | `integrallattice/coxeter_diagrams.sage`, `vinberg_invariants.sage` |
| `LatticeOrthogonalGroup` | $O(L)$ as `L.Aut()`, an owned group | `integral_lattices.sage` `Aut`; `lattice_isometries.sage` |
| the functor `Free_R[S]` | the free-module functor on a finite ordered set, with its action on morphisms (the permutation-matrix representation) | `categories/functors/free_forgetful_adjunction.sage` (`FreeModuleFunctorClass`) |
| interfaces (Julia/Oscar, GAP, PARI, polyhedral_common) | engines behind seams, verified at the boundary | `integrallattice/engines.sage`; PARI behind `definite_lattices.sage` |
| ∅, ∗, ordinals, free categories on graphs, `Set`/`Group`/`Ring`/`Mod_R`, `Ch(Mod_R)` | the abstract-category tier of the roster | partly `categories/abstract_categories/`; the rest is recorded as candidacy in `n-category-tower/INDEX.md` |

## The three corrected statements

Recorded by the corpora audit (PLAN-corpora-audit-registry, error row for
`cat/docs/sage_integration.md`); each correction above is marked in bold.

1. **Unimodularity is not an abstract isomorphism.** The roster wrote
   `UnimodularLattice: L ≅ L^v`. For a nondegenerate lattice the dual module
   $L^\vee = \operatorname{Hom}_R(L, R)$ is free of the same rank, so an
   abstract *module* isomorphism always exists. Unimodularity is that the correlation the form induces,
   $c: L \to L^\vee$, is an isomorphism — equivalently, the discriminant
   group is trivial.

2. **`Lat_R := free_Bil_R` and the nondegeneracy qualifier disagree.** The
   roster defined `Lat_R` as `free_Bil_R` and then "identified" it with
   pairs $(M, b)$ with $b$ nondegenerate. Nondegeneracy is an axiom on top
   of the form category, not a consequence of freeness; and the preamble's
   settled definition makes a lattice a *projective* module with a form,
   with freeness, finite generation, integrality and nondegeneracy all
   separate axioms.

3. **A bilinear form is not an element of $\operatorname{Sym}^2(M)$.** A
   symmetric bilinear form on $M$ valued in $R$ is a map
   $\operatorname{Sym}^2(M) \to R$, i.e. an element of
   $\operatorname{Sym}^2(M^\vee)$; in the preamble's generality the value
   module is an arbitrary $W$ and the form is the morphism, so the
   statement is corrected by naming the codomain.

The same audit row also recorded the self-contradiction
`Lattice := Lat_ZZ with indefinite signature` followed by
`DefiniteLattice` as one of its specializations; the corrected table above
defines the class by integrality alone and lets signature be the
subcategory datum.

## The one signature class with no category: parabolic

Added 2026-08-20 from the Coxeter deletion audit
(PLAN-coxeter-deletion-audit-registry, readers T and P1), where two
independent corpora built this node and the preamble has none.

The signature trichotomy a Coxeter diagram induces on its root lattice is
three-way, and the table above holds only two of the three:

| type | signature of the Gram matrix | owner |
|---|---|---|
| elliptic (spherical) | $(0,n,0)$ — negative definite | `definite_lattices.sage` |
| parabolic (euclidean) | $(0,n-1,1)$ — negative semidefinite of corank 1 | **none** |
| hyperbolic | $(1,n-1,0)$ — Lorentzian | `hyperbolic_lattices.sage` |

At diagram level all three exist: `coxeter_diagrams.sage` has `is_elliptic`
and `is_parabolic`, and `vinberg_invariants.sage` has all of `is_elliptic`,
`is_parabolic`, `is_hyperbolic`. At lattice level the parabolic row has no
category, and `integral_lattices.sage`'s `refine_one_lattice` drops a
negative semidefinite lattice out of `IntegralLattices` rather than routing
it anywhere, because these lattices are degenerate: the radical is the
rank-1 kernel of the correlation, and its quotient is the negative definite
finite part. So $\tilde A_1$ with Gram $[[-2,2],[2,-2]]$ and $\tilde A_2$
with Gram $[[-2,1,1],[1,-2,1],[1,1,-2]]$ — signatures $(0,1,1)$ and
$(0,2,1)$ — are the smallest specimens the owned tree cannot place.

The predicate the routing edge would use already exists
(`is_negative_semidefinite`, `integral_lattices.sage`). What is missing is
the category and its refinement edge, and above it the degenerate node the
design corpora put parabolic under (radical, radical complement, whether the
radical splits off — $L \cong \operatorname{rad}(L) \oplus L'$ with $L'$
nondegenerate — the stabilizer of the radical in $O(L)$; then null root,
level, real and imaginary roots, height grading, affine Weyl group). The
design is written out in
`bilinear-module-tower/api-planning/categories/bilinear_Rmod/symmetric_Rmod/degenerate_lattices/`
and in the `sage-planning-modules-bak` generation beside it.

**This is a category-tree change, so it is a decision, not an edit.** It is
recorded here rather than made.
