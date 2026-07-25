# Building the research report

The source is `coble_heegner_research_report.md`.  It uses ordinary Pandoc Markdown, citation keys from `coble_references.bib`, fenced-div identifiers, and Pandoc-crossref section/table/equation labels.

A typical PDF build is:

```sh
pandoc coble_heegner_research_report.md \
  --filter pandoc-crossref \
  --citeproc \
  --pdf-engine=xelatex \
  --number-sections \
  --toc \
  -o coble_heegner_research_report.pdf
```

A typical HTML build is:

```sh
pandoc coble_heegner_research_report.md \
  --filter pandoc-crossref \
  --citeproc \
  --standalone \
  --number-sections \
  --toc \
  -o coble_heegner_research_report.html
```

The report is a research ontology and proof program.
Statements labeled `Required theorem`, `Required lemma`, or `Problem` are deliberately not presented as established results.
