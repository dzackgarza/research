"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DocstringPreviewPluginClass = exports.InlineCodeWidget = exports.MathWidget = void 0;
exports.createDocstringPreviewExtension = createDocstringPreviewExtension;
const view_1 = require("@codemirror/view");
const state_1 = require("@codemirror/state");
const lang_python_1 = require("@codemirror/lang-python");
const highlight_1 = require("@lezer/highlight");
class MathWidget extends view_1.WidgetType {
    latex;
    displayMode;
    typesetter;
    constructor(latex, displayMode, typesetter) {
        super();
        this.latex = latex;
        this.displayMode = displayMode;
        this.typesetter = typesetter;
    }
    eq(other) {
        return (other.latex === this.latex &&
            other.displayMode === this.displayMode &&
            other.typesetter === this.typesetter);
    }
    toDOM() {
        const container = document.createElement(this.displayMode ? 'div' : 'span');
        container.className = this.displayMode
            ? 'cm-docstring-math-block'
            : 'cm-docstring-math-inline';
        const delim = this.displayMode ? '$$' : '$';
        container.textContent = `${delim}${this.latex}${delim}`;
        if (this.typesetter) {
            void this.typesetter.typeset(container);
        }
        else if (typeof window?.MathJax?.typesetPromise === 'function') {
            void window.MathJax.typesetPromise([container]);
        }
        return container;
    }
    ignoreEvent(event) {
        return event.type !== 'click';
    }
}
exports.MathWidget = MathWidget;
class InlineCodeWidget extends view_1.WidgetType {
    code;
    constructor(code) {
        super();
        this.code = code;
    }
    eq(other) {
        return other.code === this.code;
    }
    toDOM() {
        const el = document.createElement('code');
        el.className = 'cm-docstring-inline-code';
        let offset = 0;
        (0, highlight_1.highlightTree)(lang_python_1.pythonLanguage.parser.parse(this.code), highlight_1.classHighlighter, (from, to, classes) => {
            if (from > offset) {
                el.append(document.createTextNode(this.code.slice(offset, from)));
            }
            const token = document.createElement('span');
            const isFunctionCall = classes.split(' ').includes('tok-variableName') && /^\s*\(/.test(this.code.slice(to));
            token.className = isFunctionCall ? `${classes} tok-function` : classes;
            token.textContent = this.code.slice(from, to);
            el.append(token);
            offset = to;
        });
        if (offset < this.code.length) {
            el.append(document.createTextNode(this.code.slice(offset)));
        }
        return el;
    }
    ignoreEvent(event) {
        return event.type !== 'click';
    }
}
exports.InlineCodeWidget = InlineCodeWidget;
class DocstringPreviewPluginClass {
    view;
    typesetter;
    decorations;
    constructor(view, typesetter) {
        this.view = view;
        this.typesetter = typesetter;
        this.decorations = this.buildDecorations(view);
    }
    update(update) {
        if (update.docChanged || update.selectionSet || update.viewportChanged) {
            this.decorations = this.buildDecorations(update.view);
        }
    }
    buildDecorations(view) {
        const builder = new state_1.RangeSetBuilder();
        const selection = view.state.selection.main;
        const cursor = selection.head;
        const doc = view.state.doc;
        const hiddenMark = view_1.Decoration.mark({ class: 'cm-docstring-math-hidden' });
        for (const { from, to } of view.visibleRanges) {
            const text = doc.sliceString(from, to);
            const matches = [];
            const docstringBlockRegex = /(?:r|u|b|rf|fr)?(?:"""([\s\S]*?)"""|'''([\s\S]*?)''')/g;
            let docstringMatch;
            while ((docstringMatch = docstringBlockRegex.exec(text)) !== null) {
                const blockStart = from + docstringMatch.index;
                const blockContent = docstringMatch[0];
                const combinedRegex = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<!\$)\$([^$\n]+?)\$(?!\$)|``([^`\n]+?)``/g;
                let m;
                while ((m = combinedRegex.exec(blockContent)) !== null) {
                    const matchStart = blockStart + m.index;
                    const matchEnd = matchStart + m[0].length;
                    let widget;
                    if (m[1] !== undefined || m[2] !== undefined) {
                        const latex = (m[1] || m[2] || '').trim();
                        widget = new MathWidget(latex, true, this.typesetter);
                    }
                    else if (m[3] !== undefined || m[4] !== undefined) {
                        const latex = (m[3] || m[4] || '').trim();
                        widget = new MathWidget(latex, false, this.typesetter);
                    }
                    else {
                        widget = new InlineCodeWidget(m[5] || '');
                    }
                    matches.push({ from: matchStart, to: matchEnd, widget });
                }
            }
            matches.sort((a, b) => a.from - b.from);
            for (const m of matches) {
                const isEditing = cursor >= m.from && cursor <= m.to;
                if (!isEditing) {
                    const lineAtStart = doc.lineAt(m.from);
                    const lineAtEnd = doc.lineAt(m.to);
                    if (lineAtStart.number === lineAtEnd.number) {
                        builder.add(m.from, m.to, view_1.Decoration.replace({ widget: m.widget }));
                    }
                    else {
                        const line1End = Math.min(lineAtStart.to, m.to);
                        builder.add(m.from, line1End, view_1.Decoration.replace({ widget: m.widget }));
                        if (line1End < m.to) {
                            builder.add(line1End, m.to, hiddenMark);
                        }
                    }
                }
            }
        }
        return builder.finish();
    }
}
exports.DocstringPreviewPluginClass = DocstringPreviewPluginClass;
function createDocstringPreviewExtension(typesetter) {
    return view_1.ViewPlugin.define(view => new DocstringPreviewPluginClass(view, typesetter), {
        decorations: plugin => plugin.decorations
    });
}
//# sourceMappingURL=docstringPreview.js.map