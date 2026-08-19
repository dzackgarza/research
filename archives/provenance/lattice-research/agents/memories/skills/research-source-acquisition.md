---
title: Research Source Acquisition
status: active
date: 2026-05-29
---
# Research Source Acquisition

This skill is the canonical theory-source workflow for this repo.
Use it before adding, auditing, or relying on durable source material under `theory/`.

## Load with this skill

- Load `zotero-api` before querying the local Zotero cache.
- Load `zotero` only when the Zotero write API is needed.
- Load `read-arxiv-paper` when the source is on arXiv.
- Load `pdf-extraction` before invoking MinerU, SSH extraction, MinerU API, or Mistral
  OCR through `~/pdf-extraction`.
- Load `reading-pdfs` when using the local `~/pdfs` cache or Mistral OCR cache path.
- Load `research-proof-auditing` when the source is evidence for a proof, theorem,
  algorithm, or accepted mathematical claim.

## Core invariant

Every durable theory claim needs traceable primary source material.

- Keep bibliographic metadata in `theory/references/references.bib`.
- Keep the source map in `theory/references/index.md`.
- Keep reusable extracted text in `theory/references/literature/`.
- Update `theory/references/claim-map.md` when a source backs a standard definition,
  theorem, algorithm, or implementation-critical claim.
- If mathematical research in chat, plans, specs, or notes relies on an external or web
  source, record the result in a durable mathematical report memory with source links.
- Do not rely on chat history, filenames, or uncited excerpts as source authority.

## Preferred workflow

- Start inside the repo.
  Check `theory/references/index.md`, `theory/references/references.bib`,
  `theory/references/literature/`, and `theory/references/claim-map.md` before searching
  elsewhere.
- Check Zotero next. Use the local Zotero API cache for metadata, BetterBibTeX citation
  keys, existing PDFs, extracted Markdown attachments, and full-text hits.
- If Zotero needs SSH access to inspect server-side attachments or extraction outputs,
  use the SSH/Zotero workflow documented in `~/pdf-extraction/ZOTERO.md`. If credentials
  or SSH access are unavailable, stop and report the blocker instead of inventing a
  substitute source.
- Prefer primary sources over secondary summaries.
  For arXiv papers, prefer the arXiv source payload when available.
  For published papers or books, prefer DOI, publisher, official author copy, or
  edition-specific metadata.
- If no reliable extracted text exists, route extraction through `~/pdf-extraction`.
  Prefer MinerU local GPU when available, then the SSH/server path, then MinerU API,
  then Mistral OCR when appropriate.
- Never fall back to low-quality PDF extraction tools banned by the `pdf-extraction`
  policy. A bad extraction is a blocker, not a reason to silently use weaker tooling.
- Treat extracted Markdown as OCR-derived source material.
  Critical definitions, theorem statements, formulas, tables, and algorithm steps must
  be spot-checked against the PDF, arXiv source, publisher text, or another primary
  source before being used as authority.

## Repository artifacts

- Use stable citation keys from Zotero or BetterBibTeX when available.
  If no key exists, create a clear, stable key from author, year, and short title.
- Do not invent DOI, arXiv ID, publisher, page range, edition, or theorem numbering.
  Mark missing metadata explicitly and file follow-up source work if it matters.
- Store reusable extraction outputs as Markdown under `theory/references/literature/`
  with enough source provenance for another agent to identify the original paper,
  citation key, extraction method, and spot-check status.
- Do not commit large PDFs by default.
  Commit a PDF only when the user has asked for repo-local preservation or when the
  existing theory/reference policy for that source requires it.
  Otherwise record the Zotero, local-cache, DOI, arXiv, publisher, or URL path in the
  source map.
- When a source supports implementation or spec work, link it from the relevant plan,
  card, theory note, or category-spec artifact rather than leaving it only in
  `references.bib`.
- Do not leave web-backed mathematical findings only in chat.
  Capture the research outcome, scope, and source URLs in repo-local memory so later
  agents can recover the argument context after compaction or session loss.

## Follow-up handling

- If source quality is uncertain but not blocking the current task, file a tracked
  `todo` research card through the `track` skill or add a short entry to
  `.agents/TODO.md` only as a scratch receptacle for later triage.
- If citation identity, theorem interpretation, or source authority affects downstream
  work, create or update a real tracked card with context, acceptance criteria, and
  dependency notes.
- If a source choice creates policy or mathematical ambiguity, create a tracked decision
  item rather than encoding the choice silently in prose.

## Completion check

Before treating source acquisition as complete, confirm that the source has:

- A citation record or explicit metadata gap.
- A known source location.
- A known extraction path or reason extraction was unnecessary.
- A trust boundary explaining what was checked directly and what remains OCR-derived.
- Links from the theory, plan, spec, or card that will consume it.
