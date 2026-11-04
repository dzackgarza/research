# The research statement: one Markdown file to one PDF.
#
# The title and the abstract live in the file's own YAML block, and citations
# resolve against the shared Zotero export, which is the source of truth. The
# paper template and the amsthm filter belong to the pandoc-config repository at
# ~/.pandoc; when that clone is not there the stock pandoc layout is used instead,
# which is enough to check that the document compiles.
#
#   make            build ResearchStatement.pdf
#   make clean      remove it
#
# The document's mathematics uses the shared macro package (\(\Ag\), \(\latI\), ...),
# which comes from the same pandoc-config clone as the template; without it the
# LaTeX step stops at the first undefined macro. The previous recipe worked around
# that by rewriting the source through a local `pandoc_stripmacros.sh`, which is no
# longer in the tree -- build against a pandoc-config clone instead.
#
# The figures under svg-inkscape/ are the SVG sources' rendered PDFs. They are
# build inputs for the PDF, staged by hand from Inkscape, not outputs of this file.

FILENAME := ResearchStatement
PANDOC_DIR ?= $(HOME)/.pandoc
TEMPLATE := $(PANDOC_DIR)/custom/pandoc_paper_template.tex
AMSTHM := $(PANDOC_DIR)/filters/convert_amsthm_envs.lua
BIB := $(PANDOC_DIR)/bib/references.bib

FLAGS := --citeproc
ifneq ($(wildcard $(BIB)),)
FLAGS += --bibliography=$(BIB)
endif
ifneq ($(wildcard $(AMSTHM)),)
FLAGS += --lua-filter=$(AMSTHM)
endif
ifneq ($(wildcard $(TEMPLATE)),)
FLAGS += --template=$(TEMPLATE)
endif

all: $(FILENAME).pdf

$(FILENAME).pdf: $(FILENAME).md
	pandoc -f markdown+tex_math_single_backslash+table_captions+simple_tables+yaml_metadata_block+implicit_figures+link_attributes \
	  $(FILENAME).md $(FLAGS) \
	  --pdf-engine=xelatex \
	  -V date="$$(date '+%B %e, %Y')" \
	  -o $@

clean:
	rm -f $(FILENAME).pdf
	rm -rf tex_tempfiles

.PHONY: all clean
