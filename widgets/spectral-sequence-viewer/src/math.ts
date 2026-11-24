import { mathjax } from "mathjax-full/js/mathjax.js";
import { TeX } from "mathjax-full/js/input/tex.js";
import { SVG } from "mathjax-full/js/output/svg.js";
import { browserAdaptor } from "mathjax-full/js/adaptors/browserAdaptor.js";
import { RegisterHTMLHandler } from "mathjax-full/js/handlers/html.js";
import "mathjax-full/js/input/tex/base/BaseConfiguration.js";
import "mathjax-full/js/input/tex/ams/AmsConfiguration.js";
import "mathjax-full/js/input/tex/html/HtmlConfiguration.js";

RegisterHTMLHandler(browserAdaptor());
const documentMath = mathjax.document(document, {
  InputJax: new TeX({ packages: ["base", "ams", "html"] }),
  OutputJax: new SVG({ fontCache: "none" }),
});
export function math(tex: string) {
  return documentMath.convert(tex, { display: false }) as HTMLElement;
}
