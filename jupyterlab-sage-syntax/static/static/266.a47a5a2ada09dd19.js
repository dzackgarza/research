"use strict";(self.rspackChunk_dzack_jupyterlab_sage_syntax=self.rspackChunk_dzack_jupyterlab_sage_syntax||[]).push([[266],{646(o,r,e){var t=e(601),n=e.n(t),i=e(314),c=e.n(i)()(n());c.push([o.id,`.cm-docstring-inline-code {
  font-family: var(--jp-code-font-family, monospace);
  font-size: var(--jp-code-font-size, 13px);
  background-color: var(--jp-layout-color2, rgba(0, 0, 0, 0.05));
  color: var(--jp-content-font-color1, #212121);
  padding: 1px 5px;
  border-radius: 3px;
  border: 1px solid var(--jp-border-color2, rgba(0, 0, 0, 0.1));
}

.cm-docstring-inline-code .tok-keyword {
  color: var(--jp-mirror-editor-keyword-color, #008000);
}

.cm-docstring-inline-code .tok-atom,
.cm-docstring-inline-code .tok-bool {
  color: var(--jp-mirror-editor-atom-color, #88f);
}

.cm-docstring-inline-code .tok-number {
  color: var(--jp-mirror-editor-number-color, #008000);
}

.cm-docstring-inline-code .tok-string,
.cm-docstring-inline-code .tok-string2 {
  color: var(--jp-mirror-editor-string-color, #ba2121);
}

.cm-docstring-inline-code .tok-variableName,
.cm-docstring-inline-code .tok-variableName2 {
  color: var(--jp-mirror-editor-variable-color, #212121);
}

.cm-docstring-inline-code .tok-function {
  color: var(--jp-mirror-editor-def-color, #1e88e5);
}

.cm-docstring-inline-code .tok-typeName,
.cm-docstring-inline-code .tok-className,
.cm-docstring-inline-code .tok-definition {
  color: var(--jp-mirror-editor-def-color, #00f);
}

.cm-docstring-inline-code .tok-propertyName {
  color: var(--jp-mirror-editor-property-color, #05a);
}

.cm-docstring-inline-code .tok-operator {
  color: var(--jp-mirror-editor-operator-color, #7800c2);
}

.cm-docstring-inline-code .tok-comment {
  color: var(--jp-mirror-editor-comment-color, #408080);
}

.cm-docstring-inline-code .tok-meta {
  color: var(--jp-mirror-editor-meta-color, #a2f);
}

.cm-docstring-inline-code .tok-punctuation {
  color: var(--jp-mirror-editor-punctuation-color, #05a);
}

.cm-docstring-inline-code .tok-invalid {
  color: var(--jp-mirror-editor-error-color, #f00);
}

.cm-docstring-math-inline {
  display: inline-block;
}

.cm-docstring-math-block {
  display: block;
  margin: 0.5em 0;
  text-align: center;
}

.cm-docstring-math-hidden {
  display: none !important;
}
`,""]),e.d(r,{},{A:c})},314(o){o.exports=function(o){var r=[];return r.toString=function(){return this.map(function(r){var e="",t=void 0!==r[5];return r[4]&&(e+="@supports (".concat(r[4],") {")),r[2]&&(e+="@media ".concat(r[2]," {")),t&&(e+="@layer".concat(r[5].length>0?" ".concat(r[5]):""," {")),e+=o(r),t&&(e+="}"),r[2]&&(e+="}"),r[4]&&(e+="}"),e}).join("")},r.i=function(o,e,t,n,i){"string"==typeof o&&(o=[[null,o,void 0]]);var c={};if(t)for(var a=0;a<this.length;a++){var s=this[a][0];null!=s&&(c[s]=!0)}for(var l=0;l<o.length;l++){var d=[].concat(o[l]);t&&c[d[0]]||(void 0!==i&&(void 0===d[5]||(d[1]="@layer".concat(d[5].length>0?" ".concat(d[5]):""," {").concat(d[1],"}")),d[5]=i),e&&(d[2]&&(d[1]="@media ".concat(d[2]," {").concat(d[1],"}")),d[2]=e),n&&(d[4]?(d[1]="@supports (".concat(d[4],") {").concat(d[1],"}"),d[4]=n):d[4]="".concat(n)),r.push(d))}},r}},601(o){o.exports=function(o){return o[1]}},665(o,r,e){e.r(r);var t=e(72),n=e.n(t),i=e(825),c=e.n(i),a=e(659),s=e.n(a),l=e(56),d=e.n(l),p=e(540),u=e.n(p),m=e(113),f=e.n(m),v=e(646),g={};g.styleTagTransform=f(),g.setAttributes=d(),g.insert=s().bind(null,"head"),g.domAPI=c(),g.insertStyleElement=u(),n()(v.A,g);let y=v.A&&v.A.locals?v.A.locals:void 0;e.d(r,{},{default:y})},72(o){var r=[];function e(o){for(var e=-1,t=0;t<r.length;t++)if(r[t].identifier===o){e=t;break}return e}function t(o,t){for(var n={},i=[],c=0;c<o.length;c++){var a=o[c],s=t.base?a[0]+t.base:a[0],l=n[s]||0,d="".concat(s," ").concat(l);n[s]=l+1;var p=e(d),u={css:a[1],media:a[2],sourceMap:a[3],supports:a[4],layer:a[5]};if(-1!==p)r[p].references++,r[p].updater(u);else{var m=function(o,r){var e=r.domAPI(r);return e.update(o),function(r){r?(r.css!==o.css||r.media!==o.media||r.sourceMap!==o.sourceMap||r.supports!==o.supports||r.layer!==o.layer)&&e.update(o=r):e.remove()}}(u,t);t.byIndex=c,r.splice(c,0,{identifier:d,updater:m,references:1})}i.push(d)}return i}o.exports=function(o,n){var i=t(o=o||[],n=n||{});return function(o){o=o||[];for(var c=0;c<i.length;c++){var a=e(i[c]);r[a].references--}for(var s=t(o,n),l=0;l<i.length;l++){var d=e(i[l]);0===r[d].references&&(r[d].updater(),r.splice(d,1))}i=s}}},659(o){var r={};o.exports=function(o,e){var t=function(o){if(void 0===r[o]){var e=document.querySelector(o);if(window.HTMLIFrameElement&&e instanceof window.HTMLIFrameElement)try{e=e.contentDocument.head}catch(o){e=null}r[o]=e}return r[o]}(o);if(!t)throw Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");t.appendChild(e)}},540(o){o.exports=function(o){var r=document.createElement("style");return o.setAttributes(r,o.attributes),o.insert(r,o.options),r}},56(o,r,e){o.exports=function(o){var r=e.nc;r&&o.setAttribute("nonce",r)}},825(o){o.exports=function(o){if("u"<typeof document)return{update:function(){},remove:function(){}};var r=o.insertStyleElement(o);return{update:function(e){var t,n,i;t="",e.supports&&(t+="@supports (".concat(e.supports,") {")),e.media&&(t+="@media ".concat(e.media," {")),(n=void 0!==e.layer)&&(t+="@layer".concat(e.layer.length>0?" ".concat(e.layer):""," {")),t+=e.css,n&&(t+="}"),e.media&&(t+="}"),e.supports&&(t+="}"),(i=e.sourceMap)&&"u">typeof btoa&&(t+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(i))))," */")),o.styleTagTransform(t,r,o.options)},remove:function(){var o;null===(o=r).parentNode||o.parentNode.removeChild(o)}}}},113(o){o.exports=function(o,r){if(r.styleSheet)r.styleSheet.cssText=o;else{for(;r.firstChild;)r.removeChild(r.firstChild);r.appendChild(document.createTextNode(o))}}}}]);