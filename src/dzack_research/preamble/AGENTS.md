# Preamble mathematical boundaries

These rules apply to `src/dzack_research/preamble/`.

## Mathematics controls the API

- Use standard mathematical objects and names.
- Separate an object from each chosen presentation of that object.
- Do not infer mathematical identity from a shared software representation.
- Treat Sage behavior as implementation evidence. Do not treat it as a definition.
- Refine objects into preamble-owned categories. Do not expose wrapper identity as public mathematics.

## Maps and matrices

- A morphism is not a matrix.
- A `MorphismMatrix` records a morphism after a choice of module generators.
- A Gram matrix records form values after a choice of module generators.
- Equal numerical matrices do not make these roles equal.
- A normal form returns a presented object and an isomorphism. It does not return only a matrix.

## Generators

- Name the structure that generators generate.
- Use names such as `module_generators`, `group_generators`, and `algebra_generators`.
- Separate abstract generators from their images under an embedding.
- Do not use supplied generators as a substitute for a canonical group.

## Functors

Before you define a functor, state all four data:

- source category;
- target category;
- action on objects;
- action on morphisms.

An object constructor alone is not a functor.

## Definedness and computation

- Separate mathematical definedness from algorithm availability.
- Never map an unknown result to `False`.
- Do not add boolean checks for general undecidable equality or equivalence problems.
- Use a known decision algorithm only on its stated domain.

## Correction reset

If a correction changes a type, map direction, quotient level, or hypothesis, discard dependent work. Re-derive it from definitions.

Treat a correction as evidence. Check it against sources before you adopt it.

Search project and global memory before you change these public surfaces:

```bash
agent-memory search --scope both "preamble categories matrices generators functors computability"
```
