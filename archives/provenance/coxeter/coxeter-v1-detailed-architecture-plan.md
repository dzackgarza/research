<!--
Origin: gitclones/Coxeter/tmp_restore/detailed-architecture-plan.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Documentation Architecture Plan: Coxeter Project

## Executive Summary

**Objective**: Transition from comprehensive api-planning documentation to streamlined, just-in-time architecture supporting immediate implementation needs.

**Key Principle**: Preserve mathematical ground truth while minimizing cognitive overhead for implementing agents.

## Current State Assessment

### Ground Truth (PRESERVE AS-IS)
- **`docs/api-planning/`**: 43 files, 180KB+ of precise mathematical specifications
- **`CONVENTIONS.md`**: Recently created, agent-critical conventions
- **`research/`**: 25+ files of mathematical foundations and bibliography

### Outdated/Redundant Content (ARCHIVE)
- **`docs/OVERVIEW.md`**: Superseded by api-planning
- **`docs/MATHEMATICAL_THEORY.md`**: Duplicates research/ content
- **`docs/IMPLEMENTATION_GUIDE.md`**: Premature, implementation not started
- **`docs/REQUIREMENTS.md`**: Captured in api-planning specifications
- **`docs/TESTING.md`**: Generic, needs api-planning integration

### Agent-Critical Content (TOP-LEVEL)
- **`CONVENTIONS.md`**: Mathematical and implementation conventions
- **`docs/README.md`**: Navigation hub (needs updating)

## New Directory Structure

```
/
├── CONVENTIONS.md                     # Mathematical/implementation conventions (ESSENTIAL)
├── README.md                          # Project overview with quick navigation
├── Justfile                          # Build automation
│
├── docs/
│   ├── README.md                     # Updated navigation hub
│   ├── api-planning/                 # GROUND TRUTH - preserve exactly as-is
│   │   ├── ALGORITHMS.md
│   │   ├── BILINEAR_FORMS_MATHEMATICAL_NOTES.md
│   │   ├── TODO.md
│   │   └── [40+ specification files...]
│   │
│   └── reference/                    # Consolidated reference materials
│       ├── mathematical-theory.md    # Consolidated from multiple sources
│       ├── implementation-patterns.md # Future: co-locate with src/
│       └── testing-strategy.md       # Future: co-locate with tests/
│
├── research/                         # Mathematical foundations (preserve)
│   ├── BIBLIOGRAPHY.md
│   ├── papers/
│   ├── sources/
│   └── [existing structure...]
│
├── src/                              # FUTURE: Implementation with co-located docs
│   ├── categories/                   # (exists, empty)
│   ├── lattices/                     # Future: lattice/*.py + lattice/README.md
│   ├── algorithms/                   # Future: algorithm/*.py + algorithm/README.md
│   └── [future modules with embedded docs]
│
├── tests/                            # Test framework (preserve)
│
└── archive/                          # Moved content + historical versions
    ├── 2025-01-27-docs-restructure/  # This migration snapshot
    │   ├── OVERVIEW.md
    │   ├── MATHEMATICAL_THEORY.md
    │   ├── IMPLEMENTATION_GUIDE.md
    │   ├── REQUIREMENTS.md
    │   ├── TESTING.md
    │   └── COMPREHENSIVE_ERROR_CORRECTIONS.md
    ├── homotopy_theory/               # (existing)
    └── src/                           # (existing archived code)
```

## Content Migration Plan

### Phase 1: Archive Redundant Documentation
**Goal**: Move outdated docs to archive, preserve all content

| Source File | Destination | Rationale |
|-------------|-------------|-----------|
| `docs/OVERVIEW.md` | `archive/2025-01-27-docs-restructure/OVERVIEW.md` | Superseded by api-planning |
| `docs/MATHEMATICAL_THEORY.md` | `archive/2025-01-27-docs-restructure/MATHEMATICAL_THEORY.md` | Duplicates research/ content |
| `docs/IMPLEMENTATION_GUIDE.md` | `archive/2025-01-27-docs-restructure/IMPLEMENTATION_GUIDE.md` | Premature, no implementation yet |
| `docs/REQUIREMENTS.md` | `archive/2025-01-27-docs-restructure/REQUIREMENTS.md` | Captured in api-planning |
| `docs/TESTING.md` | `archive/2025-01-27-docs-restructure/TESTING.md` | Needs api-planning integration |
| `docs/COMPREHENSIVE_ERROR_CORRECTIONS.md` | `archive/2025-01-27-docs-restructure/COMPREHENSIVE_ERROR_CORRECTIONS.md` | Historical debugging notes |
| `docs/REPEATED_MISTAKE_PATTERNS.md` | `archive/2025-01-27-docs-restructure/REPEATED_MISTAKE_PATTERNS.md` | Historical debugging notes |

