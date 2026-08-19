# The first lattice DSL, and where its design differs from the preamble's

Reading of the written specification migrated 2026-08-20 from
`~/gitclones/lattice-research`. The files themselves are at
`computations/scripts/lattice-research/written-spec/`; this note is what they
say, and where the preamble deliberately says something else.

Two documents matter. The **user-authored specification**
(`lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`, 161 lines)
is a session of assertions written at a Sage prompt: what the interface should
let a mathematician type. The **written specification**
(`lattices_written_spec_backup.py`, 2112 lines) is the class tree an agent
built from it, docstring-first, with the bodies partly filled.

## The stated theory

The written specification opens with its own definition, which is the thing to
compare against:

> Let $R$ be a Dedekind domain (usually assumed a PID). A bilinear $R$-module
> is a pair $(M, \beta)$ where $M$ is a finitely generated $R$-module
> $M \cong R^n$ and $\beta : M \otimes_R M \to R$ is a symmetric bilinear form.
> When $M$ is free and finitely generated, we refer to this as an
> $R$-lattice. When additionally $R = \mathbb Z$, we refer to this simply as
> a *lattice*.
>
> More correctly, we work in a category of triples $(M, \beta, B)$ where $B$
> is a fixed generating set of $M$.

and then states the divergence explicitly:

> NB: the category of lattices is NOT a subcategory of $\mathbb Z$-modules: it
> is a subcategory of a product category $R\text{-Mod} \times \mathrm{Bil}_R$,
> where $\mathrm{Bil}_R$ is the category of elements of
> $(M \otimes_R M)^{*} := \operatorname{Hom}_R(M \otimes_R M, R)$ as $M$ ranges
> over $R$-Mod.

**The preamble rejects this.** A formed module *is* a module that additionally
has a form, sited at `categories/modules/framed/formed/`, so the forgetful
functor to $R$-Mod is a functor out of a subcategory and not a projection out
of a product. The consequence is concrete: in the product-category reading, a
lattice must re-declare every module operation on the pair; in the preamble's
reading it inherits them, and only the form-consuming operations are new. The
triples $(M, \beta, B)$ with $B$ a chosen generating set are the preamble's
`Framed` axiom, and the specification's own qualifier "more correctly" is the
admission that the framing is structure, not an implementation convenience.

The specification's other definitional content agrees with the preamble and is
already owned: $\beta$ allowed $K$-valued gives the rational lattice, with
$K = \operatorname{Frac} R$; a torsion $M$ with $\beta$ valued in $K/R$ or
$K/2R$ gives the discriminant bilinear module, over $\mathbb Z$ the
discriminant form; a morphism of bilinear modules is an $R$-module morphism
with $\beta_1(v,w) = \beta_2(f v, f w)$, and an isomorphism is an isometry.

## Design rulings worth keeping

Four survive intact, and the preamble realizes all four:

1. **One site of promotion.** `RationalLattice.from_gram` is the single place
   a rational lattice becomes integral; `is_integral` is defined there and
   nowhere else. Kernels, images and cokernels promote to a lattice only when
   free, integral and nondegenerate, and otherwise land in the torsion or
   degenerate object.
2. **Morphisms only through hom sets.** `element_from_dict` and
   `element_from_matrix` on the hom space; isometry is checked by containment
   in the hom set, never by a flag on the matrix.
3. **A perp is relative to an inclusion.** $S^{\perp}$ is a question about the
   monomorphism $S \hookrightarrow L$, not about $S$.
4. **A span is not an external direct sum.** In the user specification,
   `e.span() + f.span()` forces the off-diagonal entries to zero and is
   degenerate, while `L.span([e, f])` is $U$ itself; the two are asserted
   unequal. This is the distinction the preamble carries as the difference
   between a subobject of $L$ and an orthogonal direct sum.

## What the specification asked for that now exists

The user specification's calls resolve on the preamble, under the preamble's
names: `L.O()`/`L.Aut()`, isometries built from generator images, involutions
and their orders, the invariant/coinvariant pair with
$L^{G\perp} = L_G$, inclusion index, primitivity from the cokernel being
torsion-free, reflections in non-isotropic vectors, `roots`, the isotropic
reduction $e^{\perp}/e$ with its promotion back to a lattice, divisibility
(`div`, on both the lattice and its elements), the Coxeter diagram, the
positive cone and $O^{+}$, and base change to $\mathbb Z_p$.

Nikulin's $(r, a, \delta)$ is owned in its parts and not as a triple:
`rank`, the discriminant group's length, and `delta` — which the preamble
computes as the negation of `is_coeven`, the field's word for what the
specification called *coparity*. There is no `nikulin_invariants` accessor and
no need for one; the triple is the three owned quantities.

## What it asked for that does not exist

- `L.hyperbolic_space()`, `L.coxeter_polytope()`, `positive_cone()` as an
  object of a category of cones with a Hilbert basis — the specification's own
  last lines mark these `TODO`, and the preamble has no cone or hyperbolic-space
  category either. The related note is
  `notes/computations/fundamental-chamber-as-root-halfspace-cone.md`.
- The algebraic-geometry noun layer (`varieties.py`, 879 lines: varieties,
  divisors with the Cartier/Weil/ample/nef/big predicates and intersection
  numbers, Picard groups with `as_lattice()`, linear systems, blowups with
  their exceptional divisors, branched covers with Riemann–Hurwitz, coherent
  sheaves, families with a Picard–Fuchs operator). The preamble's
  `categories/schemes/` and `categories/divisors/` nodes are thin. The
  requirement suite written against this layer is
  `computations/scripts/lattice-research/specs/variety_spec/`.

## Superseded outright

`presentations.py` validates a presentation with Pydantic models — square
symmetric Gram matrix, nondegeneracy, matching generator counts, form-preserving
morphism matrices. The preamble states the same requirements as
`abstract_method`s on the category and checks them in the obligations sweep, so
the validator layer has no residue.

`src/sage_patches/` installed the module, ideal, quotient and `End`/`Aut`
capabilities by `setattr` onto Sage's own classes. Owned categories plus
override-refine replace it, and the practice is banned.
