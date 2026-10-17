-- book-toc.lua
-- Shortcode: {{< book-toc >}}
-- Reads book.chapters from project metadata (pandoc AST), emits linked TOC.
-- Single source of truth: _quarto.yml.

local function extract_h1_title(proj_dir, file_path)
  local full_path = proj_dir .. "/" .. file_path
  local f = io.open(full_path, "r")
  if not f then return nil end
  local content = f:read("*a")
  f:close()
  local title = content:match("^#%s+(.-)%s*[\r\n]")
  if title then
    title = title:match("^(.-)%s*{#.*}$") or title
    title = title:gsub("\\", "")
    return title
  end
  return nil
end

local function file_to_html(file_path)
  return file_path:gsub("%.md$", ".html")
end

-- True when `file` (project-relative, as written in _quarto.yml) is the page
-- currently being rendered.
local function is_self(file)
  local input = quarto.doc.input_file
  if not input then return false end
  return input:sub(-#file) == file
end

-- An explicit Attr suppresses pandoc's automatic heading id, so the part headings
-- need one of their own -- without it the page's table of contents is dead text.
local function heading_attr(title)
  local id = title:lower():gsub("[^%w]+", "-"):gsub("^-+", ""):gsub("-+$", "")
  return pandoc.Attr(id, {"unnumbered"}, {})
end

local function chapter_link(proj_dir, file)
  local title = extract_h1_title(proj_dir, file) or file
  local html = file_to_html(file)
  return pandoc.Link(title, html)
end

return {
  ["book-toc"] = function(args, kwargs)
    local proj_dir = quarto.project.directory
    if not proj_dir then return pandoc.Null() end

    local chapters = quarto.metadata.get("book.chapters")
    if not chapters then return pandoc.Null() end

    local blocks = {}

    for _, entry in ipairs(chapters) do
      if entry.part then
        -- MetaMap: part + chapters. A part is either a literal title or, when the
        -- part has a landing page of its own, that page's path — in which case the
        -- heading is the page's own title and links to it.
        local part = pandoc.utils.stringify(entry.part)
        local part_head
        if part:match("%.md$") then
          -- Anchor on the landing page's own title, not on its path, so the id
          -- reads the same way as the literal-title parts below.
          local head_id = heading_attr(extract_h1_title(proj_dir, part) or part)
          part_head = pandoc.Header(2, chapter_link(proj_dir, part), head_id)
        else
          -- Quarto has already parsed a literal part title into inlines, and one of
          -- them carries math. Stringifying it would print the LaTeX source, and
          -- reparsing that string loses the commands -- so pass the inlines through.
          part_head = pandoc.Header(2, pandoc.Inlines(entry.part), heading_attr(part))
        end
        table.insert(blocks, part_head)

        local items = {}
        if entry.chapters then
          for _, chap in ipairs(entry.chapters) do
            local file = pandoc.utils.stringify(chap)
            table.insert(items, pandoc.List{ chapter_link(proj_dir, file) })
          end
        end
        table.insert(blocks, pandoc.BulletList(items))
      else
        -- MetaString: bare file entry. The page carrying the shortcode is itself a
        -- chapter, and listing it would link the reader back to where they are.
        local file = pandoc.utils.stringify(entry)
        if not is_self(file) then
          table.insert(blocks, pandoc.BulletList{
            pandoc.List{ chapter_link(proj_dir, file) }
          })
        end
      end
    end

    return blocks
  end
}