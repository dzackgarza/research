<!--
Origin: gitclones/integral_lattice/reference_code/free_quadratic_module_integer_symmetric_refactor_checklist.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, section R3). Content below is unmodified.
-->

# Refactor Checklist: free_quadratic_module_integer_symmetric.py.original.py

Goal: make a new `lattice` class, which has a custom class hierarchy separating out mathematical details that make more sense at different levels of abstraction (e.g. things that are defined for more general $R$-modules).
Explicitly, we want to keep all of the EXISTING lattice functionality in sage, potentially rewriting and reorganizing it to be cleaner, more mathematically precise, and more obvious to use, while expanding functionality with new methods, algorithms, constructors, built-ins, etc., all conducive to research in algebraic geometry.

Task: refactor free_quadratic_module_integer_symmetric and related files into new files under integral_lattice

- Total def() count: 113
- Total TODO(FQMIS) tags: 113

Each item corresponds to a TODO(FQMIS) tag added to a function docstring, which indicates a piece of old functionality in `free_quadratic_module_integer_symmetric whose functionality` is being moved to a new method/class/etc under the `integral_lattice` subdirectory.
Line numbers are approximate and may shift as edits are made.

When trying to determine if an item should be checked off, you should look through the ENTIRE class hierarchy under `integral_lattice` to determine if that functionality was implemented SOMEWHERE, and thus available to the `lattice` class. Do not search for exact text matches, since the refactoring process might be in-progress, and new names may not match old names.
You must actually read files and determine if the _semantics_ of the old functionality has been captured somewhere. We are not just moving functions around, we are rewriting a new interface. Backward-compatibility is NOT a goal, and is in fact discouraged.

NOTE: it is perfectly fine to stub methods and entries to help plan and organize where they go. However, stubbing does NOT count as "completion" of the task in this checklist, so do not check it off. Instead, document where it is stubbed, within the checklist.

When writing new functions, one should ALWAYS consult documentation and look for existing implementations FIRST. Some sources:

- https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/integer_lattices/
- https://www.juliapackages.com/p/indefinite
- https://magma.maths.usyd.edu.au/magma/handbook/lattices (Closed source, it seems, but exploring documentation may lead to hints at algorithms in the literature that can be rewritten, or methods that can be turned into algorithms)
- https://magma.maths.usyd.edu.au/magma/handbook/text/332 (similarly)
- https://docs.gap-system.org/doc/ref/chap25.html
- https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_quadratic_module_integer_symmetric.html (this is what we are refactoring, but you can refer to old source code if it is missing)
- https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module_integer.html (for positive definite lattices ONLY)

NOTE: if you use ANY gap functions, you MUST use the newer libgap interface.

NOTE: do NOT modify ANY of the original code. It is for reference ONLY. We are writing a completely new module INSPIRED by the old modules.
Do not add any extra features that were not present in the original code, unless specifically asked for or if there are specific reasons they must be added.

NOTE: do NOT validate input types manually, e.g. with isinstance. Instead, use pydantic types.

NOTE: you MUST use pydantic types on all new function arguments.

# TODOs

