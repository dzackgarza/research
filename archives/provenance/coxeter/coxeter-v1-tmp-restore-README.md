<!--
Origin: gitclones/Coxeter/tmp_restore/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Coxeter Maximal Parabolic Classification

A mathematical framework for computing root systems, Gram matrices, and classification of maximal parabolic subgroups using indefinite quadratic forms over arbitrary fields with exact arithmetic.

## Quick Start for Implementing Agents

### 🚨 **Start Here**: [CONVENTIONS.md](CONVENTIONS.md)
**Critical mathematical definitions agents frequently get wrong**
- Bilinear forms vs inner products distinction
- Gram vs Cartan matrix differences  
- Signature-based classification hierarchy
- Exact arithmetic requirements
- Orthogonality behavior patterns

### 📋 **Implementation Specifications**: [docs/api-planning/](docs/api-planning/)
**Ground truth for implementation (180KB+ of detailed specifications)**
- Complete category hierarchy with mathematical precision
- Interface specifications for all lattice types
- Algorithm requirements with indefinite lattice focus
- Mathematical constraints and validation rules
- TDD plans with property-based testing strategies

Key entry points:
- [categories.md](docs/api-planning/categories.md) - Complete type hierarchy
- [ALGORITHMS.md](docs/api-planning/ALGORITHMS.md) - Core computational methods
- [TODO.md](docs/api-planning/TODO.md) - Implementation roadmap

### 📚 **Mathematical Background**: [docs/reference/MATHEMATICAL_FOUNDATIONS.md](docs/reference/MATHEMATICAL_FOUNDATIONS.md)
**Deep mathematical theory for complex implementations**
- Indefinite quadratic forms over arbitrary fields
- Coxeter classification theory and subdiagram analysis
- Field extension requirements and computational strategies

## Current Status

**Phase**: Transition from api-planning → api-implementation
- ✅ Mathematical foundations established
- ✅ Complete category hierarchy specified  
- ✅ Critical conventions documented
- 🔄 Implementation phase starting

## Development Setup

```bash
# Clone and setup
git clone [repository]
cd Coxeter

# Install dependencies
pip install -r requirements.txt

# Run test suite
pytest tests/
```

## Contributing

**Essential workflow**: 
1. **Read [CONVENTIONS.md](CONVENTIONS.md)** - Prevents common mathematical errors
2. **Review relevant [api-planning](docs/api-planning/) specifications** 
3. **Follow exact arithmetic and typing requirements**
4. **Use property-based testing for mathematical properties**

## Project Structure

```
CONVENTIONS.md              # 🚨 Critical mathematical definitions
docs/api-planning/          # 📋 Complete implementation specifications  
docs/reference/            # 📚 Deep mathematical theory
src/                       # Implementation (future)
tests/                     # Comprehensive test suite
```

The mathematical precision of this framework requires careful attention to definitional subtleties. Start with CONVENTIONS.md to avoid implementing against incorrect mathematical assumptions.