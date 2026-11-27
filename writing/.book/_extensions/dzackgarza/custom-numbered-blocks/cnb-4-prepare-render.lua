
require("cnb-global")
uti = require("cnb-utilities")
local warning = uti.warning 

local tablecontains = uti.tablecontains

local filterAttributes = function(el)
  local id = el.identifier
  local rattribs
  local norattribs
  local ignoreargs
  
  local info = cnbx.xref[id]  
  if info == nil then
      return(el)
  end

  local cls = info.cnbclass

  local clopt = cnbx.classDefaults[cls]
  local elementattribs = {}

  rattribs = {}
  norattribs = {}
  local norendero = {"label", "reflabel", "tag", "appearance", "container", "listin"}
  for k, v in pairs(el.attributes) do
    if tablecontains(norendero, k) then
        norattribs[k] = v
    else rattribs[k] = v
    end
  end  
  
  ignoreargs = ""
  local quotek = ""
  local ignoreo = {"container", "boxtype", "color", "colors", "appearance"}
  for k,_ in pairs(norattribs) do
    if tablecontains(ignoreo, k) then
      quotek = '"'..k..'"'
      if ignoreargs =="" then ignoreargs = quotek 
          else ignoreargs = ignoreargs ..", "..quotek end
       norattribs[k] = nil
    end
  end  
  
  if ignoreargs ~=""  then
    warning("elementwise attributes for block "..id..": "..ignoreargs..
      " are ignored. These can only be specified by class (or group, appearance)")
  end
  
  elementattribs = deepcopy(clopt)
  elementattribs = uti.updateTable(elementattribs, rattribs)

  local bty = elementattribs.boxtype
  info.boxtype = bty
  info.renderoptions = subtable(elementattribs, keynames(cnbx.boxtypes[bty].defaultOptions))
  
end  

local makeblocktitle = function(el)
  local id = el.identifier
  local info = cnbx.xref[id]  
  local pandoctitle = {}
  if info == nil then
      return(el)
  end
  if info.mdtitle ~= "" then 
    el1 = el.content[1]
    if el1.t=="Header" then 
      pandoctitle = el1.content
        table.remove(el.content, 1) 
      else 
      local blocks = pandoc.read("x " .. info.mdtitle, "markdown").blocks
      pandoctitle = blocks[1].content
      table.remove(pandoctitle, 1)
      table.remove(pandoctitle, 1)
    end
  end
  info.pandoctitle = pandoctitle
  return(el)
end  


return {
  Div = function(el)
    el = makeblocktitle(el)
    filterAttributes(el)
    return(el)
  end , 
  Pandoc = function(doc)
    return(doc)
  end  
}
