r"""Private exact computational seams for owned lattice constructions."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import textwrap

from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.tensors import Tensor, tensor
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


def rational_positive_vector(gram):
    r"""Return one exact rational positive vector for signature ``(1,n)``.

    Sage supplies the rational diagonalization privately.  The returned value
    is immediately re-entered into the preamble as a type-``(1,0)`` tensor;
    the transformation matrix itself is never public API.
    """
    if not isinstance(gram, Tensor) or gram.tensor_valence() != (0, 2):
        raise TypeError("a positive vector is computed from a bilinear-form tensor")
    engine_gram = _engine_component_matrix(gram.change_ring(SageQQ))
    diagonal, change = QuadraticForm(
        SageQQ,
        2 * engine_gram,
    ).rational_diagonal_form(return_matrix=True)
    diagonal_matrix = diagonal.matrix()
    positive = [
        index
        for index in range(diagonal_matrix.nrows())
        if diagonal_matrix[index, index] > 0
    ]
    if len(positive) != 1:
        raise ValueError(
            "a two-component positive cone requires exactly one positive direction"
        )
    column = change.column(positive[0])
    return tensor.vector(SageQQ, tuple(column))


def _integer_tensor_rows(value, *, transpose=False):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError("the OSCAR lattice seam requires a two-index tensor")
    engine = _engine_component_matrix(value)
    if transpose:
        engine = engine.transpose()
    rows = tuple(
        tuple(SageZZ(entry) for entry in row)
        for row in engine.rows()
    )
    return rows


def oscar_rational_spinor_norm_sign(gram, isometry):
    r"""Return the sign of OSCAR's rational spinor norm.

    OSCAR's ``ZZLatWithIsom`` uses the right-action matrix convention.  The
    owned isometry tensor uses column action ``M*v=M(v)``, so the adapter
    transposes exactly once before crossing the boundary.  This function
    returns OSCAR's convention; the owned real-spinor character applies the
    determinant correction separately.
    """
    if shutil.which("julia") is None:
        raise NotImplementedError("the exact rational spinor norm requires Julia/OSCAR")
    gram_rows = _integer_tensor_rows(gram)
    isometry_rows = _integer_tensor_rows(isometry, transpose=True)
    program = textwrap.dedent(
        r"""
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
            return matrix(ZZ, length(rows), length(rows[1]), reduce(vcat, rows))
        end

        gram = read_int_matrix(ARGS[1])
        lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
        isometry = read_int_matrix(ARGS[2])
        lattice_with_isometry = integer_lattice_with_isometry(
            lattice,
            change_base_ring(QQ, isometry);
            check = true,
        )
        # Ask explicitly for the un-negated bilinear form.  Current OSCAR
        # defaults to b=-1, whereas the owned convention applies the sign
        # correction by the determinant at the category boundary.
        println(rational_spinor_norm(lattice_with_isometry; b = 1))
        """
    )
    with tempfile.TemporaryDirectory() as scratch:
        gram_path = Path(scratch) / "gram.txt"
        isometry_path = Path(scratch) / "isometry.txt"
        for path, rows in (
            (gram_path, gram_rows),
            (isometry_path, isometry_rows),
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
                program,
                str(gram_path),
                str(isometry_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "OSCAR rational_spinor_norm failed")
    lines = tuple(line.strip() for line in result.stdout.splitlines() if line.strip())
    if len(lines) != 1:
        raise RuntimeError(f"expected one OSCAR spinor norm, got {lines}")
    numerator, separator, denominator = lines[0].partition("//")
    value = SageQQ(SageZZ(numerator)) / SageZZ(denominator if separator else 1)
    if value == 0:
        raise ArithmeticError("the spinor norm of an isometry is a nonzero square class")
    return SageZZ.one() if value > 0 else -SageZZ.one()


def oscar_centralizer_discriminant_image(gram, isometry):
    r"""Return OSCAR's image of ``Z_{O(L)}(f)`` in ``O(A_L)``.

    The returned generator matrices are private Smith-coordinate data for the
    finite discriminant form.  The public caller must transport them through
    the owned finite-form engine and verify the resulting live automorphisms.
    The lattice-with-isometry input follows OSCAR's right-action convention,
    so the owned type-``(1,1)`` isometry tensor is transposed exactly once at
    this boundary.
    """
    if shutil.which("julia") is None:
        raise NotImplementedError(
            "the centralizer discriminant image requires Julia/OSCAR"
        )
    gram_rows = _integer_tensor_rows(gram)
    isometry_rows = _integer_tensor_rows(isometry, transpose=True)
    program = textwrap.dedent(
        r"""
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
            return matrix(ZZ, length(rows), length(rows[1]), reduce(vcat, rows))
        end

        gram = read_int_matrix(ARGS[1])
        lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
        isometry = read_int_matrix(ARGS[2])
        lattice_with_isometry = integer_lattice_with_isometry(
            lattice,
            change_base_ring(QQ, isometry);
            check = true,
        )
        println(
            "ranks ",
            nrows(basis_matrix(invariant_lattice(lattice_with_isometry))),
            " ",
            nrows(basis_matrix(coinvariant_lattice(lattice_with_isometry))),
        )
        image, _ = image_centralizer_in_Oq(lattice_with_isometry)
        println("order ", order(image))
        for generator in gens(image)
            M = matrix(generator)
            println("generator ", nrows(M), " ", ncols(M))
            for i in 1:nrows(M)
                println("row ", join([M[i, j] for j in 1:ncols(M)], " "))
            end
        end
        """
    )
    with tempfile.TemporaryDirectory() as scratch:
        gram_path = Path(scratch) / "gram.txt"
        isometry_path = Path(scratch) / "isometry.txt"
        for path, rows in (
            (gram_path, gram_rows),
            (isometry_path, isometry_rows),
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
                program,
                str(gram_path),
                str(isometry_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip() or "OSCAR image_centralizer_in_Oq failed"
        )
    lines = tuple(line.strip() for line in result.stdout.splitlines() if line.strip())
    rank_lines = tuple(line for line in lines if line.startswith("ranks "))
    order_lines = tuple(line for line in lines if line.startswith("order "))
    if len(rank_lines) != 1 or len(order_lines) != 1:
        raise RuntimeError(f"OSCAR did not report unique ranks/order lines: {lines}")
    invariant_rank, coinvariant_rank = (
        SageZZ(entry) for entry in rank_lines[0].split()[1:]
    )
    order = SageZZ(order_lines[0].split()[1])

    generators = []
    rows = None
    expected_rows = expected_columns = None
    for line in lines:
        fields = line.split()
        if not fields:
            continue
        if fields[0] == "generator":
            if rows is not None:
                generators.append(
                    tensor.matrix(SageZZ, expected_rows, expected_columns, sum(rows, []))
                )
            expected_rows, expected_columns = map(SageZZ, fields[1:3])
            rows = []
            continue
        if fields[0] == "row":
            if rows is None:
                raise RuntimeError("OSCAR emitted a matrix row before a generator")
            row = [SageZZ(entry) for entry in fields[1:]]
            if len(row) != expected_columns:
                raise RuntimeError("OSCAR emitted a malformed generator matrix row")
            rows.append(row)
    if rows is not None:
        generators.append(
            tensor.matrix(SageZZ, expected_rows, expected_columns, sum(rows, []))
        )
    if any(generator.tensor_shape()[0] != generator.tensor_shape()[1] for generator in generators):
        raise ArithmeticError("an OSCAR centralizer-image generator is not square")
    return tuple(generators), order, invariant_rank, coinvariant_rank


def oscar_even_unimodular_primitive_embedding(gram, positive, negative):
    r"""Return a typed even-unimodular target Gram and primitive embedding tensor.

    OSCAR/Hecke's ``embed_in_unimodular`` constructs the Nikulin complement
    and gluing.  Its embedding coordinates are emitted as row images; this
    private seam transposes them into the live column-action type-``(1,1)``
    tensor before returning.
    """
    if shutil.which("julia") is None:
        raise NotImplementedError(
            "the explicit even-unimodular primitive embedding requires Julia/OSCAR"
        )
    gram_rows = _integer_tensor_rows(gram)
    program = textwrap.dedent(
        r"""
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
            return matrix(ZZ, length(rows), length(rows[1]), reduce(vcat, rows))
        end

        gram = read_int_matrix(ARGS[1])
        source = integer_lattice(; gram = change_base_ring(QQ, gram))
        positive = parse(Int, ARGS[2])
        negative = parse(Int, ARGS[3])
        target, source_in_target, _ = embed_in_unimodular(source, positive, negative)
        W = solve(basis_matrix(target), basis_matrix(source_in_target); side = :left)
        G = change_base_ring(ZZ, gram_matrix(target))
        W = change_base_ring(ZZ, W)
        println("target ", nrows(G), " ", ncols(G))
        for i in 1:nrows(G)
            println("row ", join([G[i, j] for j in 1:ncols(G)], " "))
        end
        println("embedding ", nrows(W), " ", ncols(W))
        for i in 1:nrows(W)
            println("row ", join([W[i, j] for j in 1:ncols(W)], " "))
        end
        """
    )
    with tempfile.TemporaryDirectory() as scratch:
        gram_path = Path(scratch) / "gram.txt"
        gram_path.write_text(
            "\n".join(" ".join(str(entry) for entry in row) for row in gram_rows)
            + "\n"
        )
        result = subprocess.run(
            [
                "julia",
                "--startup-file=no",
                "-e",
                program,
                str(gram_path),
                str(int(positive)),
                str(int(negative)),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip() or "OSCAR embed_in_unimodular failed"
        )
    lines = tuple(line.strip() for line in result.stdout.splitlines() if line.strip())
    sections = {}
    current = None
    shape = None
    for line in lines:
        fields = line.split()
        if fields[0] in {"target", "embedding"}:
            current = fields[0]
            shape = (int(fields[1]), int(fields[2]))
            sections[current] = [shape, []]
        elif fields[0] == "row" and current is not None:
            sections[current][1].append(tuple(SageZZ(entry) for entry in fields[1:]))
    if set(sections) != {"target", "embedding"}:
        raise RuntimeError(f"OSCAR returned malformed primitive-embedding data: {lines}")
    target_shape, target_rows = sections["target"]
    embedding_shape, embedding_rows = sections["embedding"]
    if len(target_rows) != target_shape[0] or len(embedding_rows) != embedding_shape[0]:
        raise RuntimeError("OSCAR returned incomplete primitive-embedding matrices")
    target_gram = tensor(
        SageZZ,
        (),
        target_shape,
        target_rows,
    )
    row_embedding = tensor.matrix(SageZZ, embedding_rows)
    embedding = row_embedding.dual_tensor()
    if not target_gram.pullback(embedding).is_equal_tensor(gram):
        raise ArithmeticError("OSCAR's primitive embedding does not pull back the target form")
    if abs(target_gram.det()) != 1:
        raise ArithmeticError("OSCAR's primitive-embedding target is not unimodular")
    if any(target_gram[index, index] % 2 for index in range(target_shape[0])):
        raise ArithmeticError("OSCAR's primitive-embedding target is not even")
    return target_gram, embedding


__all__ = [
    "oscar_centralizer_discriminant_image",
    "oscar_even_unimodular_primitive_embedding",
    "oscar_rational_spinor_norm_sign",
    "rational_positive_vector",
]
