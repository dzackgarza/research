# Knuth–Bendix on a finitely presented category: the 2-polygraph encoding

Research code migrated 2026-08-20 from
`gitclones/integral_lattice/cat/src/partial_implementation_bases/kbmag_implementation.py`
(PLAN-corpora-audit-registry, section R4). The surrounding n-category design
corpus is at `notes/category-design/n-category-tower/`; this directory holds
the one piece of that corpus that is an *algorithm* rather than a
specification.

## What it is

A finitely presented category — a 2-polygraph: a set of 0-cells, generating
1-cells between them, and 2-cells declaring equalities between composites —
has an undecidable word problem in general. This encoding makes equality of
composites decidable **in the cases Knuth–Bendix completion terminates**, by
translating the category into a monoid with zero and completing its
presentation into a confluent rewriting system:

- one idempotent generator `e_x` per 0-cell (the identity 1-cell at `x`),
  with `e_x e_x = e_x`;
- one absorbing element `z`, with `z w = w z = z` — the value of every
  *non-composable* product, so partial composition becomes total;
- one generator per generating 1-cell `f: x → y`, with the typing relations
  `e_x f = f`, `f e_y = f`, and `e_{x'} f = f e_{y'} = z` for wrong
  endpoints (words are read left to right along paths);
- one relation `source-word = target-word` per generating 2-cell.

The quotient monoid's nonzero elements are exactly the composable paths up
to the 2-cells, i.e. the morphisms of the presented category plus the
identities. GAP's KBMAG package (loaded through Sage's `libgap`) runs
Knuth–Bendix completion under shortlex; when completion terminates, reduced
words are normal forms, and:

- **equality of 1-cells** is equality of the normal forms of their
  composite words;
- **isomorphism of 0-cells** is the existence of generating cells
  `f: x → y`, `g: y → x` with `gf` reducing to `e_x` and `fg` to `e_y`.

The decidability boundary is honest: Knuth–Bendix need not terminate, and
where it does not, the procedure gives no answer — the source's own
`README`-level framing and this repo's undecidability audit agree that no
boolean method may paper over that.

## Provenance of the method

The monoid-with-zero encoding of a small category (identities as
idempotents, an absorbing zero totalizing partial composition) is the
standard passage from a category presentation to a monoid presentation;
the completion engine is GAP's KBMAG
(gap-packages.github.io/kbmag, cited in the source header). The polygraph
reading — generating cells at each dimension, 2-cells as rewriting rules —
is the design language of the surrounding corpus
(`notes/category-design/n-category-tower/docs/`, and `newcat2.md` there).

## Recorded defects in the migrated source (kept unmodified)

- `get_one_cells_between` compares the *methods* `w.source_raw_cell` /
  `w.target_raw_cell` against cells instead of calling them, so it returns
  no cells and `are_equivalent_zero_cells` can answer `False` for
  isomorphic 0-cells. The fix is the two call parentheses; the file is kept
  as it arrived, defect recorded here.
- `are_equivalent_two_cells` ignores the rewriting system: it declares two
  2-cells equivalent exactly when their boundaries agree, which is the
  posetal (at-most-one-2-cell) special case, not a computation.
- `are_equivalent_one_cells` and `are_equivalent_zero_cells` rebuild the
  rewriting system on every call; completion is the expensive step and the
  system depends only on the presentation, so one build per presentation is
  the correct shape.
- The file imports `src._types` and `src.abc_specs.cells` from the source
  corpus's own package layout; those specification files live in the design
  corpus at `notes/category-design/n-category-tower/src/`, so this module
  is reference research code, not an importable library.

## Relation to the preamble

The preamble decides morphism equality on framed module categories through
the equalizer (`module_morphisms.sage`, `ModuleMorphism.equalizer`) — there
the framing decides. This encoding is the tool for the *presented-category*
regime the preamble does not own, and it is a candidate engine seam for a
future `categories/abstract_categories/` finitely-presented-category node
(candidacy recorded in `notes/category-design/n-category-tower/INDEX.md`).
