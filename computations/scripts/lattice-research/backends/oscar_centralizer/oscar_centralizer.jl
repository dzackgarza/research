#!/usr/bin/env julia
"""
oscar_centralizer.jl — OSCAR backend for centralizer computations.

Given a lattice (Gram matrix) and an isometry f, computes:
  1. Generators of the IMAGE of Z_{O(L)}(f) in O(A_L, D_f) via
     `image_centralizer_in_Oq` (hermitian Miranda-Morrison theory).
  2. Basis matrix of the invariant sublattice L^f = ker(f - I).
  3. Basis matrix of the coinvariant sublattice L_f = ker(f + I).

Usage:
    julia oscar_centralizer.jl <gram_file> <isometry_file> <out_file>

Input format (both files): whitespace-separated integers, one row per line.
Output format: Julia dict literal, readable via eval() in Python after
substituting Julia syntax:
    { "invariant_basis": [[...], ...],
      "coinvariant_basis": [[...], ...],
      "image_centralizer_gens": [[[...], ...], ...],
      "image_centralizer_order": N }

Note: image_centralizer_in_Oq requires the lattice to be even.
      For odd lattices the field is left empty.
"""

using Oscar

function read_int_matrix(filename)
    rows = []
    open(filename) do f
        for line in eachline(f)
            line = strip(line)
            isempty(line) && continue
            push!(rows, parse.(Int, split(line)))
        end
    end
    n = length(rows)
    m = length(rows[1])
    return matrix(ZZ, n, m, reduce(vcat, rows))
end

function mat_to_julia_list(M)
    n, m = size(M)
    rows = []
    for i in 1:n
        push!(rows, [Int(M[i, j]) for j in 1:m])
    end
    return rows
end

function main()
    length(ARGS) == 3 || error("Usage: oscar_centralizer.jl gram isometry outfile")
    gram_file, isom_file, out_file = ARGS

    G = read_int_matrix(gram_file)
    F = read_int_matrix(isom_file)

    n = nrows(G)
    G_qq = change_base_ring(QQ, G)
    F_qq = change_base_ring(QQ, F)

    L = integer_lattice(; gram = G_qq)
    Lf = integer_lattice_with_isometry(L, F_qq; check = true)

    # Invariant sublattice L^f = ker(f - I)
    inv_lat = invariant_lattice(Lf)
    inv_basis = basis_matrix(inv_lat)

    # Coinvariant sublattice L_f = ker(f + I)  [== coinvariant for involution]
    coinv_lat = coinvariant_lattice(Lf)
    coinv_basis = basis_matrix(coinv_lat)

    # Image of centralizer Z_{O(L)}(f) in O(A_L, D_f)
    # image_centralizer_in_Oq requires even lattice
    img_gens = []
    img_order = -1
    if is_even(L)
        G_img, _ = image_centralizer_in_Oq(Lf)
        img_order = Int(order(G_img))
        for g in gens(G_img)
            push!(img_gens, mat_to_julia_list(matrix(g)))
        end
    end

    # Write output as Python-parseable literal
    open(out_file, "w") do io
        println(io, "{")
        println(io, "  \"invariant_basis\": ", mat_to_julia_list(inv_basis), ",")
        println(io, "  \"coinvariant_basis\": ", mat_to_julia_list(coinv_basis), ",")
        println(io, "  \"image_centralizer_gens\": ", img_gens, ",")
        println(io, "  \"image_centralizer_order\": ", img_order)
        println(io, "}")
    end

    @info "oscar_centralizer: done" inv_rank=nrows(inv_basis) coinv_rank=nrows(coinv_basis) img_order=img_order
end

main()
