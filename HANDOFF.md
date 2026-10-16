# Active task: geometry and cohomology categories in the preamble

## Ambient task

Present the categories, their placements and subtrees, and the functorial
constructions in the scope below. Make the named mathematical objects construct
through the preamble. Each construction must retain its defining data and maps,
lie in the correct category, and expose its operations at their mathematical
owners.

The initial request permitted category and operation stubs. The subsequent
construction pass requires every named construction to work through the session
star import, print the mathematical object and answer the named operation.
A construction failure or wrong placement is required repair work. Explicit
computational stubs remain permitted only at the boundaries stated below.

## Completion condition and complete scope

This task is incomplete. Every row below remains open until its full acceptance
condition has been checked against live source and the required mathematical
assertions. A verified specimen establishes only the stated result.

For each row, establish the public constructor, defining data, immediate
supercategories, inherited operations and relevant functors. Check functor
domains, codomains, action on arrows and the retained universal maps. Construct
objects through their mathematical owners; expose preamble objects throughout.

“Partial” records bounded verification from the current local line. It does not
establish the entire acceptance condition. Recheck the named source and
assertions before relying on that status.

| Required item | Acceptance condition | Verified status and remaining checks |
| --- | --- | --- |
| Exact complex field CC | Use Nemo/Calcium privately for exact complex computation. Retain the morphisms ZZ, QQ, QQbar and exact RR into CC. Conjugation is a field automorphism; absolute value lands in exact RR. Numerical approximation uses a named map. Polynomial rings and schemes over CC construct. | Partial: algebraic ingress, I² = −1, exp(Iπ) = −1, and distinction of 1 from 1 + 10⁻³⁰ were exercised. The Fermat quartic constructs with its stated variety placement. Check all field structure, elementary functions and scalar maps. |
| Varieties over k | Present integral, separated, finite-type schemes with their correct category parents and constructors, including exact CC as a base. | Partial: the Fermat quartic over CC constructs with explicitly stated variety placement. Reconcile the general constructors and hypotheses. |
| Curves and surfaces | Present the relative-dimension-one and relative-dimension-two varieties and their projective and proper refinements. | Partial: the real projective plane and the affine parabola through Curves(QQ).from_equation construct in their stated categories. Check all requested bases and refinement maps. General hypersurface construction alone does not assert integrality. |
| K3 surfaces | Construct the smooth quartic and the stated Horikawa family through their defining scheme and surface owners. Retain inclusions and family data. | Partial: the quartic supplies rank-22 cohomology with Hodge numbers (1,20,1). Horikawa defining bundles and invariant branch sections construct. Reconcile the remaining K3 requirements. |
| Families X → Y and one-parameter families X → C | Represent a family by its actual morphism, as an object of the appropriate slice. Construct fibres with their pullback projections and universal maps. | Partial: Hesse affine and projective pencils construct; a projective-pencil fibre retains both projections. The Legendre family morphism constructs. Check all named families, bases and fibre operations. |
| Function fields k(t) | Construct the function field of a nonempty affine chart of an integral scheme; P¹ gives k(t). | Partial: the projective-space function field constructs. Check the P¹ specimen and the chart and scalar maps. |
| Affine and projective hypersurfaces | Construct the defining coordinate rings, equation, closed subscheme and inclusion through the public owners. Retain homogeneous grading in the projective case. | Partial: both constructors are present and exercised. Check defining maps, required placement and all named specimens. |
| O on projective space and its twists O(m) | Construct the invertible sheaf and its sections. For O(m) on Pⁿ, H⁰ is the degree-m forms, Hⁿ is dual to the degree −m−n−1 forms, and intermediate cohomology vanishes. | Partial: H⁰(P²,O(1)) has rank three and derived global sections construct. Check positive and negative twists and the higher-cohomology specimens. |
| Presheaves and sheaves valued in sets, groups, rings, ZZ-modules, R-modules and R-algebras | Present the value categories and the actual sections functor on opens, its restriction maps and sheaf descent. Keep fixed-value functor categories distinct from the varying-value construction. | Partial: the fixed-value presheaf categories construct for all listed values. The affine structure sheaf constructs. Actual sections and restrictions remain to be established across the requested owners; live constructors still use _UnpresentedSectionsPresheaf. |
| Projectivization P(V) | Construct Proj Sym(V) with its projection, tautological invertible sheaf and universal quotient. Retain the comparison with projective space for a free module and the required relative maps. | Partial: rank-two projectivization, its surjective universal quotient and the projective-space comparison construct. Check the complete relative construction and slice API. |
| Module duals | Construct Mor_R(M,R¹) at the module owner with its module structure and evaluation maps. | Partial: the rank-two vector-space dual has rank two. Check the requested functorial maps and variance. |
| Linear systems and monomial section bases | Retain the selected section space, embedding into global sections, base locus, domain of definition and associated map. Construct restriction and jet maps where requested. | Partial: the complete conic system on P² has six monomial sections and its associated map. Coordinate-hyperplane restrictions and jet specimens were exercised. Reconcile the remaining maps and systems. |
| Graded singular cohomology | Construct H*(X;R) with grading, cup product, coefficient maps and functorial action. | Partial: the complex realization of P² supplies a graded algebra over ZZ. Check its operations and the required maps. |
| de Rham algebra and cohomology | Construct the relative graded-commutative DGA of a smooth affine scheme, its differential, and the stated cohomology. Include vector fields, graded derivations, contraction and Lie derivative at their owners. | Partial: QQ[x] de Rham algebra and degree-minus-one derivations construct; H²_dR(P²) has rank one. Reconcile the smooth affine relative specimen and Cartan operations. |
| Derived sheaf cohomology and RΓ | Construct derived global sections in the appropriate derived category. Sheaf cohomology in degree i is the ith cohomology of that object. Present the R-linear triangulated parent of D(R). | Partial: derived sections of O(1) on P² construct. Check category parents, the cohomology identification and the required maps. |
| Primitive cohomology | For a polarized smooth n-fold, retain the kernel and inclusion of L_h^(n−k+1): H^k → H^(2n−k+2). P² in degree two has primitive rank zero; a smooth plane cubic in degree one has rank two. | Partial: the P² specimen has rank zero. Check the cubic specimen, polarization and Lefschetz maps. |
| Residue maps on forms | Construct the residue map with its actual differential-form domain and codomain, including the stated plane-cubic specimen. | Partial: the plane-cubic residue object has rank-one domain and codomain. Check the defining spaces and maps. General residue computation may remain an explicit stub. |
| Homotopy Lie algebras | Construct the pointed-space graded Lie algebra with the Whitehead bracket and stated grading. For S², shifted degrees one and two have rank one and [ι,ι] = 2η. | Partial: these S² assertions were exercised. Check integral versus rational placement, the degree conventions and functorial maps. Computation of sphere homotopy in degrees at least four may remain a stated frontier. |
| Hodge and mixed Hodge structures | Present the coefficient objects, filtrations and their maps. Construct Tate twists, tensor products and duals. Include projective-space and K3 Hodge structures. | Partial: the named operations and P² and quartic K3 Hodge-number specimens were exercised. Reconcile all structure maps and category placement. |
| Connections and Gauss–Manin connections | Present bundles with connection and their morphisms. For a smooth proper family, construct the Gauss–Manin object in integrable connections on the base. | Partial: the Hesse smooth-locus object lies in integrable connections with finite locally free underlying bundle. Check connection morphisms and retained family maps. The Gauss–Manin connection matrix may remain an explicit computational stub. |
| Analytic disc fibres | Construct the analytic family, exact-complex disc points, fibres and fibre inclusions along the selected scalar embedding. | Partial: a disc-point fibre is a complex manifold and the inclusion retains that same fibre as domain. Reconcile all required family maps and analytification. |
| HH and Γ\\HH | Construct the upper half-plane, group action and quotient with their correct complex-manifold or orbifold placement. | Partial: HH and SL₂(ZZ)\\HH construct. Check action morphisms and quotient maps. |
| Real hyperbolic Hⁿ and its quotients | Construct H² and H³ through their Riemannian and globally symmetric owners. Retain the discrete isometry action and quotient map. | Partial: H² and its lattice-isometry quotient construct with Riemannian manifold and orbifold placement. Check H³ and the retained maps. |
| Siegel H_g and its quotients | Construct the symmetric-matrix domain with positive definite imaginary part and the symplectic action. Construct Sp₄(ZZ)\\H₂ as an orbifold. | Partial: H₂ and the stated arithmetic quotient construct. Reconcile the defining domain, action and quotient maps. |
| Symmetric spaces G/K by Satake type | Supply the classification type as a category parameter. Construct the correct Riemannian symmetric-space object and retain its defining data. | Partial: the SU(2,1) Satake specimen has real rank one and dimension four. Reconcile the full requested type construction and parents. |
| Hermitian symmetric domains by type | Present the domain classification through parameters of the appropriate category, with correct parent and dimension. | Partial: EIII and EVII construct with dimensions sixteen and twenty-seven. Check the remaining named types and defining data. |

