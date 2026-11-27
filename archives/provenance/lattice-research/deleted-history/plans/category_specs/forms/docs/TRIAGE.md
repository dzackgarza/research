# Forms Triage

The first forms pass establishes ownership separation:

- Formed-module category classes now live in `forms/`.
- Module and lattice paths that previously hosted those classes now re-export the forms
  classes.
- `FormedModules(R)` names the forms owner while preserving `Modules(R).WithForms()`.
- `forms/smoketest.sage` checks owner identity through module and lattice compatibility
  paths.

Current deferred work:

- Axiom registration is still centralized in `axioms.py`; this pass does not split the
  registry by subtree.
- `IntegerLattices()` remains a module constructor-route surface until the lattice
  constructor pass moves it behind `Lattices(R).Constructors()`.
