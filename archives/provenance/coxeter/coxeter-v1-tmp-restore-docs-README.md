<!--
Origin: gitclones/Coxeter/tmp_restore/docs/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Documentation Directory

## Essential Documents

### [OVERVIEW.md](OVERVIEW.md)
**Start here** - Project summary, mathematical background, current status, and getting started guide.

### [MATHEMATICAL_THEORY.md](MATHEMATICAL_THEORY.md)
Complete mathematical foundations: indefinite quadratic forms, Coxeter classification, subdiagram theory, and field requirements.

### [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)
Development patterns: AlgebraicLattice design, algorithm selection, testing strategies, and common pitfalls.

### [API_REFERENCE.md](API_REFERENCE.md)
Complete API specification: factory functions, core interfaces, specialized types, and SageMath integration.

### [REQUIREMENTS.md](REQUIREMENTS.md)
Technical requirements: exact arithmetic, categorical framework, field extensions, and quality standards.

### [TESTING.md](TESTING.md)
Comprehensive testing strategy: mathematical validation, cross-checking, and framework details.

## Project Conventions

### [../CONVENTIONS.md](../CONVENTIONS.md)
**Essential reading** - All mathematical and coding conventions including construction patterns, Sage integration, and critical distinctions (Gram vs Cartan matrices).

## Specialized Documentation

### [api/ALGORITHMS.md](api/ALGORITHMS.md)
Algorithm specifications with indefinite lattice focus.

### [api/TODO.md](api/TODO.md)
Mathematical research directions and implementation tasks.

### [api/interfaces/](api/interfaces/)
Detailed hierarchical interface specifications.

## Quick Start

**For Implementers**: OVERVIEW.md → CONVENTIONS.md → API_REFERENCE.md → IMPLEMENTATION_GUIDE.md

**For Mathematicians**: OVERVIEW.md → MATHEMATICAL_THEORY.md → CONVENTIONS.md → api/TODO.md

**For Users**: Natural algebraic notation example:
```python
U = AlgebraicLattice(['e', 'f'], bilinear_form={('e','f'): 1})
e, f = U.e, U.f
result = (2*e + 3*f) * (e - f)  # → -5
```