# research#219 — independent audit reconciled against source

Scope: the audit of `30df26804b` and its two supplements, checked against the three
modules and against the acceptance survey itself. The issue tree is untouched; #219 stays
where it is, open.

Result: every site the audit named is real, and every one of them is now caller-visible.
`computations/reports/sagemath_doc_search_acceptance_219.py` passes **19/19** and now
exercises the audited `_add_source_list` catch directly.

## 1. The audit's claims, checked

All six line references the audit gave match the sites it described in `30df268`, byte for
byte. The audit was accurate; nothing in it was a misreading.

| Audit claim | Verdict | Source at `30df268` |
| --- | --- | --- |
| The new test triggers `_process_inline_citations` first, so it never exercises the fixed `_add_source_list` catch | **Confirmed** | `inline_citation_enhancer.py`: `_add_source_list` converts the citation map and calls `_process_inline_citations` before the source loop. The old survey passed `"answer (src1)."`, so the `(src1)` marker matched, `create_file_link` raised inside `replace_citation`, and the `CitationLinkError` was already formed one frame below the catch under test. |
| `sagemath_utils.py:552-555` discards ctags read errors into `(None, None)`, then heuristics | **Confirmed** | `except Exception: print(...)` → `return None, None`; `get_primary_line_number` then fell through to `min(i*2+1, 100)` — an invented line number, indistinguishable from a real one, cited as `#L<n>`. |
| Sage path missing returns `[]` | **Confirmed** | `find_sagemath_files`: `print("Warning: ...")` → `return []`, which is what a search over an empty corpus also returns. |
| File errors warn and skip (`225-227`, `259-262`) | **Confirmed** | The skip itself is justified (bulk tree walk), but the reason went to stdout only: the caller could not tell "no files matched" from "files matched and could not be read". |
| `485-493`: ctags exceptions become `False` | **Confirmed** | `TimeoutExpired`, `FileNotFoundError`, `Exception` → `print` → `return False`; the caller only learned "no index", never why. |
| `35-38`: `SyntaxError` fallback without a recovery indicator | **Confirmed** | `except SyntaxError: return extract_raw_content_enhanced(...)` — a raw-text scan was returned as if it were rendered docstrings. Genuine recovery for `.pyx`/`.sage`, but invisible. |
| inline `_get_line_number:479-480`: `ImportError` becomes line 1 | **Confirmed** | `except ImportError: return 1` — a broken installation was reported as "line 1 of this file". |

## 2. What changed, site by site

Recovery that the input justifies is kept, and is carried on the result so the caller can
distinguish it from success. Everything else raises a typed error naming the path and the
cause.

| Boundary | Before | Now |
| --- | --- | --- |
| `extract_python_docstrings` (`sagemath_utils.py:88`) | raises `DocumentationReadError` on a failed read; returns a plain `str` for every fallback | raises as before; returns `ExtractedDocumentation(str)` carrying `extraction` ∈ `docstrings` / `raw-no-docstrings` / `raw-syntax-error` / `empty-file` and `recovered_from` (the `SyntaxError`) |
| `find_sagemath_files` (`:293`) | `[]` on a missing Sage root; skips printed | raises `DocumentationReadError`; per-file skips carried on `SageFileCatalog.skipped` as `(path, exception)`, with `raise_if_nothing_read()` to escalate a scan that read nothing |
| `create_sage_ctags_index` (`:507`) | `False` on every failure, reason printed | raises `CtagsIndexError(index_path, cause)`; `True` only when a usable index exists |
| `find_symbol_line_with_sage_index` (`:581`) | build failure and read failure both `(None, None)` | raises `CtagsIndexError`; `(None, None)` now means only "the index has no entry for this symbol" |
| `get_primary_line_number` (`sagemath_utils.py:667`) | explicit line → ctags → invented `min(i*2+1, 100)` | explicit line → ctags → `None`; no estimate is ever presented as a line number |
| `get_primary_line_number` (`citation_utils.py:27`) | `1` when undeterminable | `None` |
| `create_file_link` (`citation_utils.py:65`) | `#L{line_number}` / `:{line_number}` with `line_number=1` by default | accepts `None` and emits no fragment instead of a guessed `#L1` |
| `create_sources_section` (`citation_utils.py:212`) | a source with no `relative_path` was emitted as a bare `unknown` line | raises `CitationSourceError(citation_id, meta)` |
| `_process_inline_citations` (`inline_citation_enhancer.py:409`) | `line_number or 1`; a dead `href="` lookup (the link is Markdown) followed by an unreachable `return` after `raise` | passes the line number through unchanged; the dead lookup and the unreachable return are gone |
| `_get_line_number` (`inline_citation_enhancer.py:453`) | `except ImportError: return 1` | the import failure propagates |
| `convert_to_docs_url` (`citation_utils.py`) | `except ValueError: pass` guarding `parts.index("en")` | removed: the membership test on the line above makes it unreachable |

