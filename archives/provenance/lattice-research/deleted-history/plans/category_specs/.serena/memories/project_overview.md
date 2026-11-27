# Category Specs Project

## Purpose
The project aims to record the entirety of existing SageMath methods (for sets, rings, modules, algebras) as a proper collection of Abstract Base Class (ABC) specifications on specific subcategories. It operates non-destructively by intercepting and overwriting constructors, using existing implementations where possible, and refining results into a new subcategory hierarchy.

## Tech Stack
- **SageMath**: Primary mathematical software and execution environment.
- **Python**: Implementation language.
- **Just**: Command runner for task automation.

## Core Structure
The codebase is organized by mathematical domains:
- `sets/`: Set-theoretic categories and specifications.
- `rings/`: Ring-theoretic categories and specifications.
- `modules/`: Module-theoretic categories and specifications.
- `algebras/`: Algebra-theoretic categories and specifications.

Each domain typically contains:
- `axioms.py`: Definition of mathematical axioms.
- `constructions.py`: Functorial constructions.
- `homsets.py`: Specification of morphisms and homsets.
- `smoketest.sage`: Quick validation script.
- `regression/`: Regression tests against existing SageMath behavior.
- `new_spec/`: Tests for the new refined category specifications.

## Style and Conventions
- **ParentMethods**: Methods defined on parent objects (sets, rings, etc.) in the category.
- **SubcategoryMethods**: Methods available on subcategories themselves.
- **Refinement**: Intercepting Sage constructors and ensuring results belong to the new, more precise subcategory hierarchy.
- **Mathematical Meaning**: Axioms must be composable, mathematically meaningful, and chained appropriately.
- **No Automation for Specs**: Spot-checking at runtime is preferred for capturing all methods from existing Sage objects to ensure the spec is exhaustive.
