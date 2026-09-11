-- First-class Stacks Project tag citations.
-- Author writes `[@stacks-0A8C]`; this rewrites the key to the single global
-- Stacks entry (The25) and follows the citation with a hyperlinked "[Tag 0A8C]"
-- resolving to the canonical tag page. Runs before citeproc, so citeproc
-- resolves The25.
--
-- The link is emitted *beside* the citation, never inside it. With
-- `link-citations: true` citeproc wraps the whole rendered citation, suffix
-- included, in an anchor to the bibliography entry; a Link placed in the suffix
-- would then be a nested anchor and HTML writers drop it silently.
function Cite(el)
  local tag
  for _, c in ipairs(el.citations) do
    local t = c.id:match("^stacks%-(%w+)$")
    if t then
      c.id = "The25"
      tag = t
    end
  end
  if not tag then
    return el
  end
  return {
    el,
    pandoc.Space(),
    pandoc.Str("["),
    pandoc.Link({pandoc.Str("Tag " .. tag)},
                "https://stacks.math.columbia.edu/tag/" .. tag),
    pandoc.Str("]"),
  }
end
