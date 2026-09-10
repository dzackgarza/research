"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsdom_1 = require("jsdom");
// Initialize DOM environment for CodeMirror 6 ViewPlugin & WidgetType tests
const dom = new jsdom_1.JSDOM('<!DOCTYPE html><html><body><div id="editor"></div></body></html>', {
    url: 'http://localhost'
});
global.window = dom.window;
global.Window = dom.window.Window;
global.document = dom.window.document;
Object.defineProperty(global, 'navigator', {
    value: dom.window.navigator,
    writable: true,
    configurable: true
});
global.HTMLElement = dom.window.HTMLElement;
global.MutationObserver = dom.window.MutationObserver;
const rAF = (cb) => setTimeout(cb, 0);
const cAF = (id) => clearTimeout(id);
global.requestAnimationFrame = rAF;
global.cancelAnimationFrame = cAF;
dom.window.requestAnimationFrame = rAF;
dom.window.cancelAnimationFrame = cAF;
const node_assert_1 = __importDefault(require("node:assert"));
const node_test_1 = require("node:test");
const state_1 = require("@codemirror/state");
const view_1 = require("@codemirror/view");
const lang_python_1 = require("@codemirror/lang-python");
const docstringPreview_1 = require("../docstringPreview");
(0, node_test_1.describe)('Docstring Live Preview Extension Unit Tests', () => {
    function setupEditor(docText, cursorPos = 0) {
        const parent = document.createElement('div');
        document.body.appendChild(parent);
        const docstringExt = (0, docstringPreview_1.createDocstringPreviewExtension)();
        const state = state_1.EditorState.create({
            doc: docText,
            selection: { anchor: cursorPos, head: cursorPos },
            extensions: [(0, lang_python_1.python)(), docstringExt]
        });
        const view = new view_1.EditorView({ state, parent });
        return { view, parent, docstringExt };
    }
    (0, node_test_1.test)('parses and replaces inline math $f(x)=2$ when cursor is outside', () => {
        const doc = `r"""Some text $f(x) = 2$ inside docstring"""`;
        const { view, docstringExt } = setupEditor(doc, 0);
        const plugin = view.plugin(docstringExt);
        node_assert_1.default.ok(plugin, 'Plugin instance should exist');
        const decorations = plugin.decorations;
        let count = 0;
        decorations.between(0, doc.length, (from, to, value) => {
            count++;
            node_assert_1.default.strictEqual(doc.slice(from, to), '$f(x) = 2$');
            node_assert_1.default.ok(value.spec.widget instanceof docstringPreview_1.MathWidget, 'Decoration should contain a MathWidget');
            node_assert_1.default.strictEqual(value.spec.widget.latex, 'f(x) = 2');
            node_assert_1.default.strictEqual(value.spec.widget.displayMode, false);
        });
        node_assert_1.default.strictEqual(count, 1, 'Should create exactly 1 decoration replacement for inline math');
    });
    (0, node_test_1.test)('parses and replaces inline math \\(f(x) = 2\\) when cursor is outside', () => {
        const doc = `r"""Some text \\(f(x) = 2\\) inside docstring"""`;
        const { view, docstringExt } = setupEditor(doc, 0);
        const plugin = view.plugin(docstringExt);
        let count = 0;
        plugin.decorations.between(0, doc.length, (from, to, value) => {
            count++;
            node_assert_1.default.strictEqual(doc.slice(from, to), '\\(f(x) = 2\\)');
            node_assert_1.default.ok(value.spec.widget instanceof docstringPreview_1.MathWidget);
            node_assert_1.default.strictEqual(value.spec.widget.latex, 'f(x) = 2');
        });
        node_assert_1.default.strictEqual(count, 1, 'Should create exactly 1 decoration replacement for \\( \\) inline math');
    });
    (0, node_test_1.test)('parses and replaces double-backtick ``code inline`` when cursor is outside', () => {
        const doc = `r"""Some text with \`\`code inline\`\` inside docstring"""`;
        const { view, docstringExt } = setupEditor(doc, 0);
        const plugin = view.plugin(docstringExt);
        let count = 0;
        plugin.decorations.between(0, doc.length, (from, to, value) => {
            count++;
            node_assert_1.default.strictEqual(doc.slice(from, to), '``code inline``');
            node_assert_1.default.ok(value.spec.widget instanceof docstringPreview_1.InlineCodeWidget);
            const widgetDOM = value.spec.widget.toDOM();
            node_assert_1.default.strictEqual(widgetDOM.tagName, 'CODE');
            node_assert_1.default.strictEqual(widgetDOM.className, 'cm-docstring-inline-code');
            node_assert_1.default.strictEqual(widgetDOM.textContent, 'code inline');
        });
        node_assert_1.default.strictEqual(count, 1, 'Should replace double backticks with InlineCodeWidget');
    });
    (0, node_test_1.test)('click-to-edit: suppresses decoration when cursor is inside the target range', () => {
        const doc = `r"""Some text $f(x) = 2$ inside docstring"""`;
        const mathStart = doc.indexOf('$f(x) = 2$');
        const mathInsideCursor = mathStart + 3;
        const { view, docstringExt } = setupEditor(doc, mathInsideCursor);
        const plugin = view.plugin(docstringExt);
        let count = 0;
        plugin.decorations.between(0, doc.length, () => {
            count++;
        });
        node_assert_1.default.strictEqual(count, 0, 'Decoration should be suppressed while cursor is inside math range');
    });
    (0, node_test_1.test)('handles multiline framed module docstrings with display math and double backticks', () => {
        const doc = `r"""Free modules on arbitrary sets.

\`\`FreeModuleOnSet(R, S)\`\` realizes

\\[
    F_R(S)=\\{a:S\\to R\\mid \\operatorname{supp}(a)\\text{ is finite}\\}.
\\]

The set \\(S\\) is construction data.  It need not be finite, countable, or
ordered.  Finite ordered free modules are the specialization implemented by
\`\`BasedFreeModule\`\`.
"""`;
        const { view, docstringExt } = setupEditor(doc, 0);
        const plugin = view.plugin(docstringExt);
        let count = 0;
        plugin.decorations.between(0, doc.length, () => {
            count++;
        });
        node_assert_1.default.ok(count >= 4, `Expected at least 4 decorations, but found ${count}`);
    });
});
//# sourceMappingURL=docstringPreview.test.js.map