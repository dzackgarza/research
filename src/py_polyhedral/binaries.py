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
from collections.abc import Sequence
from typing import NotRequired, TypedDict

from sage.rings.integer import Integer
from sage.rings.rational import Rational

# The programs read exact numbers as decimal text, so an entry is any exact
# integer (or, for the polyhedral programs, rational) whose ``str`` is that text.
type ExactInteger = int | Integer
type ExactRational = int | Integer | Rational
type IntegerVector = Sequence[ExactInteger]
type IntegerMatrix = Sequence[Sequence[ExactInteger]]
type RationalMatrix = Sequence[Sequence[ExactRational]]
# A permutation of {0, ..., n-1}, given by the images of 0, ..., n-1.
type PermutationImages = Sequence[int]

# What a program prints in its PYTHON output format, read by ast.literal_eval.
# Each writer is cited from polyhedral_common.  A rational that is not an
# integer prints as ``p/q``, which literal_eval rejects, so parsed entries are
# integers.
# basic_common_cpp/src_matrix/MAT_MatrixFund.h: WriteVectorPYTHON
type ParsedVector = list[int]
# basic_common_cpp/src_matrix/MAT_MatrixFund.h: WriteMatrixPYTHON
type ParsedMatrix = list[list[int]]
# basic_common_cpp/src_comb/Boost_bitset.h: VectVectInt_Print_Kernel.  A face
# is the sorted list of the indices of the rows it contains.
type ParsedFaces = list[list[int]]
# The value set of ast.literal_eval, for an output whose format the program
# does not define for the invocation made here.
type PythonLiteral = (
    int | float | complex | str | bytes | bool | None | list[PythonLiteral] | tuple[PythonLiteral, ...] | dict[PythonLiteral, PythonLiteral] | set[PythonLiteral]
)


class CanonicalForm(TypedDict):
    r"""``src_latt/LATT_Canonicalize.cpp``, PYTHON branch."""

    Basis: ParsedMatrix
    eG: ParsedMatrix


class CopositivityTestResult(TypedDict):
    r"""``src_copos/Copositivity.h``: ``WriteCopositivityTestResult``."""

    isCopositive: bool
    violation_nature: NotRequired[str]
    V: NotRequired[ParsedVector]


class RealizingTerm(TypedDict):
    r"""One term ``val * V V^T`` of a completely positive decomposition."""

    val: int
    V: ParsedVector


class StrictPositivityResult(TypedDict):
    r"""``src_copos/StrictPositivity.h``: ``WriteStrictPositivityResult``."""

    result: bool
    RealizingFamily: NotRequired[list[RealizingTerm]]
    Certificate: NotRequired[ParsedMatrix]


class FundamentalDomainVertex(TypedDict):
    r"""``src_lorentzian/fund_domain_vertices.h``: ``WriteFundDomainVertex``."""

    gen: ParsedVector
    norm: int
    l_roots: ParsedMatrix


class EdgewalkRecord(TypedDict):
    r"""``src_lorentzian/edgewalk.h``: ``PrintResultEdgewalk``, PYTHON branch."""

    LorMat: ParsedMatrix
    l_norms: ParsedVector
    GrpIsomCoxMatr: list[ParsedMatrix]
    is_reflective: NotRequired[bool]
    ListVertices: list[FundamentalDomainVertex]
    n_orbit_vertices: int
    ListSimpleRoots: NotRequired[list[ParsedVector]]
    n_simple: NotRequired[int]


def binary_available(the_bin: str) -> bool:
    r"""Return whether ``the_bin`` is currently resolvable on ``PATH``."""
    return shutil.which(the_bin) is not None


def get_binary_path(the_bin: str) -> str:
    binary_path = shutil.which(the_bin)
    assert binary_path is not None, f"Binary {the_bin} is not available on PATH. Install or expose the corresponding polyhedral_common executable before calling this backend."
    return binary_path


def write_matrix_file(file_name: str, M: RationalMatrix) -> None:
    n_row = len(M)
    n_col = len(M[0])
    f = open(file_name, "w")
    f.write(str(n_row) + " " + str(n_col) + "\n")
    for i_row in range(n_row):
        for i_col in range(n_col):
            f.write(" " + str(M[i_row][i_col]))
        f.write("\n")
    f.close()


def write_list_matrix_file(file_name: str, ListM: Sequence[IntegerMatrix]) -> None:
    n_mat = len(ListM)
    n_row = len(ListM[0])
    n_col = len(ListM[0][0])
    f = open(file_name, "w")
    f.write(str(n_mat) + "\n")
    for i_mat in range(n_mat):
        f.write(str(n_row) + " " + str(n_col) + "\n")
        for i_row in range(n_row):
            for i_col in range(n_col):
                f.write(" " + str(ListM[i_mat][i_row][i_col]))
            f.write("\n")
    f.close()


def write_group_file(file_name: str, l_gen: Sequence[PermutationImages], n_act: int) -> None:
    r"""Write a permutation group of degree ``n_act`` in the format of ``ReadGroup``.

    ``src_group/GRP_GroupFct.h``: ``ReadGroup`` reads the header ``n nbGen``,
    the degree and the number of generators, then each generator as the
    images of ``0, ..., n - 1``.
    """
    n_gen = len(l_gen)
    f = open(file_name, "w")
    f.write(str(n_act) + " " + str(n_gen) + "\n")
    for e_gen in l_gen:
        for i_act in range(n_act):
            f.write(" " + str(e_gen[i_act]))
        f.write("\n")
    f.close()


def read_output(file_name: str) -> str:
    assert os.path.exists(file_name), f"Output file {file_name} does not exist"
    f = open(file_name)
    content = f.read()
    f.close()
    return content


def run_and_check(list_comm: list[str]) -> str:
    r"""Run a program with output format PYTHON and return the text it wrote."""
    arr_output = tempfile.NamedTemporaryFile()
    output_file = arr_output.name
    list_comm_call = list_comm
    list_comm_call.append("PYTHON")
    list_comm_call.append(output_file)
    result = subprocess.run(list_comm_call, capture_output=True, text=True)
    assert result.returncode == 0, f"Command {list_comm} failed: {result.stderr[:500]}"
    return read_output(output_file)


def compute_isotropic_vector(M: RationalMatrix) -> ParsedVector | None:
    binary_path = get_binary_path("LATT_FindIsotropic")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    # src_isotropy/LATT_FindIsotropic.cpp: a vector, or None.
    vector: ParsedVector | None = ast.literal_eval(run_and_check([binary_path, "rational", input_file]))
    return vector


def compute_canonical_form(M: IntegerMatrix) -> CanonicalForm:
    binary_path = get_binary_path("LATT_Canonicalize")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    form: CanonicalForm = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return form


def test_copositivity(M: RationalMatrix) -> CopositivityTestResult:
    binary_path = get_binary_path("CP_TestCopositivity")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    result: CopositivityTestResult = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return result


def test_complete_positivity(M: RationalMatrix) -> StrictPositivityResult:
    binary_path = get_binary_path("CP_TestCompletePositivity")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    result: StrictPositivityResult = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return result


def indefinite_form_automorphism_group(M: IntegerMatrix) -> list[ParsedMatrix]:
    binary_path = get_binary_path("INDEF_FORM_AutomorphismGroup")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    # src_indefinite/INDEF_FORM_AutomorphismGroup.cpp: WriteListMatrixPYTHON.
    generators: list[ParsedMatrix] = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return generators


def indefinite_form_test_equivalence(M1: IntegerMatrix, M2: IntegerMatrix) -> ParsedMatrix | None:
    binary_path = get_binary_path("INDEF_FORM_TestEquivalence")
    arr_input1 = tempfile.NamedTemporaryFile()
    arr_input2 = tempfile.NamedTemporaryFile()
    input1_file = arr_input1.name
    input2_file = arr_input2.name
    write_matrix_file(input1_file, M1)
    write_matrix_file(input2_file, M2)
    # src_indefinite/INDEF_FORM_TestEquivalence.cpp: a matrix, or None.
    witness: ParsedMatrix | None = ast.literal_eval(run_and_check([binary_path, "gmp", input1_file, input2_file]))
    return witness


def indefinite_form_test_equivalence_vector(M: IntegerMatrix, v1: IntegerVector, v2: IntegerVector) -> ParsedMatrix | None:
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
    # src_indefinite/INDEF_FORM_TestEquivalenceVector.cpp: a matrix, or None.
    witness: ParsedMatrix | None = ast.literal_eval(run_and_check([binary_path, "gmp", arr_Q.name, arr_v1.name, arr_v2.name]))
    return witness