### Phase 2: Create Reference Consolidation
**Goal**: Create focused reference documents from archived content

**New Files to Create**:
1. **`docs/reference/mathematical-theory.md`**
   - Consolidate core mathematical concepts from archived files
   - Link to detailed specifications in api-planning/
   - Focus on theory agents need during implementation

2. **`docs/reference/implementation-patterns.md`** (Future)
   - Will be created during src/ implementation
   - Co-located with actual implementation modules
   - Just-in-time documentation philosophy

3. **`docs/reference/testing-strategy.md`** (Future)
   - Integrate api-planning mathematical validation requirements
   - Co-located with tests/ structure
   - TDD integration with mathematical properties

### Phase 3: Update Navigation
**Goal**: Update docs/README.md for new structure

**New Navigation Structure**:
```markdown
# Documentation Hub

## Essential (Start Here)
- [CONVENTIONS.md](../CONVENTIONS.md) - Mathematical and implementation conventions
- [api-planning/](api-planning/) - Complete API specifications (GROUND TRUTH)

## Implementation Phase
- [reference/](reference/) - Consolidated theory and patterns
- [../src/](../src/) - Implementation with co-located documentation (future)

## Research Foundation
- [../research/](../research/) - Mathematical bibliography and sources

## Quick Paths
- **Implementing Agent**: CONVENTIONS.md → api-planning/BILINEAR_FORMS_MATHEMATICAL_NOTES.md
- **Mathematics Review**: reference/mathematical-theory.md → research/
- **API Reference**: api-planning/ (complete specifications)
```

## File-by-File Migration Mapping

```bash
# Phase 1 Moves (Archive)
docs/OVERVIEW.md → archive/2025-01-27-docs-restructure/OVERVIEW.md
docs/MATHEMATICAL_THEORY.md → archive/2025-01-27-docs-restructure/MATHEMATICAL_THEORY.md
docs/IMPLEMENTATION_GUIDE.md → archive/2025-01-27-docs-restructure/IMPLEMENTATION_GUIDE.md
docs/REQUIREMENTS.md → archive/2025-01-27-docs-restructure/REQUIREMENTS.md
docs/TESTING.md → archive/2025-01-27-docs-restructure/TESTING.md
docs/COMPREHENSIVE_ERROR_CORRECTIONS.md → archive/2025-01-27-docs-restructure/COMPREHENSIVE_ERROR_CORRECTIONS.md
docs/REPEATED_MISTAKE_PATTERNS.md → archive/2025-01-27-docs-restructure/REPEATED_MISTAKE_PATTERNS.md

# Phase 2 Creates (Reference)
[CREATE] docs/reference/mathematical-theory.md (consolidate from archived content)

# Phase 3 Updates (Navigation)
[UPDATE] docs/README.md (new navigation structure)
[UPDATE] README.md (project-level navigation update)

# Preserve As-Is
docs/api-planning/ (NO CHANGES - this is ground truth)
research/ (NO CHANGES - mathematical foundation)
CONVENTIONS.md (NO CHANGES - recently created, essential)
```

## Implementation Phases

### Phase 1: Safe Archive Migration (Zero Risk)
**Duration**: 1 hour
**Validation**: All files moved to archive, no deletions

```bash
# Create archive directory
mkdir -p archive/2025-01-27-docs-restructure

# Move files (preserving all content)
mv docs/OVERVIEW.md archive/2025-01-27-docs-restructure/
mv docs/MATHEMATICAL_THEORY.md archive/2025-01-27-docs-restructure/
mv docs/IMPLEMENTATION_GUIDE.md archive/2025-01-27-docs-restructure/
mv docs/REQUIREMENTS.md archive/2025-01-27-docs-restructure/
mv docs/TESTING.md archive/2025-01-27-docs-restructure/
mv docs/COMPREHENSIVE_ERROR_CORRECTIONS.md archive/2025-01-27-docs-restructure/
mv docs/REPEATED_MISTAKE_PATTERNS.md archive/2025-01-27-docs-restructure/

# Validation checkpoint
find archive/2025-01-27-docs-restructure/ -type f | wc -l  # Should be 7
```

