local home = os.getenv("HOME")
assert(home and home ~= "", "pandoc-tikzcd.lua: HOME is not set")

local filter_environment = setmetatable({}, { __index = _G })
local filter_chunk, load_error =
  loadfile(home .. "/.pandoc/filters/tikzcd.lua", "t", filter_environment)
assert(filter_chunk, load_error)
filter_chunk()

local render_raw_block = assert(
  filter_environment.RawBlock,
  "pandoc-tikzcd.lua: canonical filter did not define RawBlock"
)

return {
  {
    Pandoc = function(document)
      return document:walk({
        RawBlock = render_raw_block,
      })
    end,
  },
}