def indefinite_form_test_equivalence_isotropic_k_plane(
    M: IntegerMatrix,
    basis1: IntegerMatrix,
    basis2: IntegerMatrix,
    choice: str = "plane",
) -> ParsedMatrix | None:
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
    witness: ParsedMatrix | None = ast.literal_eval(
        run_and_check(
            [
                binary_path,
                "gmp",
                arr_Q.name,
                arr_basis1.name,
                arr_basis2.name,
                choice,
            ]
        )
    )
    return witness


def indefinite_form_get_orbit_representative(M: IntegerMatrix, eNorm: ExactInteger) -> ParsedMatrix:
    binary_path = get_binary_path("INDEF_FORM_GetOrbitRepresentative")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    # src_indefinite/INDEF_FORM_GetOrbitRepresentative.cpp: the matrix whose
    # rows are the representatives, ``[]`` when there are none.
    representatives: ParsedMatrix = ast.literal_eval(run_and_check([binary_path, "gmp", input_file, str(eNorm)]))
    return representatives


def indefinite_form_isotropic_k_stuff(M: IntegerMatrix, k: ExactInteger, nature: str) -> list[ParsedMatrix]:
    binary_path = get_binary_path("INDEF_FORM_GetOrbit_IsotropicKplane")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    # src_indefinite/INDEF_FORM_GetOrbit_IsotropicKplane.cpp:
    # WriteListMatrixPYTHON, one basis matrix per orbit.
    bases: list[ParsedMatrix] = ast.literal_eval(run_and_check([binary_path, "gmp", input_file, str(k), nature]))
    return bases


def indefinite_form_isotropic_k_plane(M: IntegerMatrix, k: ExactInteger) -> list[ParsedMatrix]:
    return indefinite_form_isotropic_k_stuff(M, k, "plane")


def indefinite_form_isotropic_k_flag(M: IntegerMatrix, k: ExactInteger) -> list[ParsedMatrix]:
    return indefinite_form_isotropic_k_stuff(M, k, "flag")


def write_vector_file(file_name: str, v: IntegerVector) -> None:
    n = len(v)
    with open(file_name, "w") as f:
        f.write(str(n) + "\n")
        f.write(" ".join(str(x) for x in v) + "\n")


def indefinite_form_stabilizer_vector(M: IntegerMatrix, v: IntegerVector) -> list[ParsedMatrix]:
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
    generators: list[ParsedMatrix] = ast.literal_eval(run_and_check([binary_path, "gmp", arr_Q.name, arr_v.name]))
    return generators


def indefinite_form_stabilizer_isotropic_subspace(M: IntegerMatrix, basis: IntegerMatrix, choice: str = "plane") -> list[ParsedMatrix]:
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
    # src_indefinite/INDEF_FORM_StabilizerIsotropicPlane.cpp: WriteListMatrixPYTHON.
    generators: list[ParsedMatrix] = ast.literal_eval(run_and_check([binary_path, "gmp", arr_Q.name, arr_P.name, choice]))
    return generators


def indefinite_form_stabilizer_isotropic_line(M: IntegerMatrix, v: IntegerVector) -> list[ParsedMatrix]:
    """Compute generators of Stab_{O(M)}(span(v)) for an isotropic line.

    v: list of n integers — a primitive isotropic vector.
    Returns generators of the pointwise stabilizer of the line span(v).
    Use indefinite_form_stabilizer_isotropic_subspace(M, [v], "plane") for the
    setwise stabilizer of the line (= same for lines, differs for planes).
    """
    return indefinite_form_stabilizer_isotropic_subspace(M, [v], "plane")


def indefinite_form_stabilizer_isotropic_plane_2d(M: IntegerMatrix, v1: IntegerVector, v2: IntegerVector) -> list[ParsedMatrix]:
    """Compute generators of Stab_{O(M)}(span(v1,v2)) for an isotropic 2-plane."""
    return indefinite_form_stabilizer_isotropic_subspace(M, [v1, v2], "plane")


def indefinite_form_stabilizer_isotropic_flag(M: IntegerMatrix, basis: IntegerMatrix) -> list[ParsedMatrix]:
    """Compute generators of Stab_{O(M)} for the isotropic flag defined by basis.

    basis: k×n matrix where row[i] extends the flag at each step.
    """
    return indefinite_form_stabilizer_isotropic_subspace(M, basis, "flag")


def dual_description(EXT: RationalMatrix, GRP: Sequence[PermutationImages]) -> ParsedFaces:
    r"""Return orbit representatives of the facets of the cone on the rows of ``EXT``.

    ``GRP`` generates a group of permutations of the rows of ``EXT``.
    src_dualdesc/POLY_RecursiveDualDesc.h: OutputFacets, PYTHON branch.
    """
    binary_path = get_binary_path("POLY_DirectSerialDualDesc")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP, len(EXT))
    facets: ParsedFaces = ast.literal_eval(run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file]))
    return facets