### Permitted stubs

A general operation may retain an explicit computational stub where the
construction request permits it. The table names the specific residue,
Gauss–Manin matrix and higher sphere-homotopy frontiers already identified.
The mathematical object, its defining data, domain, codomain and placement must
still construct. Sections on a non-basis open may assert with the precise
missing computation; an empty sections functor is not a permitted substitute.

For other operations, establish the permission from the original construction
request before marking the item complete. An unverified permission stays open.

### Binding decisions

- Exact CC uses Nemo/Calcium as its private computational engine. Preamble
  QQbar remains at its own owner; CC accepts its elements through QQbar → CC.
- A derivation with regular-module codomain has values in A¹. Compare with A
  through the explicit regular-module identification. The public
  linear_endomorphism operation supplies that transport.
- Use picard_to_class_group_morphism for the existing projective-space map.
  Choose routine public names from the mathematical owner without requesting
  a naming decision.
- Present PicardGroups and ClassGroups as the stated full subcategories of
  abelian groups. Each value supplied by a scheme retains that scheme.
  Picard pullback for a plane cubic must send [O(1)] to [O_C(1)].
- A category parent states the actual mathematics. A missing parent requires
  its own category construction or an explicit abstract boundary.
- All public mathematical objects and their constituents are preamble
  objects. Reuse maintained engines privately.
