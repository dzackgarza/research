# Vendored from https://github.com/MathieuDutSik/py_polyhedral.
#
# The wrapper is part of the Python package; the large polyhedral_common
# executables are deliberately not.  Backend calls resolve the requested
# executable from PATH at call time, so the wrapper remains importable in an
# environment where none of the optional binaries are installed.
import ast
import os
import shutil
import subprocess
import tempfile


def binary_available(the_bin):
    r"""Return whether ``the_bin`` is currently resolvable on ``PATH``."""
    return shutil.which(the_bin) is not None


def get_binary_path(the_bin):
    binary_path = shutil.which(the_bin)
    assert binary_path is not None, (
        f"Binary {the_bin} is not available on PATH. "
        "Install or expose the corresponding polyhedral_common executable "
        "before calling this backend."
    )
    return binary_path


def write_matrix_file(file_name, M):
    n_row = len(M)
    n_col = len(M[0])
    f = open(file_name, 'w')
    f.write(str(n_row) + " " + str(n_col) + '\n')
    for i_row in range(n_row):
        for i_col in range(n_col):
            f.write(" " + str(M[i_row][i_col]))
        f.write("\n")
    f.close()


def write_list_matrix_file(file_name, ListM):
    n_mat = len(ListM)
    n_row = len(ListM[0])
    n_col = len(ListM[0][0])
    f = open(file_name, 'w')
    f.write(str(n_mat) + '\n')
    for i_mat in range(n_mat):
        f.write(str(n_row) + " " + str(n_col) + '\n')
        for i_row in range(n_row):
            for i_col in range(n_col):
                f.write(" " + str(ListM[i_mat][i_row][i_col]))
            f.write("\n")
    f.close()


def write_group_file(file_name, l_gen, n_act):
    n_gen = len(l_gen)
    f = open(file_name, 'w')
    f.write(str(n_act) + " " + str(n_gen) + '\n')
    for e_gen in l_gen:
        for i_act in range(n_act):
            f.write(" " + str(e_gen[i_act]))
        f.write("\n")
    f.close()


def ast_read(file_name):
    assert os.path.exists(file_name), f"Output file {file_name} does not exist"
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return ast.literal_eval(content)


def run_and_check(list_comm):
    arr_output = tempfile.NamedTemporaryFile()
    output_file = arr_output.name
    list_comm_call = list_comm
    list_comm_call.append("PYTHON")
    list_comm_call.append(output_file)
    result = subprocess.run(list_comm_call, capture_output=True, text=True)
    assert result.returncode == 0, (
        f"Command {list_comm} failed: {result.stderr[:500]}"
    )
    return ast_read(output_file)


def compute_isotropic_vector(M):
    binary_path = get_binary_path("LATT_FindIsotropic")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "rational", input_file])


def compute_canonical_form(M):
    binary_path = get_binary_path("LATT_Canonicalize")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def test_copositivity(M):
    binary_path = get_binary_path("CP_TestCopositivity")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def test_complete_positivity(M):
    binary_path = get_binary_path("CP_TestCompletePositivity")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def indefinite_form_automorphism_group(M):
    binary_path = get_binary_path("INDEF_FORM_AutomorphismGroup")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def indefinite_form_test_equivalence(M1, M2):
    binary_path = get_binary_path("INDEF_FORM_TestEquivalence")
    arr_input1 = tempfile.NamedTemporaryFile()
    arr_input2 = tempfile.NamedTemporaryFile()
    input1_file = arr_input1.name
    input2_file = arr_input2.name
    write_matrix_file(input1_file, M1)
    write_matrix_file(input2_file, M2)
    return run_and_check([binary_path, "gmp", input1_file, input2_file])


def indefinite_form_test_equivalence_vector(M, v1, v2):
    """Return a witness in O(M) sending the first integral vector to the second.

    M:
        n x n Gram matrix as a list of lists of integers.
    v1, v2:
        integer vectors of length n.

    Returns:
        an n x n integer matrix witness, or ``None`` if the vectors are not
        equivalent under the full orthogonal group ``O(M)``.
    """
    binary_path = get_binary_path("INDEF_FORM_TestEquivalenceVector")
    arr_Q = tempfile.NamedTemporaryFile()
    arr_v1 = tempfile.NamedTemporaryFile()
    arr_v2 = tempfile.NamedTemporaryFile()
    write_matrix_file(arr_Q.name, M)
    write_vector_file(arr_v1.name, v1)
    write_vector_file(arr_v2.name, v2)
    return run_and_check([binary_path, "gmp", arr_Q.name, arr_v1.name, arr_v2.name])


def indefinite_form_test_equivalence_isotropic_k_plane(M, basis1, basis2, choice="plane"):
    """Return a witness sending one isotropic subspace or flag to another.

    M:
        n x n Gram matrix as a list of lists of integers.
    basis1, basis2:
        k x n integer matrices given as row lists.
    choice:
        ``"plane"`` for isotropic subspaces, ``"flag"`` for isotropic flags.

    Returns:
        an n x n integer matrix witness in row-action convention, or ``None``.
    """
    binary_path = get_binary_path("INDEF_FORM_TestEquivalenceIsotropicKplane")
    arr_Q = tempfile.NamedTemporaryFile()
    arr_basis1 = tempfile.NamedTemporaryFile()
    arr_basis2 = tempfile.NamedTemporaryFile()
    write_matrix_file(arr_Q.name, M)
    write_matrix_file(arr_basis1.name, basis1)
    write_matrix_file(arr_basis2.name, basis2)
    return run_and_check(
        [
            binary_path,
            "gmp",
            arr_Q.name,
            arr_basis1.name,
            arr_basis2.name,
            choice,
        ]
    )


