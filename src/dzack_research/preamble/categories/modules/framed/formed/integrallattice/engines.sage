r"""Engine seams for the indefinite orthogonal-group surfaces.

Three engines live behind this boundary, per the hidden-backend ruling: an
engine is an implementation detail of an owned homset or group surface, and
nothing an engine returns leaves this module unverified over $\mathbb Z$.

* **polyhedral_common** (Mathieu Dutour Sikirić) decides isometry of
  indefinite lattices with an exact witness, enumerates the $O(L)$-orbits
  of the primitive totally isotropic sublattices of rank $k$ and of the
  flags of them, and produces generating sets for $O(L)$ and for stabilizers
  of those sublattices.  It is reached
  through the vendored ``py_polyhedral`` wrapper
  (github.com/MathieuDutSik/py_polyhedral, the reference implementation this
  seam's marshalling follows): drop that clone into ``computations/vendor/``
  and build the ``INDEF_FORM_*`` binaries per the upstream README.  When the
  wrapper is absent the seam says so by name; emptiness questions answer the
  three-valued ``Unknown`` at their own surface instead.  The same package's
  ``LORENTZ_FundDomain_AllcockEdgewalk`` binary walks a fundamental
  polyhedron of the reflection subgroup of a Lorentzian lattice (Allcock's
  edgewalk), deciding reflectivity.

* **OSCAR/Hecke** computes the rational spinor norm of an isometry
  (``rational_spinor_norm`` on a lattice with isometry), Nikulin's
  primitive embedding into an even unimodular lattice
  (``embed_in_unimodular``), and the image in $O(A_L)$ of the centralizer
  of an isometry (``image_centralizer_in_Oq``, hermitian
  Miranda--Morrison), reached as ``julia`` subprocesses.  The spinor and
  centralizer programs are transcribed from the source corpus's backends
  (lattice-research ``dawes_orbit_backend`` and ``oscar_centralizer``),
  which ran them green.

* **VinbergsAlgorithmNF** (Bottinelli) enumerates Vinberg roots over
  totally real number fields; the seam runs it over $\mathbb Q$ as a second
  engine beside ``vinal``.

Matrix convention at this boundary: the preamble reads a morphism matrix in
rows -- row $i$ is the image of the $i$-th framing label -- so an isometry
matrix $W$ preserves the form when $W G W^{\mathsf T}=G$.  Every crossing
below asserts its convention on the returned data rather than trusting the
engine's documentation.
"""

import importlib
import importlib.util
import shutil
import subprocess
import tempfile
import textwrap
from pathlib import Path
from typing import TYPE_CHECKING

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

if TYPE_CHECKING:
    from types import ModuleType

    from sage.matrix.matrix_integer_dense import Matrix_integer_dense

    IntegerRows = list[list[int]]


_POLYHEDRAL_PROVISIONING = (
    "the polyhedral_common engine is not provisioned: clone "
    "github.com/MathieuDutSik/py_polyhedral into computations/vendor/ and "
    "build the INDEF_FORM_* binaries it wraps (polyhedral_common)"
)


def polyhedral_engine() -> "ModuleType | None":
    r"""Return the vendored ``py_polyhedral`` wrapper, or ``None`` when absent.

    Absence is a fact about provisioning, not about the mathematics: callers
    with an ``Unknown`` channel answer ``Unknown``, callers without one
    assert with :data:`_POLYHEDRAL_PROVISIONING`.
    """
    if importlib.util.find_spec("py_polyhedral") is None:
        return None
    return importlib.import_module("py_polyhedral.binaries")


def _integer_rows(gram: "Matrix_integer_dense") -> "IntegerRows":
    return [[int(entry) for entry in row] for row in matrix(SageZZ, gram).rows()]


def indefinite_isometry_witness(
    domain_gram: "Matrix_integer_dense",
    codomain_gram: "Matrix_integer_dense",
) -> "Matrix_integer_dense | None":
    r"""Return $W$ with $W G_{\mathrm{cod}} W^{\mathsf T}=G_{\mathrm{dom}}$, or ``None``.

    The rows of $W$ are the images of the domain's framing labels in the
    codomain's framing, so $W$ *is* the matrix of an isometry
    $L_{\mathrm{dom}}\to L_{\mathrm{cod}}$ in the preamble's row convention.
    ``None`` is the engine's decision that no isometry exists
    (``INDEF_FORM_TestEquivalence``); a returned witness is verified over
    $\mathbb Z$ here before it leaves the seam.
    """
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    raw = engine.indefinite_form_test_equivalence(
        _integer_rows(codomain_gram), _integer_rows(domain_gram)
    )
    if raw is None:
        return None
    witness = matrix(SageZZ, raw)
    assert (
        witness * matrix(SageZZ, codomain_gram) * witness.transpose()
        == matrix(SageZZ, domain_gram)
    ), "the engine's witness does not carry one Gram matrix to the other"
    return witness


