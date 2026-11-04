# research#219 — independent audit reconciled against source

Scope: the audit of `30df26804b` and its two supplements, checked against the three
modules and against the acceptance survey itself. The issue tree is untouched; #219 stays
where it is, open.

Result: every site the audit named is real, and every one of them is now caller-visible.
`computations/reports/sagemath_doc_search_acceptance_219.py` passes **27/27** and now
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
| `find_symbol_line_with_sage_index` (`:581`) | build failure and read failure both `(None, None)`; a matching entry with a corrupt `line:` field was dropped to the same `(None, None)` | raises `CtagsIndexError`; `(None, None)` now means only "the index has no entry for this symbol" — neither an unreadable index nor a corrupt matching entry can pose as a true negative (b21) |
| `get_primary_line_number` (`sagemath_utils.py:667`) | explicit line → ctags → invented `min(i*2+1, 100)` | explicit line → ctags → `None`; no estimate is ever presented as a line number |
| `get_primary_line_number` (`citation_utils.py:27`) | `1` when undeterminable | `None` |
| `create_file_link` (`citation_utils.py:65`) | `#L{line_number}` / `:{line_number}` with `line_number=1` by default | accepts `None` and emits no fragment instead of a guessed `#L1` |
| `create_sources_section` (`citation_utils.py:212`) | a source with no `relative_path` was emitted as a bare `unknown` line | raises `CitationSourceError(citation_id, meta)` |
| `_process_inline_citations` (`inline_citation_enhancer.py:409`) | `line_number or 1`; a dead `href="` lookup (the link is Markdown) followed by an unreachable `return` after `raise` | passes the line number through unchanged; the dead lookup and the unreachable return are gone |
| `_get_line_number` (`inline_citation_enhancer.py:453`) | `except ImportError: return 1` | the import failure propagates |
| `_add_source_list` (`inline_citation_enhancer.py:350-405`) | a document with no `relative_path` defaulted to `"unknown"` and was linked as `file://.../unknown` / `.../src/sage/unknown`, never triggering the `CitationLinkError` wrap | the same sentinel `citation_utils` rejects now fails closed up front: `CitationLinkError` carrying "no relative_path" before any link is formed (b22) |
| `convert_to_docs_url` (`citation_utils.py`) | `except ValueError: pass` guarding `parts.index("en")` | removed: the membership test on the line above makes it unreachable |

## 3. What the acceptance now proves

`python3 computations/reports/sagemath_doc_search_acceptance_219.py` → `PASS (27/27)`.
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
- **b19 closes the ctags success path**, which the previous survey left unverified. The
  builder is run for real: a stand-in `ctags` on `PATH` honours the CLI surface the
  builder uses and writes the real tags format, so our subprocess call, the `returncode ==
  0` branch, the written index and the parser are all exercised end to end. The class sits
  on line 7 of the fixture, so the returned line number proves the index was read rather
  than defaulted; a second `create_sage_ctags_index()` calls the stand-in exactly once
  more — i.e. never — proving the fresh-index branch.
- **b20 closes the runtime warning path**, which the previous survey only read. It
  executes `HayStack_Doc_Search`'s own source for its imports and function definitions
  (the app body runs at import, so importing the module would launch Streamlit), with the
  UI and the LLM generator stubbed, and then runs `index_files` on one unreadable and one
  readable file. Caller-visible result: exactly one `st.warning` carrying the path and
  `FileNotFoundError`, the readable file indexed, and on a run where nothing survives the
  return value is `{}` plus `"No documents were successfully processed."`.

## 3a. What the acceptance still does not establish

- Streamlit itself is replaced by a recorder, and `ctags` by a stand-in. The assertions are
  about *our* code's behaviour at those boundaries — that the warning is emitted with the
  reason, that the index is built, written and parsed — not about Streamlit's rendering or
  universal-ctags' own output. A run against the real app and a real ctags binary is still
  outside this survey.

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

- `HayStack_Doc_Search.index_files` is now **executed** (b20), but from its own source with
  the application body skipped and Streamlit stubbed; the surrounding app flow
  (`main`, the cache-hit path, retrieval) is still not run.
- The ctags **success** path is now executed (b19) against a stand-in executable: our
  subprocess call, success branch, index file and parser are covered; universal-ctags'
  own output format is taken as documented rather than observed.
- `find_sagemath_files`, `create_sage_ctags_index`, `find_symbol_line_with_sage_index`,
  `create_sources_section` and `sagemath_utils.get_primary_line_number` have no in-repo
  caller (`grep -rln` finds only their definitions and the acceptance survey). Their
  contract changes therefore cannot break a caller in this repository, and equally are not
  exercised by one; they are covered here as module API.
- The issue cannot be closed from this connector (read-only issues). Closure needs the
  owner to confirm the acceptance reading above.

## 6. Reproduce

```sh
python3 computations/reports/sagemath_doc_search_acceptance_219.py   # 27/27, exit 0
python3 computations/scripts/sagemath_doc_search/inline_citation_enhancer.py  # module demo
```