def indefinite_form_get_orbit_representative(M, eNorm):
    binary_path = get_binary_path("INDEF_FORM_GetOrbitRepresentative")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file, str(eNorm)])


def indefinite_form_isotropic_k_stuff(M, k, nature):
    binary_path = get_binary_path("INDEF_FORM_GetOrbit_IsotropicKplane")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file, str(k), nature])


def indefinite_form_isotropic_k_plane(M, k):
    return indefinite_form_isotropic_k_stuff(M, k, "plane")


def indefinite_form_isotropic_k_flag(M, k):
    return indefinite_form_isotropic_k_stuff(M, k, "flag")


def write_vector_file(file_name, v):
    n = len(v)
    with open(file_name, 'w') as f:
        f.write(str(n) + '\n')
        f.write(' '.join(str(x) for x in v) + '\n')


def indefinite_form_stabilizer_vector(M, v):
    """Compute generators of Stab_{O(M)}(v) for any integer vector v.

    v: list of n integers (column vector)
    Returns list of n×n integer matrices generating the stabilizer.
    Convention: generators satisfy M G M^T = G (row-vector / right action).
    Works for isotropic and non-isotropic v alike.
    """
    binary_path = get_binary_path("INDEF_FORM_StabilizerVector")
    arr_Q = tempfile.NamedTemporaryFile()
    arr_v = tempfile.NamedTemporaryFile()
    write_matrix_file(arr_Q.name, M)
    write_vector_file(arr_v.name, v)
    return run_and_check([binary_path, "gmp", arr_Q.name, arr_v.name])


def indefinite_form_stabilizer_isotropic_subspace(M, basis, choice="plane"):
    """Compute generators of the stabilizer of an isotropic subspace.

    M: n×n Gram matrix (list of lists of ints)
    basis: k×n matrix (list of k rows) — basis vectors of the isotropic subspace.
           For an isotropic LINE pass a 1×n matrix (one row).
           For an isotropic PLANE pass a 2×n matrix (two rows).
           For a FLAG pass a k×n matrix where rows are nested: row[0] spans
           the line, rows 0..1 span the plane, etc.
    choice: "plane" — stabilizer of the subspace spanned by basis
            "flag"  — stabilizer of the full flag (line ⊂ plane ⊂ ... ⊂ span(basis))
    Returns list of n×n integer matrices.
    Convention: generators satisfy M G M^T = G.
    """
    binary_path = get_binary_path("INDEF_FORM_StabilizerIsotropicPlane")
    arr_Q = tempfile.NamedTemporaryFile()
    arr_P = tempfile.NamedTemporaryFile()
    write_matrix_file(arr_Q.name, M)
    write_matrix_file(arr_P.name, basis)
    return run_and_check([binary_path, "gmp", arr_Q.name, arr_P.name, choice])


def indefinite_form_stabilizer_isotropic_line(M, v):
    """Compute generators of Stab_{O(M)}(span(v)) for an isotropic line.

    v: list of n integers — a primitive isotropic vector.
    Returns generators of the pointwise stabilizer of the line span(v).
    Use indefinite_form_stabilizer_isotropic_subspace(M, [v], "plane") for the
    setwise stabilizer of the line (= same for lines, differs for planes).
    """
    return indefinite_form_stabilizer_isotropic_subspace(M, [v], "plane")


def indefinite_form_stabilizer_isotropic_plane_2d(M, v1, v2):
    """Compute generators of Stab_{O(M)}(span(v1,v2)) for an isotropic 2-plane."""
    return indefinite_form_stabilizer_isotropic_subspace(M, [v1, v2], "plane")


def indefinite_form_stabilizer_isotropic_flag(M, basis):
    """Compute generators of Stab_{O(M)} for the isotropic flag defined by basis.

    basis: k×n matrix where row[i] extends the flag at each step.
    """
    return indefinite_form_stabilizer_isotropic_subspace(M, basis, "flag")


def dual_description(EXT, GRP):
    binary_path = get_binary_path("POLY_DirectSerialDualDesc")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP, len(EXT))
    return run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file])


def lorentzian_reflective_edgewalk(M):
    binary_path = get_binary_path("LORENTZ_ReflectiveEdgewalk")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def polytope_face_lattice(EXT, GRP, LevSearch):
    binary_path = get_binary_path("POLY_DirectFaceLattice")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP)
    return run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file, str(LevSearch)])


def lattice_compute_delaunay(M):
    binary_path = get_binary_path("LATT_SerialComputeDelaunay")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    return run_and_check([binary_path, "gmp", input_file])


def lattice_iso_delaunay_domains(ListM):
    binary_path = get_binary_path("LATT_SerialLattice_IsoDelaunayDomain")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_list_matrix_file(input_file, ListM)
    return run_and_check([binary_path, "gmp", input_file])
