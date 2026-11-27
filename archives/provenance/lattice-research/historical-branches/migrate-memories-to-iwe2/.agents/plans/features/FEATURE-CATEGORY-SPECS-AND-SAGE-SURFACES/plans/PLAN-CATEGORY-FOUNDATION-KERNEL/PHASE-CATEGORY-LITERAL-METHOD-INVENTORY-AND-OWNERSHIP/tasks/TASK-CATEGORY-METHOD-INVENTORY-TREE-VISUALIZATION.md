---
id: TASK-CATEGORY-METHOD-INVENTORY-TREE-VISUALIZATION
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY]]'
title: Visualize method-bearing category hierarchy as user-facing documentation
status: complete
priority: high
description: Build one tree/graph per top-level category showing the subcategory hierarchy,
  restricted to nodes that introduce a nontrivial method or override one. Output as
  Mermaid diagrams in `plans/visuals/`. This is user-facing documentation to help
  understand where nontrivial spec surfaces come from.
successCriteria:
- One Mermaid tree diagram exists per top-level category (cat, sets, rings, modules,
  algebras, lattices, forms, posets, topological_spaces, homsets, tensor_algebra_components)
- Each diagram shows the subcategory containment hierarchy
- Nodes are restricted to categories that introduce at least one nontrivial method
  or override a method from a supercategory (structural parent/constructor-only
  categories are elided)
- Each node shows the category name and a count of introduced methods
- Edges show subcategory containment (parent → child)
- Diagrams follow `plans/visuals/` conventions (Mermaid format, documented in README)
complexity: 65
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---

# Visualize Method-Bearing Category Hierarchy

Build a user-facing visualization of the category hierarchy across all
`category_specs/` top-level categories, restricted to nodes that actually
introduce nontrivial methods. The goal is to let a reader see at a glance
where the spec's method surface comes from — which categories carry
computational weight and which are purely structural.

## Procedure

### 1. Traverse the Category Tree

For each top-level category directory in `category_specs/`:

- `cat/` — Category of categories
- `sets/` — Sets
- `rings/` — Rings
- `modules/` — Modules
- `algebras/` — Algebras
- `lattices/` — Lattices
- `forms/` — Forms
- `posets/` — Posets
- `topological_spaces/` — Topological spaces
- `homsets/` — Hom/End/Aut categories
- `tensor_algebra_components/` — Tensor algebra components

For each, identify the subcategory containment graph:

- The root `__init__.py` defines the top-level category
- `subcategories/*.py` files define subcategories
- `subcategories/constructions/*.py` define construction-based subcategories
- Cross-cutting axioms in root `axioms.py` may attach to multiple top-level
  categories

### 2. Identify Method-Bearing Nodes

A node (category) qualifies for inclusion in the visualization if it:

- Defines an `ElementMethods` class with at least one public method (not
  starting with `_`)
- Defines methods directly on the category class itself
- Has a `homsets.py`, `endsets.py`, or `autsets.py` file with methods
- Overrides a method from a supercategory (even if the override just
  specializes the return type)

Exclude nodes that:

- Have no methods beyond `__init__`, Sage category boilerplate, or
  `_base_category_class_and_axiom` registration
- Are purely structural (exist only to organize subcategories in the
  containment graph)
- Are construction categories that merely route to Sage constructors
  without adding methods

### 3. Build the Diagrams

For each top-level category, produce a Mermaid `flowchart TD` or `graph TD`
diagram in `plans/visuals/`:

```
plans/visuals/
├── category-tree-sets.mmd
├── category-tree-rings.mmd
├── category-tree-modules.mmd
├── category-tree-algebras.mmd
├── category-tree-lattices.mmd
├── category-tree-forms.mmd
├── category-tree-posets.mmd
├── category-tree-topological-spaces.mmd
├── category-tree-cat.mmd
├── category-tree-homsets.mmd
├── category-tree-tensor-algebra-components.mmd
└── README.md (updated)
```

Each diagram node shows:

```
Sets().Finite()  [12 methods]
```

Where `12 methods` is the count of methods introduced at that node (not
inherited from supercategories). Methods overridden at this node should be
counted separately or noted with a marker (e.g., `+3 overridden`).

Edges show subcategory containment: `A --> B` means B is a subcategory of A.

### 4. Prune to Readability

The diagrams are user-facing documentation, not machine output:

- If a diagram would have more than ~30 nodes, consider grouping leaf
  subcategories that only differ by a single axiom into a collapsed
  representation
- If a category introduces zero nontrivial methods, elide it from the
  diagram (it's structural, not method-bearing)
- If a category introduces only 1-2 trivial methods (e.g., a single
  `__repr__` override), use a lighter visual treatment or a note
- Construction categories that are method-bearing should be shown as a
  group under their parent, not as full peers of axiom-based subcategories

### 5. Document Findings

Add entries to the `plans/visuals/README.md` explaining:

- What each diagram shows (which top-level category, what filtering was
  applied)
- What "nontrivial method" means for the purpose of this visualization
- Which categories were elided and why
- How to regenerate the diagrams when specs change

### 6. Cross-Reference

- Load `category-spec-visuals` for Mermaid diagram conventions before
  creating any diagram file.
- Load `category-spec-style` for category naming conventions — the
  node labels in diagrams must match the spec's vocabulary.
- The method inventory spec (`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`)
  is the canonical source for method ownership data. Cross-check diagram
  method counts against the spec.

## Non-Goals

- This task does NOT produce a machine-readable graph format (no DOT, no
  JSON export). Mermaid is the format.
- This task does NOT analyze method bodies or validate correctness. It
  only counts and categorizes method presence.
- This task does NOT produce a single unified graph. Separate per-category
  trees are more readable than one monolithic diagram.