- [x] L90 IntegralLattice — implemented in integral_lattice/constructors.py (IntegralLattice). Supports finite types (A,B,C,D,E,F4,G2), affine types (~A,~B,~C,~D,~E,~F4,~G2), hyperbolic plane (U/H), rank-1 Z and <n>, and type-I/II forms I\*{p,q}, II\_{p,q}; also parses sums/powers via direct sums.
- [x] L307 RandomLattice — implemented in integral_lattice/lattice_utils.py (random_lattice)
- [x] L316 IntegralLatticeDirectSum — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.direct_sum)
- [x] L427 IntegralLatticeGluing — implemented in integral_lattice/constructors.py (IntegralLatticeGluing)
- [x] L702 **init** — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.**init**)
- [x] L768 span — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.span)
- [x] L775 \_assign_names — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.assign_names)
- [x] L785 \_assign_generic_names — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.assign_generic_names)
- [x] L793 \_first_ngens — implemented in integral_lattice/FreeModule/free_module.py (FreeModule._first_ngens)
- [x] L802 basis — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.basis)
- [x] L811 take — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.take)
- [ ] L821 dual_basis — implemented via L.dual().basis(); see L1377
- [ ] L828 basis_with_keys — TODO(FQMIS)
- [ ] L835 set_roots — TODO(FQMIS)
- [x] L845 is_decomposable — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.is_decomposable)
- [ ] L850 sub_gram_matrix — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.sub_gram_matrix)
- [ ] L904 subgraph_to_gram_matrix — TODO(FQMIS)
- [x] L909 as_graph — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.as_graph)
- [x] L952 _eq_ — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__eq__)
- [x] L956 _lt_ — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__lt__)
- [x] L960 _le_ — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__le__)
- [x] L964 _add_ — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__add__)
- [x] L968 _mul_ — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__mul__)
- [x] L1003 _repr_ — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric._repr_*)
- [x] L1058 gens_dict — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.gens_dict)
- [x] L1077 b — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.b)
- [x] L1083 q — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.q)
- [x] L1089 **matmul** — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__matmul__)
- [x] L1095 **pow** — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__pow__)
- [x] L1101 **truediv** — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.__truediv__)
- [x] L1107 index — implemented in integral_lattice/FreeModule/submodule.py (Submodule.index)
- [x] L1111 is_unimodular — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_unimodular)
- [x] L1115 AL — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.AL)
- [x] L1120 length — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.length)
- [x] L1124 e_perp_mod_e — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.e_perp_mod_e)
- [ ] L1157 I_perp_mod_I — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.I_perp_mod_I)
- [x] L1251 get_Eichler_matrix — implemented in integral_lattice/elements/bilinear_module_element.py (BilinearModuleElement.get_Eichler_matrix)
- [x] L1414 discriminant_group — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.discriminant_group)
- [x] L1149 is_isotropic_subspace — implemented in integral_lattice/lattice_utils.py (function is_isotropic_subspace)
- [ ] L1157 I_perp_mod_I — TODO(FQMIS)
- [x] L1187 perp — implemented in integral_lattice/FreeModule/submodule.py (Submodule.perp)
- [x] L1194 delta — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.delta)
- [x] L1198 rad — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.rad)
- [x] L1202 project_to_discriminant_group — implemented in integral_lattice/elements/lattice_element.py (LatticeElement.project_to_discriminant_group)
- [x] L1206 div — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.div)
- [x] L1211 defines_reflection — implemented in integral_lattice/elements/bilinear_module_element.py (BilinearModuleElement.defines_reflection)
- [x] L1215 get_reflection — implemented in integral_lattice/elements/bilinear_module_element.py (BilinearModuleElement.get_reflection)
- [x] L1221 get_reflection_matrix — implemented in integral_lattice/elements/bilinear_module_element.py (BilinearModuleElement.get_reflection_matrix)
- [x] L1232 get_Eichler — implemented in integral_lattice/elements/bilinear_module_element.py (BilinearModuleElement.get_Eichler)
- [ ] L1251 get_Eichler_matrix — TODO(FQMIS)
- [x] L1270 to_lin_comb_generators — implemented in sage/modules/free_module_element.pyx (FreeModuleElement.to_lin_comb_generators)
- [x] L1275 to_numerical_vector — implemented in integral_lattice/FreeModule/free_module.py (FreeModule.to_numerical_vector)
- [x] L1279 stable_orthogonal_group — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.stable_orthogonal_group)
- [x] L1286 kernel_sublattice — implemented in sage/modules/free_module_morphism.py (FreeModuleMorphism.kernel)
- [ ] L1290 invariant_sublattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.invariant_submodule)
- [ ] L1309 coinvariant_sublattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.coinvariant_sublattice)
- [ ] L1313 embed — TODO(FQMIS)
- [ ] L1317 embed_in_unimodular — TODO(FQMIS)
- [ ] L1340 enumerate_quadratic_truple — TODO(FQMIS)
- [ ] L1348 glue_map — TODO(FQMIS)
- [ ] L1352 overlattice_from_glue — TODO(FQMIS)
- [x] L1358 is_even — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_even)
- [x] L1377 dual — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.dual)
- [x] L1387 dual_lattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.dual_module)
- [ ] L1414 discriminant_group — TODO(FQMIS)
- [x] L1476 signature — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_form.py (BilinearForm.signature)
- [ ] L1493 signature_pair — TODO(FQMIS)
- [x] L1510 direct_sum — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.direct_sum)
- [ ] L1572 saturation — TODO(FQMIS)
- [x] L1576 is_primitive — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_primitive)
- [x] L1607 orthogonal_complement — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.orthogonal_complement)
- [x] L1649 sublattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.sublattice)
- [x] L1694 overlattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/free_bilinear_module.py (FreeBilinearModule.overlattice)
- [x] L1717 maximal_overlattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.maximal_overlattice)
- [x] L1846 is_isotropic_subspace — implemented in integral_lattice/lattice_utils.py (function is_isotropic_subspace)
- [ ] L1854 is_in_orthogonal_group — TODO(FQMIS)
- [x] L1858 orthogonal_group — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (present; NotImplemented)
- [x] L2017 is_definite — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_definite)
- [x] L2021 is_positive_definite — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_positive_definite)
- [x] L2025 is_negative_definite — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_negative_definite)
- [x] L2043 contains — implemented in sage/modules/free_module.py (Module_free_ambient.__contains__)
- [ ] L2047 primitive_closure — TODO(FQMIS)
- [ ] L2051 saturation — TODO(FQMIS)
- [x] L2055 is_primitive_sublattice — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.is_primitive)
- [ ] L2059 is_primitive_vector — TODO(FQMIS)
- [ ] L2064 irreducible_components — TODO(FQMIS)
- [x] L2072 get_orbits_of_isotropic_k_planes — implemented in integral_lattice/lattice_algorithms.py (INDEF_FORM_GetOrbit_IsotropicKplane)
- [ ] L2105 is_locally_isometric — TODO(FQMIS)
- [ ] L2110 is_isometric — TODO(FQMIS)
- [x] L2136 get_orbit_representative — implemented in integral_lattice/lattice_algorithms.py (INDEF_FORM_GetOrbitRepresentative)
- [ ] L2160 genus — TODO(FQMIS)
- [ ] L2178 genus_representatives — TODO(FQMIS)
- [x] L2183 tensor_product — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.tensor_product)
- [x] L2245 quadratic_form — implemented in integral_lattice/FreeModule/FreeBilinearModule/bilinear_z_module.py (BilinearZModule.quadratic_form)
- [ ] L2263 quadratic_form_as_polynomial — TODO(FQMIS)
- [ ] L2267 bilinear_form_as_polynomial — TODO(FQMIS)
- [x] L2328 LLL — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.LLL)
- [x] L2403 twist — implemented in integral_lattice/FreeModule/FreeBilinearModule/Lattice/lattice_other.py (FreeQuadraticModule_integer_symmetric.twist)
- [ ] L2470 local_modification — TODO(FQMIS)
- [x] L2566 type1 — implemented via IntegralLattice string constructors in integral_lattice/constructors.py (supports I\*{p,q})
- [x] L2572 type2 — implemented via IntegralLattice string constructors in integral_lattice/constructors.py (supports II\*{p,q})

# For DefiniteLattice subclass

- [ ] L874 Coxeter_Diagram — TODO(FQMIS)
- [ ] L920 plot_coxeter_diagram — TODO(FQMIS)
- [ ] L945 roots — TODO(FQMIS)
- [ ] L1266 theta_series — TODO(FQMIS)
- [ ] L1321 close_vectors — TODO(FQMIS)
- [ ] L1328 short_vectors_iterator — TODO(FQMIS)
- [ ] L1332 short_vectors_affine — TODO(FQMIS)
- [ ] L1336 shortest_vectors — TODO(FQMIS)
- [ ] L1344 kissing_number — TODO(FQMIS)
- [ ] L2029 root_lattice_recognition — TODO(FQMIS)
- [ ] L2033 root_lattice_recognition_fundamental — TODO(FQMIS)
- [ ] L2068 definite_orthogonal_groups — TODO(FQMIS)
- [ ] L2272 minimum — TODO(FQMIS)
- [ ] L2299 maximum — TODO(FQMIS)
- [ ] L2369 short_vectors — TODO(FQMIS)