def indefinite_orthogonal_group_generator_matrices(
    gram: "Matrix_integer_dense",
) -> tuple:
    r"""Return matrices generating $O(L)$ for an indefinite $L$, row convention.

    ``INDEF_FORM_AutomorphismGroup``: a finite generating set, which $O(L)$
    has by Borel and Harish-Chandra; the engine exhibits one.  Each generator
    is verified to satisfy $MGM^{\mathsf T}=G$ before it leaves the seam.
    """
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    gram_z = matrix(SageZZ, gram)
    generators = tuple(
        matrix(SageZZ, rows)
        for rows in engine.indefinite_form_automorphism_group(_integer_rows(gram))
    )
    assert all(
        generator * gram_z * generator.transpose() == gram_z
        for generator in generators
    ), "an engine generator does not preserve the form"
    return generators


def isotropic_sublattice_orbit_representative_rows(
    gram: "Matrix_integer_dense", rank: int, isotropic_object: str
) -> tuple:
    r"""Return one $k\times n$ basis-row block per $O(L)$-orbit.

    ``INDEF_FORM_GetOrbit_IsotropicKplane``: representatives of the
    $O(L)$-orbits of the primitive totally isotropic sublattices of rank
    ``rank`` (``isotropic_object="plane"``), or of the flags of such
    sublattices whose top term has that rank
    (``isotropic_object="flag"``).  Rows are validated by the caller against
    the owned lattice (isotropy, orthogonality, independence); this seam only
    shapes the data.
    """
    assert isotropic_object in ("plane", "flag"), (
        "the engine enumerates isotropic sublattices or flags of them"
    )
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    return tuple(
        engine.indefinite_form_isotropic_k_stuff(
            _integer_rows(gram), int(rank), isotropic_object
        )
    )


def indefinite_vector_orbit_representative_rows(
    gram: "Matrix_integer_dense", square: int
) -> tuple:
    r"""Return one coordinate row per $O(L)$-orbit of vectors of the given square.

    ``INDEF_FORM_GetOrbitRepresentative``: representatives of the
    $O(L)$-orbits of vectors $v$ with $b(v,v)=\text{square}$ -- finitely
    many for an indefinite lattice (the migrated finiteness note is
    ``notes/topics/coble-enriques-lattice-theory/``
    ``finiteness-orbits-indefinite-lattices.md``).  Each returned row is
    verified here to have the requested square before it leaves the seam;
    reading rows as lattice elements is the owned caller's step.
    """
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    gram_z = matrix(SageZZ, gram)
    rows = tuple(
        tuple(SageZZ(entry) for entry in row)
        for row in engine.indefinite_form_get_orbit_representative(
            _integer_rows(gram), int(square)
        )
    )
    for row in rows:
        vector_row = matrix(SageZZ, [row])
        assert (vector_row * gram_z * vector_row.transpose())[0, 0] == square, (
            "an engine orbit representative does not have the requested square"
        )
    return rows


def isotropic_sublattice_stabilizer_generator_matrices(
    gram: "Matrix_integer_dense", basis_rows: "IntegerRows", isotropic_object: str
) -> tuple:
    r"""Return generators of the setwise stabilizer of an isotropic sublattice or flag.

    ``INDEF_FORM_StabilizerIsotropicPlane``: for
    ``isotropic_object="plane"`` the stabilizer of the sublattice
    ``basis_rows`` spans; for ``isotropic_object="flag"`` the stabilizer of
    the full chain the rows generate, term by term.  Form preservation is
    verified per generator; span preservation is the caller's check against
    the owned subobjects.
    """
    assert isotropic_object in ("plane", "flag"), (
        "the engine stabilizes isotropic sublattices or flags of them"
    )
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    gram_z = matrix(SageZZ, gram)
    generators = tuple(
        matrix(SageZZ, rows)
        for rows in engine.indefinite_form_stabilizer_isotropic_subspace(
            _integer_rows(gram), basis_rows, choice=isotropic_object
        )
    )
    assert all(
        generator * gram_z * generator.transpose() == gram_z
        for generator in generators
    ), "an engine stabilizer generator does not preserve the form"
    return generators