- Preserve existing rack edits.

## Next work, ranked

1. Verify the current sections constructors before relying on any sheaf
   claim. Start with the existing sheaves-compute-sections-on-opens TODO owner.
   On Spec QQ[x], the sheaf associated to M = QQ[x]¹ must give M on the whole
   space and M_x on D(x), with the localization restriction. Verify the units
   sheaf on that affine scheme and the stated chart-section specimen on P¹.
   Repair the common sections owner and its finite-atlas descent paths.
2. Reconcile each scope row against its live owner, immediate ancestors and
   public constructions. Start with rows whose actual defining functors or
   maps remain unverified. Update this table with exact acceptance status and
   the remaining mathematical obligation. Preserve the independent assertions.
3. Verify the remaining named constructions, including the plane-cubic
   primitive kernel, relative de Rham and Cartan maps, connection morphisms,
   higher-cohomology twists and classification parameters. Repair shared
   structural causes at their owners.
4. Close the task only after every required item meets its acceptance
   condition or has an explicitly permitted and precisely stated stub.
   Selected successful specimens alone do not satisfy that condition.

The earlier issue-401 implementation, port reconciliation and whole-preamble
audit lanes are retired from selection for this request. Their live obligations
belong to TODO.md and their owning artifacts.

### Working references

Read INTENT.md, AGENTS.md, CONTRIBUTING.md, TODO.md, COMPLAINTS.md and the
relevant entries of docs/preamble-megadoc.md before changing the affected
owners. Resolve mathematical placement from the governing architecture.

The original construction detail is in the Claude session
/home/dzack/.claude/projects/-home-dzack-research/7de3fff4-5627-45ef-b8ea-4645b6d2e760.jsonl.
Use the reading-transcripts parser to inspect it. The corresponding briefs are
under /tmp/claude-1000/-home-dzack-research/7de3fff4-5627-45ef-b8ea-4645b6d2e760/scratchpad/.
The governing task, acceptance conditions and decisions needed to resume are
stated above.

For targeted specimens, use
env PYTHONPATH=/home/dzack/research/src /home/dzack/gitclones/sage-dev-allopts/.venv/bin/python.
For a worktree, select its src directory and verify dzack_research.__file__.
The Sage launcher here does not accept -python. Follow the repository rules
for targeted tests and its existing time budgets.
