<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Coxeter Group Theory: Computational Framework and Research Environment

A dual-purpose mathematical framework combining rigorous research infrastructure with practical computational tools for Coxeter group theory, maximal parabolic classification, and indefinite quadratic forms.

## Project Architecture: Research + Implementation

This project maintains two complementary environments:

### 🔬 **Research Environment** → [`research/`](research/)
**Pure mathematical research and theoretical development**
- Mathematical foundations and theoretical framework
- Literature collection and scholarly resources  
- Open research questions and ongoing investigations
- Academic-grade documentation and citations

### ⚙️ **Implementation Environment** → [`implementation/`](implementation/)
**Agent-driven software development with mathematical rigor**
- TDD-based development workflows with anti-gaming measures
- API specifications and algorithmic implementations
- Mathematical conventions that prevent agent errors
- Practical computational tools and validation systems

## Quick Navigation

### For Mathematical Researchers
**Start here**: [`research/README.md`](research/README.md) - Comprehensive research environment
- [`research/foundations/`](research/foundations/) - Core mathematical theory
- [`research/explorations/`](research/explorations/) - Active research investigations  
- [`research/literature/`](research/literature/) - Curated academic resources

### For Software Developers and Implementing Agents
**Start here**: [`implementation/README.md`](implementation/README.md) - Development environment
- **Critical**: [`implementation/conventions/CONVENTIONS.md`](implementation/conventions/CONVENTIONS.md) - Mathematical definitions agents must follow
- [`implementation/planning/`](implementation/planning/) - Complete API specifications and algorithms
- [`implementation/tools/`](implementation/tools/) - Development tools and agent configurations

## Core Mathematical Focus

**Coxeter Groups and Maximal Parabolic Classification**:
- Indefinite quadratic forms over arbitrary fields
- Hyperbolic reflection groups and finite covolume criteria
- Exact arithmetic computational methods
- Systematic enumeration of maximal parabolic subdiagrams

**Theoretical Framework**:
- Category-theoretic treatment of bilinear modules
- Signature-based classification of indefinite lattices
- Field extension requirements for non-crystallographic types
- Connection to algebraic topology and geometric group theory

## Research Contributions

This project advances several areas of mathematics:

1. **Computational Coxeter Theory**: Efficient algorithms for maximal parabolic enumeration
2. **Mathematical Software**: Exact arithmetic implementations with rigorous validation
3. **Theoretical Development**: Modern categorical framework for classical Coxeter theory
4. **Literature Integration**: Systematic organization of scattered theoretical results

## Development Philosophy

**Research-Implementation Synergy**:
- Mathematical theory guides computational design
- Implementation validates theoretical predictions
- Research questions drive feature development
- Academic rigor maintained throughout development process

**Quality Standards**:
- Exact arithmetic (no floating-point approximations)
- Property-based testing prevents gaming
- Literature validation for all results
- Comprehensive mathematical documentation

## Getting Started

### 1. Choose Your Path

**Research Focus**: Start with [`research/README.md`](research/README.md)
- Understand mathematical foundations
- Explore open questions and research directions
- Access curated literature and references

**Development Focus**: Start with [`implementation/README.md`](implementation/README.md)
- Review critical mathematical conventions
- Study API specifications and development workflows
- Set up TDD environment with anti-gaming measures

### 2. Essential Reading

**For Everyone**:
- [`research/foundations/mathematical-theory.md`](research/foundations/mathematical-theory.md) - Core mathematical framework
- [`implementation/conventions/CONVENTIONS.md`](implementation/conventions/CONVENTIONS.md) - Critical definitions

**For Researchers**:
- [`research/explorations/open-questions.md`](research/explorations/open-questions.md) - Current research challenges
- [`research/literature/BIBLIOGRAPHY.md`](research/literature/BIBLIOGRAPHY.md) - Comprehensive literature collection

**For Developers**:
- [`implementation/planning/TODO.md`](implementation/planning/TODO.md) - Implementation roadmap
- [`implementation/planning/ALGORITHMS.md`](implementation/planning/ALGORITHMS.md) - Algorithm specifications

### 3. Development Setup

```bash
# Clone repository
git clone [repository-url]
cd Coxeter

# Install dependencies
pip install -r requirements.txt

# Run comprehensive test suite
pytest tests/

# For SageMath integration
sage -python setup.py install
```

## Project Structure

```
Coxeter/
├── README.md                   # This file - project overview
├── research/                   # 🔬 Mathematical research environment
│   ├── foundations/           # Core mathematical theory
│   ├── explorations/          # Active research investigations
│   └── literature/            # Academic literature collection
├── implementation/            # ⚙️ Software development environment  
│   ├── conventions/           # Mathematical definitions for agents
│   ├── planning/              # API specifications and algorithms
│   ├── tools/                 # Development and validation tools
│   └── src/                   # Source code implementation
├── docs/                      # Additional documentation
├── tests/                     # Comprehensive test suite
└── src/                       # Main source code
```

## Research Environment Highlights

**Mathematical Foundations**: Comprehensive treatment of indefinite quadratic forms, Coxeter group theory, and geometric group theory applications.

**Open Research**: Active investigation of computational complexity, Galois theory applications, and connections to modern homotopy theory.

**Literature Integration**: Systematic collection of academic papers, Wikipedia articles, and reference materials with proper citation management.

## Implementation Environment Highlights

**Agent-Driven Development**: Specialized TDD agents with anti-gaming measures ensure mathematical correctness while enabling efficient development.

**Mathematical Rigor**: Exact arithmetic throughout, with comprehensive validation against literature examples and theoretical predictions.

**Modular Architecture**: Category-theoretic design enables systematic extension to new mathematical structures while maintaining correctness.

## Contributing

### Research Contributions
- Add findings to [`research/explorations/research-notes.md`](research/explorations/research-notes.md)
- Contribute literature with proper citations
- Propose new research directions in open questions
- Document experimental results and computational investigations

### Implementation Contributions
**Essential Workflow**:
1. **Read mathematical conventions** - [`implementation/conventions/CONVENTIONS.md`](implementation/conventions/CONVENTIONS.md)
2. **Study relevant specifications** - [`implementation/planning/`](implementation/planning/)
3. **Follow TDD workflow** with property-based testing
4. **Ensure exact arithmetic** and mathematical correctness
5. **Validate against literature** examples

## Academic Integration

**Publication Target**: Results suitable for academic publication in computational mathematics, group theory, and mathematical software journals.

**SageMath Integration**: Designed for eventual integration into SageMath's official codebase with full compatibility.

**Reproducible Research**: All computational results reproducible with detailed documentation and version control.

---

**Mission**: Advance the theoretical understanding and computational capabilities for Coxeter group theory while maintaining the highest standards of mathematical rigor and software quality.

**Vision**: Create a comprehensive framework that serves both pure mathematical research and practical computational applications, contributing meaningfully to both the academic literature and the broader mathematical software ecosystem.