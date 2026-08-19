<!--
Origin: gitclones/Coxeter/implementation/planning/MIGRATION_CHECKLIST.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Migration Checklist: modules_bak → modules

Files to migrate from modules_bak to the new scaffold structure.

## Source Files Inventory

```
modules_bak/
├── BilRMod/
│   ├── BilRMod_category.md
│   ├── BilRMod_elements.md  
│   ├── BilRMod_factory.md
│   ├── BilRMod_morphisms.md
│   ├── BilRMod_objects.md
│   ├── BilRMod_subcategories.md
│   └── subcategories/
│       ├── alternating/
│       ├── degenerate/
│       ├── nondegenerate/
│       ├── skew_symmetric/
│       └── symmetric/
├── RMod/
│   ├── lattices/
│   │   ├── coxeter_lattices/
│   │   ├── hyperbolic_lattices/
│   │   └── root_lattices/
│   ├── RMod_category.md
│   ├── RMod_elements.md
│   ├── RMod_factory.md
│   ├── RMod_morphisms.md
│   ├── RMod_objects.md
│   └── subcategories/
│       ├── free/
│       ├── finitely_generated/
│       └── with_basis/
└── SymmetricBilRMod/
    ├── subcategories/
    │   ├── definite/
    │   ├── hyperbolic/
    │   ├── indefinite/
    │   └── parabolic/
    ├── SymmetricBilRMod_category.md
    ├── SymmetricBilRMod_elements.md
    ├── SymmetricBilRMod_factory.md
    ├── SymmetricBilRMod_morphisms.md
    └── SymmetricBilRMod_objects.md
```

## Migration Plan

### 1. RMod Category (Priority: High)

**Source**: `modules_bak/RMod/RMod_*.md`
**Target**: `modules/RMod/`

- [ ] `RMod_category.md` → `RMod_category.md` (merge with scaffold)
- [ ] `RMod_objects.md` → `RMod_objects.md` (merge with scaffold) 
- [ ] `RMod_elements.md` → `RMod_elements.md` (create new file)
- [ ] `RMod_morphisms.md` → `RMod_homs.md` (merge with scaffold)
- [ ] `RMod_factory.md` → `RMod_constructions.md` (merge with scaffold)

**Subcategories**:
- [ ] `subcategories/free/` → `RMod_subcategories.md` (section: Free)
- [ ] `subcategories/finitely_generated/` → `RMod_subcategories.md` (section: FinitelyGenerated)
- [ ] `subcategories/with_basis/` → `RMod_subcategories.md` (section: WithBasis)

**Lattice specializations**:
- [ ] `lattices/root_lattices/` → `RMod/subcategories/root_lattices/` (create new structure)
- [ ] `lattices/coxeter_lattices/` → `RMod/subcategories/coxeter_lattices/` (create new structure)  
- [ ] `lattices/hyperbolic_lattices/` → `RMod/subcategories/hyperbolic_lattices/` (create new structure)

### 2. BilRMod Category (Priority: High)

**Source**: `modules_bak/BilRMod/BilRMod_*.md`
**Target**: `modules/BilRMod/` (create scaffold first)

- [ ] Create BilRMod scaffold (copy RMod pattern)
- [ ] `BilRMod_category.md` → `BilRMod_category.md`
- [ ] `BilRMod_objects.md` → `BilRMod_objects.md`
- [ ] `BilRMod_elements.md` → `BilRMod_elements.md`
- [ ] `BilRMod_morphisms.md` → `BilRMod_homs.md`
- [ ] `BilRMod_factory.md` → `BilRMod_constructions.md`
- [ ] `BilRMod_subcategories.md` → `BilRMod_subcategories.md`

**Subcategories** (complex hierarchy):
- [ ] `subcategories/symmetric/` → `BilRMod/subcategories/symmetric/`
- [ ] `subcategories/skew_symmetric/` → `BilRMod/subcategories/skew_symmetric/`
- [ ] `subcategories/alternating/` → `BilRMod/subcategories/alternating/`
- [ ] `subcategories/degenerate/` → `BilRMod/subcategories/degenerate/`
- [ ] `subcategories/nondegenerate/` → `BilRMod/subcategories/nondegenerate/`

### 3. SymmetricBilRMod Category (Priority: Medium)

**Source**: `modules_bak/SymmetricBilRMod/SymmetricBilRMod_*.md`
**Target**: `modules/SymmetricBilRMod/` (create scaffold first)

- [ ] Create SymmetricBilRMod scaffold
- [ ] `SymmetricBilRMod_category.md` → `SymmetricBilRMod_category.md`
- [ ] `SymmetricBilRMod_objects.md` → `SymmetricBilRMod_objects.md`
- [ ] `SymmetricBilRMod_elements.md` → `SymmetricBilRMod_elements.md`
- [ ] `SymmetricBilRMod_morphisms.md` → `SymmetricBilRMod_homs.md`
- [ ] `SymmetricBilRMod_factory.md` → `SymmetricBilRMod_constructions.md`

**Subcategories** (signature-based):
- [ ] `subcategories/definite/` → `subcategories/definite/`
- [ ] `subcategories/indefinite/` → `subcategories/indefinite/`
- [ ] `subcategories/hyperbolic/` → `subcategories/hyperbolic/`
- [ ] `subcategories/parabolic/` → `subcategories/parabolic/`

## Migration Strategy

### Phase 1: Core Categories (Week 1)
1. **RMod** - Foundation category, start here
2. **BilRMod** - Build on RMod concepts
3. Verify scaffold structure works with real content

### Phase 2: Specialized Categories (Week 2)  
4. **SymmetricBilRMod** - Most complex hierarchy
5. Deep subcategory structures

### Phase 3: Integration (Week 3)
6. Cross-category consistency checks
7. Update category relationships  
8. Integration testing

## Content Merging Guidelines

### For Scaffold Files (Already Created)
- **PRESERVE** scaffold structure and organization
- **MERGE** content from modules_bak into appropriate sections
- **RESOLVE** conflicts by favoring mathematical correctness

### For New Files (Elements)
- **EXTRACT** from modules_bak source files
- **ORGANIZE** into new structure
- **MAINTAIN** consistency with scaffold patterns

### For Complex Hierarchies (Subcategories)
- **MAP** old hierarchy to new structure
- **FLATTEN** where appropriate for maintainability  
- **PRESERVE** mathematical relationships

## Validation Checkpoints

After each category migration:
- [ ] Files follow naming convention
- [ ] Cross-references work correctly
- [ ] Mathematical relationships preserved
- [ ] No orphaned content in modules_bak
- [ ] Scaffold structure integrity maintained

## Notes

- **NEVER** overwrite scaffold files completely - always merge
- **PRESERVE** all mathematical content - no content loss
- **MAINTAIN** docstring format and structure
- **ENSURE** backwards compatibility where possible
- Priority order reflects category dependency structure