def vector_equivalence_witness(
    gram: "Matrix_integer_dense",
    source_row: list,
    target_row: list,
) -> "Matrix_integer_dense | None":
    r"""Return $W$ with $WGW^{\mathsf T}=G$ and $vW=w$, or ``None``.

    ``INDEF_FORM_TestEquivalenceVector`` answers in the transposed-inverse
    orientation (recorded by the source corpus's validated normalizer); the
    seam inverts once and asserts the row-convention identities on the
    result, so a convention drift upstream fails loudly here.

    Any two vectors: the engine's decision does not ask for isotropy, and
    the non-isotropic case is the one Dawes' vector-orbit theory consumes.
    """
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    raw = engine.indefinite_form_test_equivalence_vector(
        _integer_rows(gram),
        [int(entry) for entry in source_row],
        [int(entry) for entry in target_row],
    )
    if raw is None:
        return None
    witness = matrix(SageZZ, raw).inverse().change_ring(SageZZ)
    gram_z = matrix(SageZZ, gram)
    assert witness * gram_z * witness.transpose() == gram_z, (
        "the engine's vector witness does not preserve the form"
    )
    source = matrix(SageZZ, [source_row])
    target = matrix(SageZZ, [target_row])
    assert source * witness == target, (
        "the engine's vector witness does not carry the source to the target"
    )
    return witness


def vector_stabilizer_generator_matrices(
    gram: "Matrix_integer_dense", vector_row: list
) -> tuple:
    r"""Return generators of $\operatorname{Stab}_{O(L)}(v)$, row convention.

    ``INDEF_FORM_StabilizerVector``: a generating set for the *pointwise*
    stabilizer of one vector -- the group whose finite-quotient image turns
    an $O(L)$-equivalence witness into a decision about a subgroup
    containing $\ker\varphi$.  Each generator is verified here to preserve the form and to
    fix the vector; that the set generates the whole stabilizer is the
    engine's contract, stated and not re-derived.
    """
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    gram_z = matrix(SageZZ, gram)
    row = matrix(SageZZ, [[int(entry) for entry in vector_row]])
    generators = tuple(
        matrix(SageZZ, rows)
        for rows in engine.indefinite_form_stabilizer_vector(
            _integer_rows(gram), [int(entry) for entry in vector_row]
        )
    )
    assert all(
        generator * gram_z * generator.transpose() == gram_z
        for generator in generators
    ), "an engine stabilizer generator does not preserve the form"
    assert all(row * generator == row for generator in generators), (
        "an engine stabilizer generator moves the vector it must fix"
    )
    return generators


def isotropic_sublattice_equivalence_witness(
    gram: "Matrix_integer_dense",
    source_rows: "IntegerRows",
    target_rows: "IntegerRows",
    isotropic_object: str,
) -> "Matrix_integer_dense | None":
    r"""Return $W$ with $WGW^{\mathsf T}=G$ carrying one isotropic sublattice (or flag) to another.

    ``INDEF_FORM_TestEquivalenceIsotropicKplane``.  For a sublattice the
    check is equality of the row modules of ``source_rows``$\cdot W$ and
    ``target_rows``; for a flag the *chain* is checked term by term -- span
    equality of every initial segment, which is strictly finer than the
    total-span comparison (the source corpus's flag branch checked only total
    spans, deciding a coarser relation; that recorded error is corrected
    here).
    """
    assert isotropic_object in ("plane", "flag"), (
        "the engine compares isotropic sublattices or flags of them"
    )
    engine = polyhedral_engine()
    assert engine is not None, _POLYHEDRAL_PROVISIONING
    raw = engine.indefinite_form_test_equivalence_isotropic_k_plane(
        _integer_rows(gram), source_rows, target_rows, choice=isotropic_object
    )
    if raw is None:
        return None
    witness = matrix(SageZZ, raw)
    gram_z = matrix(SageZZ, gram)
    assert witness * gram_z * witness.transpose() == gram_z, (
        "the engine's sublattice witness does not preserve the form"
    )
    rank = len(source_rows)
    terms = range(1, rank + 1) if isotropic_object == "flag" else (rank,)
    for term in terms:
        image = matrix(SageZZ, source_rows[:term]) * witness
        assert image.row_module() == matrix(SageZZ, target_rows[:term]).row_module(), (
            "the engine's witness does not carry the stated flag term to its target"
        )
    return witness


