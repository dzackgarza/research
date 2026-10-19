-- Theorem-family citations for the book, in the syntax the pandoc papers use.
--
-- Reference implementation: ~/.pandoc/filters/convert_amsthm_envs.lua (the
-- amsenv filter) turns the same citations into cleveref commands for LaTeX.
-- This filter makes the same item-by-item decisions and emits the two
-- commands custom-numbered-blocks resolves (cnb-3-crossref.lua):
--
--   @thm:key, [@thm:key]      -->  \longref{thm:key}   ("Theorem 2.9")
--   [-@thm:key]               -->  \ref{thm:key}       ("2.9")
--   [see @thm:key, (ii)]      -->  see \longref{thm:key}, (ii)
--   [@thm:a; @lem:b]          -->  \longref{thm:a}; \longref{lem:b}
--   @def:key [@MH73, I §3.1]  -->  \longref{def:key} [@MH73, I §3.1]
--
-- cnb matches one id per command, so a cluster never merges into one command.
-- A cluster with no theorem-family key is left for citeproc. In a mixed
-- cluster, each maximal run of bibliography keys stays one Cite for
-- citeproc, set off by a space.

-- Mirrors THEOREM_FAMILY_METADATA in zettlr-pandoc
-- source/common/util/pandoc-quick-reference.ts and ref_prefixes in the
-- amsenv filter.
local ref_prefixes = {
  thm = true, lem = true, prop = true, cor = true, def = true, rmk = true,
  ex = true, conj = true, clm = true, obs = true, qst = true, prob = true,
  ass = true, warn = true, exr = true, cons = true, ["not"] = true, conv = true,
}

local function is_theorem_key(key)
  local prefix = key:match("^(%a+):.")
  return prefix ~= nil and ref_prefixes[prefix] == true
end

function Cite(el)
  local has_theorem_key = false
  for _, citation in ipairs(el.citations) do
    has_theorem_key = has_theorem_key or is_theorem_key(citation.id)
  end
  if not has_theorem_key then
    return nil
  end

  local out = pandoc.Inlines{}
  local bibliography_run = {}
  local previous = nil
  local function separator(kind)
    if previous == "theorem" and kind == "theorem" then
      out:insert(pandoc.Str(";"))
      out:insert(pandoc.Space())
    elseif previous ~= nil then
      out:insert(pandoc.Space())
    end
    previous = kind
  end
  local function flush_bibliography_run()
    if #bibliography_run > 0 then
      separator("bibliography")
      out:insert(pandoc.Cite({}, bibliography_run))
      bibliography_run = {}
    end
  end
  for _, citation in ipairs(el.citations) do
    if not is_theorem_key(citation.id) then
      table.insert(bibliography_run, citation)
    else
      flush_bibliography_run()
      separator("theorem")
      out:extend(citation.prefix)
      if #citation.prefix > 0 then
        out:insert(pandoc.Space())
      end
      local command = citation.mode == "SuppressAuthor" and "\\ref{" or "\\longref{"
      out:insert(pandoc.RawInline("tex", command .. citation.id .. "}"))
      out:extend(citation.suffix)
    end
  end
  flush_bibliography_run()
  return out
end
