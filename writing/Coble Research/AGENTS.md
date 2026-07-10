# Coble Paper Project - Agent Instructions

## Required Reading on Every Session Start

**READ THESE IN ORDER before taking any actions:**

1. **This file (AGENTS.md)** - You're reading it now
2. **justfile** - Contains ALL project workflows and recipes
3. **Project structure** (via `tree -L 2`)

## Critical Project Structure

```
content_latex/       LaTeX source for the paper (has inline bibliography)
content_pandoc/      Pandoc/markdown source (alternative format)
knowledge/
  ├── papers/        Full paper extractions (50KB-300KB markdown files)
  ├── meta/          Project metadata and reference lists
  └── [sections]/    Organized knowledge by topic
resources/bib/       Bibliography artifacts
global.bib          Symlink to ~/zotero_global.bib
```

## Reference Management Workflow

**When asked to "add a reference" or "add a paper":**

1. The justfile has `sync-refs` showing the pattern:
   ```bash
   just pandoc::download-arxiv ARXIV_ID BIBKEY
   ```

2. This downloads the paper and extracts it to `knowledge/papers/BIBKEY.md`

3. **DO NOT**:
   - Create stub markdown files manually
   - Add to Zotero first (user handles that separately)
   - Edit the inline LaTeX bibliography (it's maintained separately)

4. **File verification**: Papers in `knowledge/papers/` are 50KB-300KB (full extractions), not stubs

## Common Failure Modes to Avoid

1. **Reading one example and generalizing** - Check multiple files and file sizes
2. **Acting before understanding** - Read the justfile, understand the workflow
3. **Ignoring obvious patterns** - File sizes, naming conventions, directory structure
4. **Assuming tools instead of checking** - The justfile tells you what tools exist
5. **Creating files manually when recipes exist** - Always check for `just` recipes first

## Project-Specific Commands

- `just sync-refs` - Sync known references from arXiv
- `just compile-reference DIR FILE` - Extract a reference LaTeX file to markdown
- `just compile-tex` - Compile LaTeX source
- `just compile-pandoc` - Compile Pandoc source
- `just preview FILE FORMAT` - Live preview a markdown file

## When In Doubt

1. Run `just --list` to see all available recipes
2. Check `knowledge/papers/` file sizes to understand what "extraction" means
3. Read multiple example files before creating new ones
4. The justfile is the source of truth for project workflows

## TODO: Known Pipeline Issues

### Paper Extraction Quality (`pandoc::extract-ref`)

The LaTeX → Markdown extraction pipeline has known issues:

1. **Citations broken**: All `\cite{}` commands convert to "?" instead of proper citations
   - Affects ~100+ citations per paper
   - Citations need manual lookup if needed
   - TODO: Investigate if biblatex/natbib processing can be enabled

2. **Internal references broken**: Cross-references show as `[0]` instead of section numbers
   - `\ref{}` commands not resolving
   - TODO: Check if tex4ht can preserve LaTeX references or if post-processing needed

3. **Unicode handling**: make4ht throws Unicode character errors (e.g., U+25FB)
   - Errors are suppressed with `|| true` but may cause data loss
   - TODO: Verify no content is actually lost, add proper Unicode support to tex4ht config

4. **Build artifacts**: Extraction leaves many intermediate files in paper directories
   - `.aux`, `.dvi`, `.html`, `.log`, etc.
   - TODO: Add cleanup step to `extract-ref` recipe or `.gitignore` patterns

These issues don't prevent reading/understanding papers but limit their utility for precise citation work.
