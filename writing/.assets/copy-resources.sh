#!/usr/bin/env bash
# Copy the site's static resource trees into the render output.
#
# This stands in for `project.resources`, which cannot be used here: every part of
# the book reaches the project root as a symlink, and Quarto's resource glob does
# not walk into one, so a `resources:` entry naming any of these trees silently
# copies nothing. Explicitly named single files still work and stay in _quarto.yml.
#
# Run by Quarto as a post-render step, with the working directory at the project
# root and the output directory in QUARTO_PROJECT_OUTPUT_DIR.
set -euo pipefail

out="${QUARTO_PROJECT_OUTPUT_DIR:?post-render step run outside Quarto}"

# The interactive category diagram is an ordinary file pair, not a tree: the book page
# that embeds it is at the site root, so the iframe's `category-graph.html` has to be
# there too, whatever directory the source lives in.
for file in category-theory/lean/category-graph.html category-theory/lean/category-graph.dot; do
    [ -f "${file}" ] || { echo "copy-resources: ${file} is missing" >&2; exit 1; }
    cp -L --no-preserve=mode "${file}" "${out}/"
done

for tree in data coble/reference coble/papers; do
    [ -d "${tree}" ] || { echo "copy-resources: ${tree} is missing" >&2; exit 1; }
    mkdir -p "${out}/$(dirname "${tree}")"
    # -L dereferences the symlinked part; --no-preserve=mode keeps the output
    # world-readable regardless of the source tree's bits.
    cp -RL --no-preserve=mode "${tree}" "${out}/$(dirname "${tree}")/"
done