# ---- the OSCAR seam ----


_JULIA_READ_INT_MATRIX = """
using Oscar

function read_int_matrix(path)
    rows = Vector{Vector{Int}}()
    open(path) do io
        for line in eachline(io)
            line = strip(line)
            isempty(line) && continue
            push!(rows, parse.(Int, split(line)))
        end
    end
    n = length(rows)
    m = length(rows[1])
    return matrix(ZZ, n, m, reduce(vcat, rows))
end
"""


def _julia_stdout_lines(
    julia_program: str, matrices: "tuple[Matrix_integer_dense, ...]", extra_arguments: tuple = ()
) -> list[str]:
    r"""Run one julia program over matrix files; return its stdout lines.

    The matrices are written to files handed over as ``ARGS[1..k]``; further
    scalar arguments follow them.  Callers needing the shared
    ``read_int_matrix`` preamble (which also loads Oscar) prepend
    :data:`_JULIA_READ_INT_MATRIX` themselves.
    """
    assert shutil.which("julia") is not None, (
        "the OSCAR seam runs julia; no julia executable is on PATH"
    )
    with tempfile.TemporaryDirectory() as scratch:
        paths = []
        for index, rows_matrix in enumerate(matrices):
            path = Path(scratch) / f"matrix_{index}.txt"
            path.write_text(
                "\n".join(
                    " ".join(str(entry) for entry in row)
                    for row in _integer_rows(rows_matrix)
                )
                + "\n"
            )
            paths.append(str(path))
        result = subprocess.run(
            [
                "julia",
                "--startup-file=no",
                "-e",
                textwrap.dedent(julia_program),
                *paths,
                *[str(argument) for argument in extra_arguments],
            ],
            capture_output=True,
            text=True,
        )
    assert result.returncode == 0, result.stderr
    return [line.rstrip() for line in result.stdout.splitlines()]


def oscar_even_unimodular_primitive_embedding(
    gram: "Matrix_integer_dense", positive: int, negative: int
) -> tuple["Matrix_integer_dense", "Matrix_integer_dense"]:
    r"""Return $(G_M, W)$: an even unimodular Gram matrix and embedding rows.

    Hecke's ``embed_in_unimodular`` (``QuadForm/Quad/ZLattices.jl``) runs
    Nikulin's complement construction: the complement's genus is read off
    the datum pair (signature $(p-p_S,\,q-n_S)$, discriminant form $-q_S$),
    a representative $R$ is produced, and $S\oplus R$ is glued along an
    anti-isometry of the discriminant forms into the even unimodular $M$.

    Returned in the preamble's row convention: row $i$ of $W$ is the image
    of the $i$-th framing label of $S$ in $M$'s framing, so
    $W G_M W^{\mathsf T} = G_S$ -- asserted here before the data leaves the
    seam, along with $|\det G_M| = 1$ and evenness of the diagonal.
    Primitivity is the owned inclusion's own question (cokernel
    torsion-freeness) and is asserted where that morphism is minted.
    """
    julia_program = """
        gram = read_int_matrix(ARGS[1])
        S = integer_lattice(; gram = change_base_ring(QQ, gram))
        pos = parse(Int, ARGS[2])
        neg = parse(Int, ARGS[3])
        M, S_in_M, iS = embed_in_unimodular(S, pos, neg)
        W = solve(basis_matrix(M), basis_matrix(S_in_M); side = :left)
        GM = change_base_ring(ZZ, gram_matrix(M))
        WZ = change_base_ring(ZZ, W)
        for i in 1:nrows(GM)
            println(join([GM[i, j] for j in 1:ncols(GM)], " "))
        end
        println("--")
        for i in 1:nrows(WZ)
            println(join([WZ[i, j] for j in 1:ncols(WZ)], " "))
        end
        """
    lines = _julia_stdout_lines(
        _JULIA_READ_INT_MATRIX + julia_program,
        (gram,),
        (int(positive), int(negative)),
    )
    separator = next(
        position
        for position, line in enumerate(lines)
        if line == "--"
    )
    codomain_gram = matrix(
        SageZZ, [[SageZZ(entry) for entry in line.split()] for line in lines[:separator] if line]
    )
    embedding_rows = matrix(
        SageZZ,
        [[SageZZ(entry) for entry in line.split()] for line in lines[separator + 1:] if line],
    )
    gram_z = matrix(SageZZ, gram)
    assert embedding_rows * codomain_gram * embedding_rows.transpose() == gram_z, (
        "the engine's embedding rows do not pull the unimodular form back to the domain's"
    )
    assert abs(codomain_gram.determinant()) == 1, (
        "the engine's codomain is not unimodular"
    )
    assert all(codomain_gram[i, i] % 2 == 0 for i in range(codomain_gram.nrows())), (
        "the engine's codomain is not even"
    )
    return codomain_gram, embedding_rows


