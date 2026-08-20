# prior-art-hott — corpus INDEX

Two documents, landed 2026-08-20 from
`gitclones/Coxeter/research/explorations/implementation-notes/` under
`PLAN-coxeter-deletion-audit-registry` (reader H). Both read a formalized
category-theory library and ask what its design choices imply for a Sage
category tree.

- `lessons_from_coq_hott.md` — the Coq-HoTT `PreCategory` record: hom *types*
  indexed by the pair of objects rather than one morphism type with
  domain/codomain accessors; redundant symmetric forms of the laws;
  truncation levels tracked explicitly, so a hom-set is set-truncated by
  declaration. Then comma categories, functor categories, and adjunctions as
  that library builds them.
- `lessons_from_hott3.md` — the Lean 3 HoTT library, read for universal
  properties. A pullback is the structure $(x, y, p : f(x) = g(y))$ — the
  witness is part of the datum, not a side condition — and the universal
  property is an *equivalence* (`is_equiv` on the induced map) rather than
  existence plus uniqueness. Limits appear as Kan extensions along the map to
  the terminal category.

## Disposition against the preamble

Owned: slice categories, which are the comma-category special case
$\mathcal{C}/X$ — `categories/abstract_categories/slice_categories.sage`,
alongside `cat.sage`, `products.sage`, `arrow_categories.sage`.

Absent, and named here: general comma categories $(F \downarrow G)$; Kan
extensions, and with them limits-as-Kan-extensions; universal properties
with an explicit witness object rather than asserted of a construction.

The witness point is the one with in-repo consequences. The repository's
subobject model already works this way — a subobject *is* the monomorphism
$f : A \hookrightarrow B$, and questions like primitivity or index are asked
of $f$ — so `lessons_from_hott3.md` is the prior art for a doctrine the
preamble adopted independently, stated one level more generally than the
preamble states it.

## Errors recorded

None recorded against either file by the audit.
