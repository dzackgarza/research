-- Keeps ::: {.remark #rmk:key} a custom-numbered-blocks block, as in the
-- pandoc papers.
--
-- Quarto reserves the classes in `proof_types` (quarto_cli
-- share/filters/main.lua: proof, remark, solution). Its normalize stage turns
-- a div with such a class into a Proof node, and its crossref stage then
-- fails on an amsenv id such as #rmk:key, which has no "type-" prefix.
-- User filters run after normalize by default, so custom-numbered-blocks
-- never sees the div. This filter runs at pre-ast, before normalize, and
-- renames each reserved class that is also a custom-numbered-blocks class;
-- restore-reserved-classes.lua renames it back at pre-quarto, before
-- custom-numbered-blocks runs.

local quarto_proof_types = { proof = true, remark = true, solution = true }
local hidden = {}

return {
  {
    Meta = function(meta)
      local cnb = meta["custom-numbered-blocks"]
      for class, _ in pairs(cnb and cnb.classes or {}) do
        if quarto_proof_types[class] then
          hidden[class] = true
        end
      end
    end,
  },
  {
    Div = function(el)
      if not el.classes:find_if(function(class) return hidden[class] end) then
        return nil
      end
      el.classes = el.classes:map(function(class)
        return hidden[class] and ("amsthm-hidden-" .. class) or class
      end)
      return el
    end,
  },
}
