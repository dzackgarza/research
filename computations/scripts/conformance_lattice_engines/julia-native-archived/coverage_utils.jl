# coverage_utils.jl — runtime coverage guard for Julia/Oscar test files.
#
# Mirrors the Python conftest.py pattern: introspect an actual Oscar object
# to discover its available methods, then compare against `# method: <name>`
# tags in the test file.  Ground truth comes from the live runtime, not from
# a hand-maintained list.

# ── Infrastructure names to ignore (Julia/Oscar plumbing, not API surface) ──

const GLOBAL_IRRELEVANT = Set{Symbol}([
    # Julia builtins / Base overloads
    :show, :print, :display, :hash, :==, :isequal, :copy, :deepcopy,
    :convert, :promote_rule, :eltype, :iterate, :length, :size,
    :getindex, :setindex!, :firstindex, :lastindex,
    # Oscar/AbstractAlgebra plumbing
    :parent, :parent_type, :elem_type, :base_ring, :base_ring_type,
    :check_parent, :expressify,
    # Serialization
    :save, :load,
])

"""
    runtime_methods(sample, module_prefixes; extra_irrelevant) -> Set{String}

Discover callable method names that dispatch on `typeof(sample)` and whose
defining module starts with one of `module_prefixes`.  Filters out private
names (leading `_`) and infrastructure names.
"""
function runtime_methods(
    sample;
    module_prefixes::Vector{String} = ["Hecke", "Oscar", "Nemo", "AbstractAlgebra"],
    extra_irrelevant::Set{Symbol} = Set{Symbol}(),
)
    T = typeof(sample)
    irrelevant = union(GLOBAL_IRRELEVANT, extra_irrelevant)
    found = Set{String}()

    for m in methodswith(T; supertypes=true)
        fname = m.name
        # skip private / irrelevant
        fname in irrelevant && continue
        s = string(fname)
        startswith(s, '_') && continue

        # check defining module
        mod = m.module
        modname = string(mod)
        any(p -> startswith(modname, p), module_prefixes) || continue

        push!(found, s)
    end
    return found
end

"""
    covered_methods(filepath::String) -> Set{String}

Parse a Julia test file and return the set of method names found in
`# method: <name>` comment lines.  Strips parenthesised signatures so that
`# method: genus(L::ZZLat)` and `# method: genus` both register as `"genus"`.
"""
function covered_methods(filepath::String)
    methods = Set{String}()
    for line in eachline(filepath)
        m = match(r"#\s*method:\s*(.+)", line)
        if m !== nothing
            raw = strip(m.captures[1])
            raw == "runtime_coverage" && continue  # skip the guard's own tag
            # normalise: drop everything from first '(' onward
            name = replace(raw, r"\(.*" => "")
            # also drop type annotations like "::ZZMatrix"
            name = replace(name, r"::.*" => "")
            push!(methods, strip(name))
        end
    end
    return methods
end

"""
    assert_runtime_methods_covered(filepath, sample; kwargs...)

Fail with a detailed message listing every runtime method on `sample` that
has no corresponding `# method:` tag in the test file.
"""
function assert_runtime_methods_covered(
    filepath::String,
    sample;
    module_prefixes::Vector{String} = ["Hecke", "Oscar", "Nemo", "AbstractAlgebra"],
    extra_irrelevant::Set{Symbol} = Set{Symbol}(),
)
    relevant = runtime_methods(
        sample;
        module_prefixes = module_prefixes,
        extra_irrelevant = extra_irrelevant,
    )
    covered = covered_methods(filepath)
    uncovered = sort(collect(setdiff(relevant, covered)))

    if !isempty(uncovered)
        error(
            "Coverage failure in $(basename(filepath)):\n" *
            "  Relevant runtime methods: $(length(relevant))\n" *
            "  Covered by tests:         $(length(covered))\n" *
            "  Uncovered ($(length(uncovered))):\n" *
            join(["    - $m" for m in uncovered], "\n")
        )
    end
end
