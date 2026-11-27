# Cat Triage

Source for this pass: `cat/docs/SAGE_INVENTORY.md`, `cat/docs/MAPPING.md`,
installed Sage source under `sage/categories/`, official Sage documentation, and the
local smoke surface `cat/smoketest.sage`.

## Current Smoke Frontier

- Some subtree category classes already define direct `Hom` methods for their own
  object-level homset constructors. Those direct methods may shadow the Cat-level
  category-object `Hom` at runtime and should be reviewed in a later uniformization
  pass.
- Natural transformations are not modeled. The current Cat morphism surface is Sage
  functors and construction functors.
- The generic Sage functor API does not provide a uniform invertibility certificate.
  Concrete autofunctor membership beyond the generic aut-category condition remains a
  future refinement.

## Validation Scope

Run `sage cat/smoketest.sage` after layout and documentation edits are complete.
This smoke is structural. It checks Cat instantiation, category-object membership,
functor HomCategory instantiation, and standard construction navigation. It does not prove
that all other subtrees have completed the later uniformization refactor.