def oscar_centralizer_discriminant_image(
    gram: "Matrix_integer_dense", isometry_rows: "Matrix_integer_dense"
) -> tuple:
    r"""Return the image of $Z_{O(L)}(f)$ in $O(A_L)$, with its cross-checks.

    Hecke's ``image_centralizer_in_Oq`` on a lattice with isometry: the image
    of the centralizer of $f$ in the discriminant orthogonal group,
    computed by hermitian Miranda--Morrison theory, which is what makes it
    available at all -- the centralizer itself is an infinite arithmetic
    group with no generating set on offer.  Even lattices only, which is
    the hypothesis of that theory and is asserted by the owned caller.

    Returned: ``(generator_rows, order, invariant_rank, coinvariant_rank)``.
    The generator matrices are the engine's, on *its* smith generators of
    $A_L$; crossing them into the owned $O(A_L)$ and checking that they land
    where they must is the caller's step, not this seam's.  The two ranks
    are the engine's own $L^f$ and $L_f$ (the latter the orthogonal
    complement of the former, which is what OSCAR computes -- the source
    corpus's script commented it as $\ker(f+1)$, true only for an
    involution), carried so the owned invariant and coinvariant lattices
    have something to disagree with.
    """
    assert shutil.which("julia") is not None, (
        "the OSCAR seam runs julia; no julia executable is on PATH"
    )
    julia_program = """
        gram = read_int_matrix(ARGS[1])
        isometry = read_int_matrix(ARGS[2])
        L = integer_lattice(; gram = change_base_ring(QQ, gram))
        Lf = integer_lattice_with_isometry(L, change_base_ring(QQ, isometry); check = true)
        println("ranks ", nrows(basis_matrix(invariant_lattice(Lf))),
                " ", nrows(basis_matrix(coinvariant_lattice(Lf))))
        G, _ = image_centralizer_in_Oq(Lf)
        println("order ", order(G))
        for g in gens(G)
            M = matrix(g)
            println("generator")
            for i in 1:nrows(M)
                println("row ", join([M[i, j] for j in 1:ncols(M)], " "))
            end
        end
        """
    lines = _julia_stdout_lines(
        _JULIA_READ_INT_MATRIX + julia_program, (gram, isometry_rows)
    )
    # Keyed lines, so that anything julia prints on its own account -- a
    # package banner, a warning -- is not parsed as data.
    keyed = [line.split(maxsplit=1) for line in lines if line.split()]
    ranks = [entry for entry in keyed if entry[0] == "ranks"]
    orders = [entry for entry in keyed if entry[0] == "order"]
    assert len(ranks) == 1 and len(orders) == 1, (
        f"the engine did not report one rank line and one order line: {lines}"
    )
    invariant_rank, coinvariant_rank = (int(entry) for entry in ranks[0][1].split())
    order = SageZZ(orders[0][1])
    generator_rows: list = []
    for entry in keyed:
        match entry[0]:
            case "generator":
                generator_rows.append([])
            case "row":
                assert generator_rows, (
                    "the engine emitted a matrix row before any generator"
                )
                generator_rows[-1].append(
                    [SageZZ(coordinate) for coordinate in entry[1].split()]
                )
            case _:
                continue
    generators = tuple(matrix(SageZZ, rows) for rows in generator_rows)
    assert all(
        generator.is_square() and generator.determinant() != 0
        for generator in generators
    ), "an engine centralizer-image generator is not invertible"
    return generators, order, invariant_rank, coinvariant_rank


# ---- the polyhedral_common Lorentzian seam ----


_EDGEWALK_PROVISIONING = (
    "the Allcock edgewalk engine is not provisioned: build polyhedral_common "
    "(github.com/MathieuDutSik/polyhedral_common) and put "
    "LORENTZ_FundDomain_AllcockEdgewalk on PATH"
)


