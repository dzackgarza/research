--[[
MIT License

Copyright (c) 2023-2026 Ute Hahn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
]]--

--[[
Writes one file `list-of-<name>.qmd` for every list named by a `listin` key.

The lists are generated from the registry (cnbx.xref), not appended chapter by
chapter. For a book the registry holds every chapter's blocks, and the rendered
chapter's own entries were replaced from its divs, so every render rewrites each
list whole: rendering a single chapter, or rendering it twice, gives the same list.
Entries are in reading order: by chapter position in book.render, then by number.

For a book the files are written at the project root, next to the registry, and
each link is the project-relative source path of its chapter ("/part/ch.md#id").
A book page shows a list with the div `::: {.listof list="<name>"} :::`; see the
note in Pandoc_makeListof for why an include of the file does not work there.
]]--

uti = require "cnb-utilities"

local ifelse = uti.ifelse

-- "12.3.4" -> {12, 3, 4}, compared entry by entry
local function numberkey(s)
  local key = {}
  for n in tostring(s or ""):gmatch("%d+") do table.insert(key, tonumber(n)) end
  return key
end

local function keyless(a, b)
  for i = 1, math.max(#a, #b) do
    local x, y = a[i] or -1, b[i] or -1
    if x ~= y then return x < y end
  end
  return false
end

local function chapterpos(info)
  if cnbx.chapterorder and info.file then
    return cnbx.chapterorder[info.file] or math.huge
  end
  return 0
end

local function before(a, b)
  local pa, pb = chapterpos(a.info), chapterpos(b.info)
  if pa ~= pb then return pa < pb end
  local ka, kb = numberkey(a.info.refnumber), numberkey(b.info.refnumber)
  if keyless(ka, kb) or keyless(kb, ka) then return keyless(ka, kb) end
  return a.id < b.id
end

local function link(id, info)
  if cnbx.isbook and info.src then return "/" .. info.src .. "#" .. id end
  return "#" .. id
end

local function entry(id, info)
  local label = info.reflabel or info.label or ""
  local number = tostring(info.refnumber or "")
  local tag = label .. ifelse(number == "", "", " " .. number)
  local title = info.mdtitle or info.md or ""
  return "\n [**" .. tag .. "**](" .. link(id, info) .. ")" ..
    ifelse(title == "", "", ": " .. title) .. "\\Pageref{" .. id .. "}\n"
end

local function collectlists()
  local lists = {}
  for id, info in pairs(cnbx.xref) do
    if type(info) == "table" then
      for _, name in ipairs(info.listin or {}) do
        lists[name] = lists[name] or {}
        table.insert(lists[name], { id = id, info = info })
      end
    end
  end

  for _, entries in pairs(lists) do table.sort(entries, before) end
  return lists
end

local function listmarkdown(entries)
  local parts = { "`\\providecommand{\\Pageref}[1]{\\hfill p.\\pageref{#1}}`{=latex}\n" }
  for _, e in ipairs(entries or {}) do table.insert(parts, entry(e.id, e.info)) end
  return table.concat(parts)
end

local function Pandoc_makeListof(doc)
  local lists = collectlists()

  -- A div `::: {.listof list="name"} :::` is replaced by that list. Quarto expands
  -- every include before it renders the first chapter, so a list file cannot be
  -- included by the render that writes it; this div is expanded when its own page
  -- is filtered, from the registry as the chapters before it left it.
  doc = doc:walk {
    Div = function(div)
      if div.classes:includes("listof") and div.attributes.list then
        return pandoc.read(listmarkdown(lists[div.attributes.list]), "markdown").blocks
      end
    end
  }

  for name, entries in pairs(lists) do
    local filename = "list-of-" .. name .. ".qmd"
    if cnbx.isbook then filename = pandoc.path.join({ cnbx.projectdir, filename }) end
    local file = io.open(filename, "w")
    if file then
      file:write(listmarkdown(entries))
      file:close()
    else
      uti.warning("cannot write to file " .. filename)
    end
  end

  return doc
end


return {
  Pandoc = Pandoc_makeListof
}
