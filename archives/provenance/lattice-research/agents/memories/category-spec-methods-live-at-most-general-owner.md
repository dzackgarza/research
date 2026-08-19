---
title: Category Spec Methods Live At The Most General Owner
---

# Category Spec Methods Live At The Most General Owner

## Object

Method ownership in category specs.

## Bad Substitute

Attaching a method to the most salient downstream object where it is used.

## First Question

What is the weakest and most general mathematical category on which this method is
defined?

## Rule

Every method belongs at the most general category where its mathematical definition
applies. Downstream categories inherit or specialize that method; they do not redeclare
it merely because the method is important there.

Start with the mathematical statement in standard language:

- In any category, morphisms have domains and codomains and compose.
- In a concrete category, morphisms can be evaluated on elements.
- In an additive category, each `Hom(X,Y)` is an abelian group and composition is
  bilinear.
- In an `R`-linear category, each `Hom(X,Y)` is an `R`-module and composition is
  `R`-bilinear.
- In an abelian category, kernels and cokernels exist, images and coimages are defined,
  and monomorphisms and epimorphisms are detected by the corresponding kernel and
  cokernel conditions.
- `End(X)` is `Hom(X,X)` and contains the identity endomorphism.
- `Aut(X)` is the group of invertible endomorphisms.
- A matrix representing a morphism exists only after choosing finite free presentations
  or bases.
- In the category of finite-dimensional vector spaces over a field, an endomorphism has
  characteristic polynomial, eigenvalues after scalar extension when necessary,
  eigenspaces, and associated decomposition data under the usual hypotheses.

The accepted owner is the weakest category in that list, not the Sage implementation
class and not a project-specific synonym. If the right phrase is "finite-dimensional
vector spaces over a field", write that phrase. Do not replace standard mathematical
language with a coined project label.

For finitely generated modules over a PID, invariant factors come from the Smith
normal form classification.  Therefore `invariants()` and `invariant_factors()` belong
to `Modules(R).FinitelyPresented().OverPID()`, not to discriminant groups or torsion
quadratic modules.  Discriminant groups use those invariant factors as inherited
module structure while adding form-specific data such as quotient-valued bilinear and
quadratic forms.

## Witness example

A discriminant group `A_L = L^\#/L` has invariant factors because it is a finitely
presented torsion module over a PID. Its discriminant-specific structure is the cokernel
diagram and descended form data, not the invariant-factor classification itself.

## Non-example

Adding `invariants()` to `DiscriminantGroups(ZZ).ParentMethods` because lattice
papers discuss discriminant group invariants.  That duplicates a PID-module method at
a lower category and hides the inheritance relation the spec is supposed to expose.