def lorentz_edgewalk_fundamental_domain(gram: "Matrix_integer_dense") -> dict:
    r"""Return the edgewalk's fundamental-domain data for a Lorentzian Gram.

    ``LORENTZ_FundDomain_AllcockEdgewalk`` (polyhedral_common) walks the
    edges of a fundamental polyhedron for the reflection subgroup
    $W(L)\le O(L)$, per Allcock's edgewalk method -- unlike Vinberg root
    enumeration it terminates on every input, so reflectivity is a decision
    here rather than a wait.  The engine's convention is signature
    $(n, 1)$; the owned caller performs the twist transport.

    Returned dict keys: ``simple_root_rows`` (one integer row per simple
    root, verified here to define an integral reflection preserving the
    form), ``vertices`` (triples of generator row, incident root rows, and
    the vertex norm -- ideal vertices have norm $0$), ``is_reflective``,
    and ``isometry_generator_rows`` (generators of the finite isometry
    group of the polyhedron the engine reports, each verified to preserve
    the form).
    """
    assert shutil.which("LORENTZ_FundDomain_AllcockEdgewalk") is not None, (
        _EDGEWALK_PROVISIONING
    )
    from sage.libs.gap.libgap import libgap

    gram_z = matrix(SageZZ, gram)
    with tempfile.TemporaryDirectory() as scratch:
        gram_path = Path(scratch) / "lorentzian_gram.txt"
        rows = _integer_rows(gram_z)
        gram_path.write_text(
            f"{len(rows)} {len(rows[0])}\n"
            + "\n".join(" ".join(str(entry) for entry in row) for row in rows)
            + "\n"
        )
        out_path = Path(scratch) / "edgewalk.gap"
        namelist_path = Path(scratch) / "edgewalk.nml"
        namelist_path.write_text(
            "&PROC\n"
            f' FileLorMat = "{gram_path}"\n'
            ' OptionInitialVertex = "isotropic_vinberg"\n'
            ' OutFormat = "GAP"\n'
            f' FileOut = "{out_path}"\n'
            ' OptionNorms = "all"\n'
            " EarlyTerminationIfNotReflective = T\n"
            " ComputeAllSimpleRoots = T\n"
            "/\n"
        )
        run = subprocess.run(
            ["LORENTZ_FundDomain_AllcockEdgewalk", str(namelist_path)],
            capture_output=True,
            text=True,
        )
        assert run.returncode == 0, run.stderr
        # The engine writes a GAP function body ("return rec(...);").
        record = dict(
            libgap.eval("(function() " + out_path.read_text() + " end)()")
        )

    simple_root_rows = tuple(
        tuple(SageZZ(entry) for entry in row)
        for row in record["ListSimpleRoots"].sage()
    )
    for row in simple_root_rows:
        root = matrix(SageZZ, [row])
        square = (root * gram_z * root.transpose())[0, 0]
        assert square != 0, "a simple root is isotropic"
        pairings = gram_z * root.transpose()
        assert all(2 * entry[0] % square == 0 for entry in pairings.rows()), (
            "a simple root's reflection is not integral on the lattice"
        )
    vertices = tuple(
        (
            tuple(SageZZ(entry) for entry in vertex["gen"].sage()),
            tuple(
                tuple(SageZZ(entry) for entry in root)
                for root in vertex["l_roots"].sage()
            ),
            vertex["norm"].sage(),
        )
        for vertex in record["ListVertices"]
    )
    isometry_generators = tuple(
        matrix(SageZZ, generator.sage())
        for generator in libgap.GeneratorsOfGroup(record["GrpIsomCoxMatr"])
        if not bool(libgap.IsOne(generator))
    )
    assert all(
        generator * gram_z * generator.transpose() == gram_z
        for generator in isometry_generators
    ), "an engine polyhedron-isometry generator does not preserve the form"
    return {
        "simple_root_rows": simple_root_rows,
        "vertices": vertices,
        "is_reflective": bool(record["is_reflective"].sage()),
        "isometry_generator_rows": isometry_generators,
    }


# ---- the VinbergsAlgorithmNF seam ----


_VINBERG_NF_PROVISIONING = (
    "the VinbergsAlgorithmNF engine is not provisioned: clone "
    "github.com/bottine/VinbergsAlgorithmNF into ~/gitclones/ and "
    "instantiate its julia project"
)

_VINBERG_NF_PROJECT = Path.home() / "gitclones" / "VinbergsAlgorithmNF"


