SHELL:=/bin/zsh
FILENAME="ResearchStatement"

## WARNING: "reset" wipes out this directory!
TEMP_DIR="/tmp/"
DATE := $(shell date '+%B %e, %Y')

latex:
	echo "Stripping macros..."
	@cat data.yaml > $(FILENAME)_stripped.md;
	cat $(FILENAME).md | pandoc_stripmacros.sh >> $(FILENAME)_stripped.md;
	echo $(DATE)
	echo "Making LaTeX...";
	cat $(FILENAME)_stripped.md | pandoc --wrap=none -r markdown+simple_tables+table_captions+yaml_metadata_block+tex_math_single_backslash+implicit_figures+link_attributes --template=$$PANDOC_DIR/custom/pandoc_paper_template.tex --lua-filter=$$PANDOC_DIR/filters/convert_amsthm_envs.lua -V date="$(DATE)" -o $(FILENAME).tex
	@rm $(FILENAME).aux -f || true;
	@rm $(FILENAME).bcf -f || true;
	@rm $(FILENAME).log -f || true;
	@rm $(FILENAME).run.xml -f || true;
	@rm $(FILENAME).toc -f || true;

all: latex
	@latexmk --shell-escape -pdf $(FILENAME).tex -quiet -outdir=tex_tempfiles && cp tex_tempfiles/$(FILENAME).pdf . 2>&1 >/dev/null;
	@rm $(FILENAME).aux -f || true;
	@rm $(FILENAME).bcf -f || true;
	@rm $(FILENAME).log -f || true;
	@rm $(FILENAME).run.xml -f || true;
	@rm $(FILENAME).toc -f || true;

.SILENT:

clean:
	@rm $(FILENAME)_stripped.md -f || true;
	@rm $(FILENAME).tex -f || true;
	@rm $(FILENAME).pdf -f || true;
	@rm tex_tempfiles -rf || true;
	@rm -rf latex.out || true;
	@rm $(FILENAME).aux -f || true;
	@rm $(FILENAME).bcf -f || true;
	@rm $(FILENAME).log -f || true;
	@rm $(FILENAME).run.xml -f || true;
	@rm $(FILENAME).toc -f || true;

.PHONY: clean

.ONESHELL:
