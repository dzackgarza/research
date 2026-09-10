-- First-class Stacks Project tag citations.
-- Author writes `[@stacks-0A8C]`; this rewrites the key to the single global
-- Stacks entry (The25) and appends a hyperlinked ", Tag 0A8C" resolving to the
-- canonical tag page. Runs before citeproc, so citeproc resolves The25.
function Cite(el)
  for _, c in ipairs(el.citations) do
    local tag = c.id:match("^stacks%-(%w+)$")
    if tag then
      c.id = "The25"
      c.suffix = c.suffix or {}
      table.insert(c.suffix, pandoc.Str(","))
      table.insert(c.suffix, pandoc.Space())
      table.insert(c.suffix, pandoc.Link({pandoc.Str("Tag " .. tag)},
                  "https://stacks.math.columbia.edu/tag/" .. tag))
    end
  end
  return el
end