## 3. What the acceptance now proves

`python3 computations/reports/sagemath_doc_search_acceptance_219.py` → `PASS (19/19)`.
Each check is one boundary, and each one asserts the *caller-visible* consequence.

- **b15 is the audited one.** It reaches `_add_source_list` twice — through
  `post_process_response_citations` with a response that is long and citation-free (so the
  short-response path does not inject a `(srcN)`), and by calling `_add_source_list`
  directly — and asserts that the `CitationLinkError` was **formed in `_add_source_list`**
  by inspecting the innermost traceback frame. With the old response text the same
  assertion names `replace_citation`, i.e. the old survey could not have passed it.
- b16 pins the other boundary: the same text *with* a `(src1)` marker is formed in
  `replace_citation`. The two checks together are what make the two catches separable.
- b2/b3/b4 pin the three recoveries as flagged rather than silent; b6 pins the per-file
  skip and its escalation; b8/b9 separate "no entry" from "no usable index".
- b18 pins that search and citation output still work: source list with a local-file link
  and a rendered documentation URL, and inline markers resolving to those entries.

## 4. Deliberate non-changes

- **Inline markers still resolve to `#ref-…`.** `create_file_link` returns Markdown, so the
  `href="` lookup could never match and the "direct link" branch was dead; but rewriting
  the marker to the `file://` URL would trade an anchor that always resolves for one a
  browser may refuse to follow, in a Streamlit page I cannot render here. The dead lookup
  and its misleading comment are gone and the code now states what it does. #219 is about
  error visibility, not link targets; this is flagged, not changed.
- **`citation_utils.create_citation_link` still computes a link and discards it.** It has no
  caller anywhere in the repository (checked with `grep -rln`). Dead code, no failure
  discarded; left alone rather than folded into this change.
- **`HayStack_Doc_Search.index_files` keeps its per-file `except Exception`.** That is a
  justified bulk-scan recovery, and it already surfaces the reason:
  `st.warning(f"Could not process file {file_path}: {e}")`, plus
  `st.warning("No documents were successfully processed.")` when nothing survives.

## 5. Limits of this verification

- `HayStack_Doc_Search.py` is compiled but **not executed**: it needs Streamlit and a live
  pipeline. Its failure handling was verified by reading it, not by running it.
- The ctags **success** path is untested: this VM has no `ctags` binary and no Sage tree.
  Only the build-failure and read-failure paths are exercised (b7, b8).
- `find_sagemath_files`, `create_sage_ctags_index`, `find_symbol_line_with_sage_index`,
  `create_sources_section` and `sagemath_utils.get_primary_line_number` have no in-repo
  caller (`grep -rln` finds only their definitions and the acceptance survey). Their
  contract changes therefore cannot break a caller in this repository, and equally are not
  exercised by one; they are covered here as module API.
- The issue cannot be closed from this connector (read-only issues). Closure needs the
  owner to confirm the acceptance reading above.

## 6. Reproduce

```sh
python3 computations/reports/sagemath_doc_search_acceptance_219.py   # 19/19, exit 0
python3 computations/scripts/sagemath_doc_search/inline_citation_enhancer.py  # module demo
```
