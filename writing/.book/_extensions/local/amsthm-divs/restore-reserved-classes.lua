-- Undoes hide-reserved-classes.lua once Quarto's normalize stage has run.

function Div(el)
  if not el.classes:find_if(function(class) return class:match("^amsthm%-hidden%-") end) then
    return nil
  end
  el.classes = el.classes:map(function(class)
    return (class:gsub("^amsthm%-hidden%-", ""))
  end)
  return el
end