### Phase 2: Reference Consolidation (Low Risk)
**Duration**: 2 hours
**Validation**: New reference files created, no dependencies broken

```bash
# Create reference directory
mkdir -p docs/reference

# Create consolidated mathematical theory (extract from archived files)
# Focus on implementation-relevant theory
```

### Phase 3: Navigation Update (Medium Risk)
**Duration**: 1 hour
**Validation**: All links functional, clear navigation paths

```bash
# Update navigation files
# Ensure all links point to correct locations
# Test all navigation paths
```

## Validation Checkpoints

### Checkpoint 1: Content Preservation
- [ ] All 7 files successfully moved to archive
- [ ] Archive directory contains exactly 7 files
- [ ] No content deleted from project
- [ ] api-planning/ unchanged (diff check)

### Checkpoint 2: Reference Quality
- [ ] mathematical-theory.md covers core concepts from archived files
- [ ] References to api-planning/ for detailed specifications
- [ ] No duplicate content between reference/ and api-planning/
- [ ] Clear implementation guidance

### Checkpoint 3: Navigation Functionality
- [ ] All links in docs/README.md functional
- [ ] Clear agent workflow paths defined
- [ ] Project README.md updated for new structure
- [ ] Quick reference paths tested

## Rollback Procedures

### Emergency Rollback (Phase 1)
```bash
# Restore all archived files
mv archive/2025-01-27-docs-restructure/* docs/
rmdir archive/2025-01-27-docs-restructure/
```

### Partial Rollback (Phase 2)
```bash
# Remove reference directory if needed
rm -rf docs/reference/
# Files already safely in archive
```

### Navigation Rollback (Phase 3)
```bash
# Git restore navigation files
git checkout HEAD -- docs/README.md README.md
```

## Future Implementation Co-location Strategy

When `src/` implementation begins:

### Module-Level Documentation
```
src/lattices/
├── __init__.py
├── lattice.py
├── lattice_element.py
├── README.md              # Module-specific documentation
├── examples.md            # Usage examples
└── algorithms/
    ├── __init__.py
    ├── eigenvalue_analysis.py
    ├── README.md          # Algorithm-specific docs
    └── examples/          # Worked examples
```

### Test-Level Documentation
```
tests/lattices/
├── test_lattice.py
├── test_lattice_element.py
├── README.md              # Test strategy for this module
└── fixtures/
    ├── test_data.py
    └── examples.md        # Test case documentation
```

## Success Metrics

1. **Agent Efficiency**: Agents find essential information within 2 documentation files
2. **Zero Data Loss**: All content preserved in archive
3. **Clear Navigation**: 3-step max path to any required information
4. **Maintainability**: Future src/ co-location strategy defined
5. **Ground Truth Preservation**: api-planning/ remains the authoritative source

## Risk Assessment

### Low Risk
- **Content archival**: Simple file moves, no deletions
- **Reference creation**: New files, no dependencies affected
- **api-planning preservation**: No changes to ground truth

### Medium Risk
- **Navigation updates**: Link breakage possible but easily fixable
- **Agent workflow disruption**: Minimal impact due to preservation of essential files

### Mitigation
- **Complete backup**: Git commit before any changes
- **Incremental validation**: Checkpoint after each phase
- **Rollback procedures**: Documented recovery for each phase

## Conclusion

This architecture plan transforms the Coxeter project documentation from comprehensive but overwhelming to streamlined and implementation-focused, while preserving all mathematical ground truth and providing clear pathways for future co-located documentation during the implementation phase.

The key innovation is the strict separation between:
1. **Ground Truth** (api-planning/): Complete, authoritative specifications
2. **Agent Essentials** (CONVENTIONS.md): Critical implementation guidance  
3. **Reference** (docs/reference/): Consolidated, focused guidance
4. **Research Foundation** (research/): Mathematical underpinnings

This structure supports efficient agent workflows while maintaining mathematical rigor and complete traceability to source material.