def lorentzian_reflective_edgewalk(M: IntegerMatrix) -> EdgewalkRecord:
    binary_path = get_binary_path("LORENTZ_ReflectiveEdgewalk")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    record: EdgewalkRecord = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return record


def lorentzian_perfect_domain_traversal(M: IntegerMatrix, option: str = "total") -> str:
    """Return GAP full-adjacency output for all Lorentzian perfect domains.

    This is the Python bridge to ``LORENTZ_MPI_PerfectLorentzian``.  The
    executable itself owns the complete adjacency traversal; this wrapper only
    serializes its documented namelist input and requests
    ``ObjectFullAdjacencyGAP``.  The GAP format is intentional: upstream's
    group object has a native GAP serializer, whereas crossing that group into
    Sage/libGAP belongs at the Sage engine boundary.  A zero runtime bound
    means the executable returns data only after enumeration has completed.
    """
    if option not in ("total", "isotropic"):
        raise ValueError("a Lorentzian perfect-domain traversal is total or isotropic")
    binary_path = get_binary_path("LORENTZ_MPI_PerfectLorentzian")
    with tempfile.TemporaryDirectory() as temporary_directory:
        matrix_file = os.path.join(temporary_directory, "lorentzian.gram")
        output_file = os.path.join(temporary_directory, "perfect-domains.out")
        namelist_file = os.path.join(temporary_directory, "perfect-domains.nml")
        storage_prefix = os.path.join(temporary_directory, "storage")
        write_matrix_file(matrix_file, M)
        with open(namelist_file, "w", encoding="utf-8") as stream:
            stream.write(
                "&DATA\n"
                '  arithmetic = "gmp"\n'
                f'  LorMatFile = "{matrix_file}"\n'
                f'  Option = "{option}"\n'
                '  FileDualDescription = "unset"\n'
                "/\n\n"
                "&SYSTEM\n"
                "  Saving = F\n"
                f'  Prefix = "{storage_prefix}"\n'
                "  max_runtime_second = 0\n"
                '  OutFormat = "ObjectFullAdjacencyGAP"\n'
                f'  OutFile = "{output_file}"\n'
                "/\n"
            )
        result = subprocess.run(
            [binary_path, namelist_file],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, "LORENTZ_MPI_PerfectLorentzian failed: " + result.stderr[:500]
        with open(output_file, encoding="utf-8") as stream:
            return stream.read()


def polytope_face_lattice(EXT: RationalMatrix, GRP: Sequence[PermutationImages], LevSearch: int) -> list[ParsedFaces]:
    r"""Return, for each level up to ``LevSearch``, orbit representatives of faces.

    ``GRP`` generates a group of permutations of the rows of ``EXT``, so the
    group file has degree ``len(EXT)``, as in :func:`dual_description`.
    src_poly/POLY_Kskeletton.h: the PYTHON branch prints one list of faces
    per level.
    """
    binary_path = get_binary_path("POLY_DirectFaceLattice")
    arr_inpEXT = tempfile.NamedTemporaryFile()
    arr_inpGRP = tempfile.NamedTemporaryFile()
    inpEXT_file = arr_inpEXT.name
    inpGRP_file = arr_inpGRP.name
    write_matrix_file(inpEXT_file, EXT)
    write_group_file(inpGRP_file, GRP, len(EXT))
    levels: list[ParsedFaces] = ast.literal_eval(run_and_check([binary_path, "rational", inpEXT_file, inpGRP_file, str(LevSearch)]))
    return levels


def lattice_compute_delaunay(M: IntegerMatrix) -> PythonLiteral:
    binary_path = get_binary_path("LATT_SerialComputeDelaunay")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_matrix_file(input_file, M)
    value: PythonLiteral = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return value


def lattice_iso_delaunay_domains(ListM: Sequence[IntegerMatrix]) -> PythonLiteral:
    binary_path = get_binary_path("LATT_SerialLattice_IsoDelaunayDomain")
    arr_input = tempfile.NamedTemporaryFile()
    input_file = arr_input.name
    write_list_matrix_file(input_file, ListM)
    value: PythonLiteral = ast.literal_eval(run_and_check([binary_path, "gmp", input_file]))
    return value
