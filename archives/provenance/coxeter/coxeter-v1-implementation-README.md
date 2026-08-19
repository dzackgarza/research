<!--
Origin: gitclones/Coxeter/implementation/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Coxeter Implementation Environment

This directory contains the practical implementation infrastructure for the Coxeter maximal parabolic project, focusing on agent-driven development workflows, coding conventions, and computational tools.

## Overview

The implementation environment is organized to support systematic software development guided by Test-Driven Development (TDD) principles, with specialized agents for planning, testing, and implementation. It separates development methodology from theoretical research while maintaining mathematical rigor.

## Directory Structure

```
implementation/
├── README.md                    # This file - implementation environment overview
├── conventions/                 # Agent-critical coding conventions
│   └── CONVENTIONS.md          # Mathematical definitions agents must follow
├── planning/                   # Detailed implementation planning (former api-planning/)
│   ├── TODO.md                 # Task breakdown and priorities
│   ├── ALGORITHMS.md           # Algorithm specifications
│   ├── categories/             # Category-theoretic API design
│   ├── factory.md              # Factory pattern implementations
│   └── BILINEAR_MODULES_TDD_PLAN.md  # TDD workflow specifications
├── tools/                      # Development tools and utilities
│   ├── agents/                 # Specialized agent configurations
│   ├── testing/                # Test infrastructure
│   └── validation/             # Code validation tools
└── src/                        # Source code (links to ../src/)
```

## Mathematical Accuracy Requirements

**CRITICAL**: All implementations must follow the mathematical conventions defined in `conventions/CONVENTIONS.md`. These conventions prevent agents from falling back to incorrect training data.

### Key Mathematical Principles
1. **Bilinear vs Inner Product**: Distinguish between general bilinear forms and positive definite inner products
2. **Gram vs Cartan Matrices**: Use proper mathematical definitions, not crystallographic shortcuts
3. **Exact Arithmetic**: No floating-point approximations for classification algorithms
4. **Field Extensions**: Handle non-crystallographic types (H₃, H₄) with proper algebraic number fields

## Development Workflow

### TDD Agent System
The implementation uses specialized agents coordinated through TDD workflows:

**Primary Agents**:
- **TDD-TestWriter**: Creates comprehensive, ungameable tests
- **TDD-Implementer**: Implements functionality to pass tests (without gaming)
- **TDD-Adversarial**: Detects gaming patterns and creates adversarial tests
- **TDD-Validator**: Black-box test execution and validation

**Anti-Gaming Measures** (Critical):
- Property-based testing prevents reverse-engineering of expected outputs
- Black-box test execution hides test internals from implementers
- Gaming detection identifies hardcoded test responses
- Mathematical validation ensures real functionality over test satisfaction

### Development Process

1. **Planning Phase**: Use `planning/` docs to understand requirements and API design
2. **Test-First**: TDD-TestWriter creates comprehensive test suites
3. **Implementation**: TDD-Implementer builds functionality guided by tests
4. **Validation**: TDD-Adversarial and TDD-Validator ensure quality
5. **Integration**: Continuous integration with existing mathematical framework

### Code Organization

**Category-Theoretic Structure**: Follow the category design in `planning/categories/`:
- **BilinearRMod**: Base category of bilinear R-modules
- **SymmetricRMod**: Symmetric bilinear modules (our focus)
- **DefiniteLattices**: Positive/negative definite subcategories
- **IndefiniteLattices**: Hyperbolic and mixed-signature cases

**Factory Pattern**: Use `planning/factory.md` for consistent object construction with proper mathematical validation.

## Development Guidelines

### Agent Instructions

**For TDD-TestWriter**:
- Create property-based tests that cannot be gamed
- Focus on mathematical properties, not specific outputs
- Include boundary conditions and edge cases
- Test against literature examples with known results

