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
        -- MetaMap: part + chapters
        local part_title = pandoc.utils.stringify(entry.part)
        table.insert(blocks, pandoc.Header(2, pandoc.Str(part_title), pandoc.Attr("", {"unnumbered"}, {})))

        local items = {}
        if entry.chapters then
          for _, chap in ipairs(entry.chapters) do
            local file = pandoc.utils.stringify(chap)
            table.insert(items, pandoc.List{ chapter_link(proj_dir, file) })
          end
        end
        table.insert(blocks, pandoc.BulletList(items))
      else
        -- MetaString: bare file entry
        local file = pandoc.utils.stringify(entry)
        table.insert(blocks, pandoc.BulletList{
          pandoc.List{ chapter_link(proj_dir, file) }
        })
      end
    end

    return blocks
  end
}