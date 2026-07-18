#!/usr/bin/env python3
"""Regenerate the interactive category graph from its DOT manifest.

`docs/lean/category-graph.dot` is the source of truth (nodes = categories, edges
= the preferred forgetful/inclusion functors). This runs `dot -Tsvg` on it and
injects the SVG into a self-contained pan/zoom wrapper, producing
`docs/lean/category-graph.html`. The SVG is derived output; edit the `.dot`.
Run: `just graph`.
"""
import subprocess
from pathlib import Path

DOT = Path("docs/lean/category-graph.dot")
OUT = Path("docs/lean/category-graph.html")

svg = subprocess.run(["dot", "-Tsvg", str(DOT)], capture_output=True, text=True, check=True).stdout
svg = svg[svg.find("<svg"):]  # drop the xml/doctype preamble so <svg> embeds inline

WRAP = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Category &amp; functor graph</title>
<style>
  html,body{margin:0;height:100%;background:#fff;font-family:system-ui,sans-serif}
  #vp{position:fixed;inset:0;overflow:hidden;cursor:grab;touch-action:none}
  #vp.grabbing{cursor:grabbing}
  #world{transform-origin:0 0}
  #world svg{display:block;max-width:none;height:auto}
  #hint{position:fixed;left:10px;bottom:10px;font-size:12px;color:#6b7280;
        background:rgba(255,255,255,.9);padding:4px 8px;border:1px solid #e5e7eb;border-radius:6px}
  @media (prefers-color-scheme:dark){html,body{background:#0b0f19}
    #hint{color:#9ca3af;background:rgba(17,24,39,.9);border-color:#374151}}
</style></head>
<body>
<div id="vp"><div id="world">%SVG%</div></div>
<div id="hint">scroll to zoom &middot; drag to pan</div>
<script>
(function(){
  var vp=document.getElementById('vp'),world=document.getElementById('world');
  var s=1,x=20,y=20,down=false,px=0,py=0;
  function apply(){world.style.transform='translate('+x+'px,'+y+'px) scale('+s+')';}
  window.addEventListener('load',function(){var svg=world.querySelector('svg');
    if(!svg)return;var bb=svg.getBoundingClientRect();
    s=Math.min(vp.clientWidth/bb.width,vp.clientHeight/bb.height)*0.95||1;
    x=(vp.clientWidth-bb.width*s)/2;y=20;apply();});
  vp.addEventListener('wheel',function(e){e.preventDefault();
    var f=e.deltaY<0?1.1:1/1.1,r=vp.getBoundingClientRect(),
        mx=e.clientX-r.left,my=e.clientY-r.top;
    x=mx-(mx-x)*f;y=my-(my-y)*f;s*=f;apply();},{passive:false});
  vp.addEventListener('pointerdown',function(e){down=true;px=e.clientX;py=e.clientY;
    vp.classList.add('grabbing');vp.setPointerCapture(e.pointerId);});
  vp.addEventListener('pointermove',function(e){if(!down)return;
    x+=e.clientX-px;y+=e.clientY-py;px=e.clientX;py=e.clientY;apply();});
  vp.addEventListener('pointerup',function(){down=false;vp.classList.remove('grabbing');});
  apply();
})();
</script></body></html>"""

OUT.write_text(WRAP.replace("%SVG%", svg))
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