**For TDD-Implementer**:
- Implement real mathematical functionality, not test satisfaction
- Use exact arithmetic throughout (no floating-point shortcuts)
- Follow mathematical conventions strictly
- Document algorithmic choices and complexity analysis

**For Code Reviewers**:
- Verify mathematical correctness against theory
- Check for gaming patterns (hardcoded test responses)
- Ensure exact arithmetic is maintained
- Validate performance characteristics

### Quality Standards

**Mathematical Rigor**:
- All algorithms preserve mathematical meaning
- Exact computation using appropriate number fields
- Proper error handling for degenerate cases
- Literature validation for classification results

**Code Quality**:
- Clear separation of mathematical concepts
- Proper abstraction levels (no premature optimization)
- Comprehensive test coverage
- Documentation linking code to mathematical theory

**Performance Requirements**:
- Efficient algorithms for practical problem sizes
- Pruning strategies for exponential searches
- Parallelization where mathematically appropriate
- Memory-conscious implementations for large matrices

## Integration with Research Environment

### Research ↔ Implementation Flow

**From Research to Implementation**:
- Mathematical theory guides algorithmic design
- Literature examples become test cases
- Open questions drive feature priorities
- Historical context informs implementation choices

**From Implementation to Research**:
- Computational results validate theoretical predictions
- Performance analysis suggests algorithmic improvements
- Edge cases discovered during testing inform theory
- Implementation experience guides research directions

### Shared Resources

**Mathematical Foundations**: Implementation algorithms must align with `../research/foundations/`
**Literature Validation**: Use examples from `../research/literature/` for testing
**Experimental Framework**: Implementation supports research exploration needs

## Tool Integration

### SageMath Integration
- Use SageMath for exact arithmetic over number fields
- Leverage existing root system and lattice implementations
- Maintain compatibility with SageMath categorical framework
- Provide SageMath-compatible interfaces for external use

### Testing Infrastructure
- pytest for Python unit and integration tests
- Property-based testing using Hypothesis
- Performance benchmarking for algorithmic comparisons
- Literature-based validation test suites

### Development Tools
- Black-box test execution environment
- Gaming detection utilities
- Mathematical validation scripts
- Performance profiling and optimization tools

## Quick Start for Developers

### Initial Setup
1. **Read Conventions**: Start with `conventions/CONVENTIONS.md` - absolutely critical
2. **Understand Planning**: Review `planning/TODO.md` and relevant algorithm docs
3. **Study Category Design**: Examine `planning/categories/` for API structure
4. **Check Examples**: Look at existing tests and implementations for patterns

### Development Workflow
```bash
# 1. Create tests first (TDD approach)
# 2. Run black-box test execution
# 3. Implement functionality to pass tests
# 4. Run adversarial gaming detection
# 5. Validate against literature examples
# 6. Integration with existing codebase
```

### Common Pitfalls to Avoid
- **Mathematical Errors**: Always consult `conventions/CONVENTIONS.md`
- **Gaming**: Never hardcode test-specific responses
- **Floating-Point**: Use exact arithmetic only
- **Premature Optimization**: Focus on mathematical correctness first

## Agent Communication Protocols

### Inter-Agent Coordination
- **Clear Task Boundaries**: Each agent has specific responsibilities
- **Information Isolation**: Implementers don't see test internals
- **Quality Gates**: Validation agents block gaming attempts
- **Escalation Paths**: Human oversight for complex mathematical decisions

### Error Handling
- **Mathematical Errors**: Immediate escalation to human oversight
- **Gaming Detection**: Automatic rejection with detailed analysis
- **Performance Issues**: Algorithmic review and optimization
- **Integration Failures**: Systematic debugging with mathematical validation

---

**Implementation Environment Mission**: Provide robust, mathematically correct software development infrastructure that maintains the highest standards of mathematical accuracy while enabling efficient agent-driven development workflows.

**Quality Assurance**: Every implementation must pass mathematical validation, gaming detection, and literature verification before integration into the main codebase.