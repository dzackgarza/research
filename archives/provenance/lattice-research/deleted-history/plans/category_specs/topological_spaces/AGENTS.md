# AGENTS.md — topological_spaces

GOAL: record topological-space and metric-space method surfaces as ABC specs on the
category of topological spaces.

This subtree owns the fact that a topological space is a set equipped with a topology.
Thus `Sets().Topological()` is the category of topological spaces, not a merely
set-local implementation detail. `Sets().Metric()` is the metric-space subcategory.

Tasks:
- Keep topological and metric method surfaces here.
- Let set, real-set, ring, module, and algebra categories refer to this subtree when
  their objects carry topology.
- Keep constructors separate from subcategories. Add concrete constructors only when a
  Sage topological-space constructor has been inventoried.
