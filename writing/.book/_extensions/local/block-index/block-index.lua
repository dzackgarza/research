-- Expands a `::: {.block-index kinds="theorem lemma"} :::` div into a list of every
-- numbered block of those kinds in the book, grouped by chapter in reading order.
--
-- The entries come from the registry that custom-numbered-blocks writes at the
-- project root (._htmlbook_xref.json): each block's label, number, chapter and
-- markdown title. That registry is never pruned, so it also holds blocks from
-- chapters that moved and blocks that were deleted. An entry is listed only when its
-- chapter is in book.chapters and the chapter source still contains `#<id>`.
--
-- A page holding this div reads the registry as the chapters before it left it. The
-- index pages therefore sit at the end of book.chapters, so a full render lists the
-- current state of every chapter.

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local s = f:read("a")
  f:close()
  return s
end

local function chapter_files(book)
  local out = {}
  local function walk(list)
    for _, item in ipairs(list or {}) do
      if type(item) == "table" and item.chapters then
        local part = pandoc.utils.stringify(item.part or "")
        if part:match("%.md$") then table.insert(out, part) end
        walk(item.chapters)
      else
        table.insert(out, pandoc.utils.stringify(item))
      end
    end
  end
  walk(book.chapters)
  return out
end

local function chapter_title(src, fallback)
  local t = src:match("^#%s+([^\n]+)") or src:match("\n#%s+([^\n]+)")
  if not t then return fallback end
  return (t:gsub("%s*{[^}]*}%s*$", ""))
end

-- "12.3.4" -> {12, 3, 4}, compared lexicographically.
local function number_key(s)
  local key = {}
  for n in tostring(s):gmatch("%d+") do table.insert(key, tonumber(n)) end
  return key
end

local function key_less(a, b)
  for i = 1, math.max(#a, #b) do
    local x, y = a[i] or -1, b[i] or -1
    if x ~= y then return x < y end
  end
  return false
end

local function build(div, meta)
  local labels = {}
  for kind in (div.attributes.kinds or ""):gmatch("%S+") do
    labels[(kind:gsub("^%l", string.upper))] = true
  end
  local projectdir = quarto.project.directory
  local registry = read_file(pandoc.path.join({ projectdir, "._htmlbook_xref.json" }))
  if not registry then
    error("block-index: " .. projectdir .. "/._htmlbook_xref.json does not exist; render the whole book")
  end
  local xref = quarto.json.decode(registry)

  local by_file = {}
  for id, info in pairs(xref) do
    if type(info) == "table" and labels[info.reflabel] and info.file then
      by_file[info.file] = by_file[info.file] or {}
      table.insert(by_file[info.file], { id = id, info = info })
    end
  end

  local md = {}
  for _, chapter in ipairs(chapter_files(meta.book)) do
    local stem = pandoc.path.split_extension(chapter)
    local entries = by_file[stem]
    local src = entries and read_file(pandoc.path.join({ projectdir, chapter }))
    if src then
      local live = {}
      for _, e in ipairs(entries) do
        if src:find("#" .. e.id, 1, true) then table.insert(live, e) end
      end
      table.sort(live, function(a, b)
        return key_less(number_key(a.info.refnumber), number_key(b.info.refnumber))
      end)
      if #live > 0 then
        table.insert(md, "## " .. chapter_title(src, stem) .. " {.unnumbered .unlisted}\n")
        for _, e in ipairs(live) do
          local title = (e.info.md and e.info.md ~= "") and (": " .. e.info.md) or ""
          table.insert(md, string.format("- [**%s %s**](%s#%s)%s",
            e.info.reflabel, e.info.refnumber, chapter, e.id, title))
        end
        table.insert(md, "")
      end
    end
  end
  return pandoc.read(table.concat(md, "\n"), "markdown").blocks
end

return {
  {
    Pandoc = function(doc)
      local blocks = pandoc.List()
      for _, b in ipairs(doc.blocks) do
        if b.t == "Div" and b.classes:includes("block-index") then
          blocks:extend(build(b, doc.meta))
        else
          blocks:insert(b)
        end
      end
      doc.blocks = blocks
      return doc
    end,
  },
}