def vinbergs_algorithm_nf_root_rows(
    gram: "Matrix_integer_dense", count: int
) -> tuple:
    r"""Return up to ``count`` Vinberg roots from the number-field engine.

    VinbergsAlgorithmNF (Bottinelli) runs Vinberg's algorithm over totally
    real number fields; this seam presents $\mathbb Q$ as
    ``rationals_as_number_field`` and asks for the next ``count`` roots --
    the program the source corpus ran.  A second engine for the owned
    ``vinberg_algorithm`` (whose default engine is ``vinal``);
    root normalization differs per engine, so this seam only shapes the
    rows and the owned caller verifies them against the lattice.
    """
    assert _VINBERG_NF_PROJECT.is_dir(), _VINBERG_NF_PROVISIONING
    julia_program = f"""
        import Pkg
        Pkg.activate("{_VINBERG_NF_PROJECT}")
        using Hecke
        using VinbergsAlgorithmNF
        VA = VinbergsAlgorithmNF
        K, a = Hecke.rationals_as_number_field()
        rows = [
            parse.(Int, split(line))
            for line in eachline(ARGS[1])
            if !isempty(strip(line))
        ]
        vd = VA.VinbergData(K, rows)
        (status, (rs, dict, das)) = VA.next_n_roots!(vd, n = parse(Int, ARGS[2]))
        for r in rs
            println(join([string(coordinates(x)[1]) for x in r], " "))
        end
        """
    lines = _julia_stdout_lines(julia_program, (gram,), (int(count),))
    return tuple(
        tuple(SageQQ(entry.replace("//", "/")) for entry in line.split())
        for line in lines
        if line
    )


def oscar_rational_spinor_norm_sign(
    gram: "Matrix_integer_dense", isometry_rows: "Matrix_integer_dense"
) -> int:
    r"""Return the sign of OSCAR's ``rational_spinor_norm`` of one isometry.

    OSCAR/Hecke's convention values the spinor norm of the reflection
    $\sigma_w$ at the square class of $(w,w)$; the corpus's own definition
    (Dawes 2021 §1.2, transcribed in the migrated glossary) uses
    $-(w,w)/2$, and the two differ by the determinant character.  This seam
    returns OSCAR's raw sign; the owned character on
    ``LatticeIsometries.MorphismMethods`` applies the determinant correction
    and documents the relation.  Program transcribed from the source
    corpus's backend, which ran it against Hecke's
    ``integer_lattice_with_isometry``.
    """
    assert shutil.which("julia") is not None, (
        "the OSCAR seam runs julia; no julia executable is on PATH"
    )
    julia_program = textwrap.dedent(
        """
        using Oscar

        function read_int_matrix(path)
            rows = Vector{Vector{Int}}()
            open(path) do io
                for line in eachline(io)
                    line = strip(line)
                    isempty(line) && continue
                    push!(rows, parse.(Int, split(line)))
                end
            end
            n = length(rows)
            m = length(rows[1])
            return matrix(ZZ, n, m, reduce(vcat, rows))
        end

        gram = read_int_matrix(ARGS[1])
        lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
        isometry = read_int_matrix(ARGS[2])
        lattice_with_isometry = integer_lattice_with_isometry(
            lattice,
            change_base_ring(QQ, isometry);
            check = true,
        )
        println(rational_spinor_norm(lattice_with_isometry))
        """
    )
    with tempfile.TemporaryDirectory() as scratch:
        gram_path = Path(scratch) / "gram.txt"
        isometry_path = Path(scratch) / "isometry.txt"
        for path, rows in (
            (gram_path, _integer_rows(gram)),
            (isometry_path, _integer_rows(isometry_rows)),
        ):
            path.write_text(
                "\n".join(" ".join(str(entry) for entry in row) for row in rows)
                + "\n"
            )
        result = subprocess.run(
            [
                "julia",
                "--startup-file=no",
                "-e",
                julia_program,
                str(gram_path),
                str(isometry_path),
            ],
            capture_output=True,
            text=True,
        )
    assert result.returncode == 0, result.stderr
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert len(lines) == 1, f"expected one spinor norm, got {lines}"
    numerator, _, denominator = lines[0].partition("//")
    value = SageZZ(numerator) / SageZZ(denominator if denominator else 1)
    assert value != 0, "the spinor norm of an isometry is a nonzero square class"
    return 1 if value > 0 else -1
