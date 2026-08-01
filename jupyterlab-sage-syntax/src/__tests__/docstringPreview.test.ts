import { JSDOM } from 'jsdom';

// Initialize DOM environment for CodeMirror 6 ViewPlugin & WidgetType tests
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="editor"></div></body></html>', {
  url: 'http://localhost'
});
(global as any).window = dom.window;
(global as any).Window = dom.window.Window;
(global as any).document = dom.window.document;
Object.defineProperty(global, 'navigator', {
  value: dom.window.navigator,
  writable: true,
  configurable: true
});
(global as any).HTMLElement = dom.window.HTMLElement;
(global as any).MutationObserver = dom.window.MutationObserver;

const rAF = (cb: Function) => setTimeout(cb, 0);
const cAF = (id: any) => clearTimeout(id);
(global as any).requestAnimationFrame = rAF;
(global as any).cancelAnimationFrame = cAF;
dom.window.requestAnimationFrame = rAF as any;
dom.window.cancelAnimationFrame = cAF as any;

import assert from 'node:assert';
import { test, describe } from 'node:test';
import { EditorState } from '@codemirror/state';
import { EditorView, Decoration } from '@codemirror/view';
import { StreamLanguage } from '@codemirror/language';
import { python as legacyPythonMode } from '@codemirror/legacy-modes/mode/python';
import { python } from '@codemirror/lang-python';
import {
  createDocstringPreviewExtension,
  DocstringPreviewPluginClass,
  InlineCodeWidget,
  MathWidget
} from '../docstringPreview';

describe('Docstring Live Preview Extension Unit Tests', () => {
  function setupEditor(docText: string, cursorPos = 0) {
    const parent = document.createElement('div');
    document.body.appendChild(parent);

    const docstringExt = createDocstringPreviewExtension();
    const state = EditorState.create({
      doc: docText,
      selection: { anchor: cursorPos, head: cursorPos },
      extensions: [python(), docstringExt]
    });

    const view = new EditorView({ state, parent });
    return { view, parent, docstringExt };
  }

  test('parses and replaces inline math $f(x)=2$ when cursor is outside', () => {
    const doc = `r"""Some text $f(x) = 2$ inside docstring"""`;
    const { view, docstringExt } = setupEditor(doc, 0);

    const plugin = view.plugin(docstringExt as any) as unknown as DocstringPreviewPluginClass;
    assert.ok(plugin, 'Plugin instance should exist');

    const decorations = plugin.decorations;
    let count = 0;
    decorations.between(0, doc.length, (from: number, to: number, value: Decoration) => {
      count++;
      assert.strictEqual(doc.slice(from, to), '$f(x) = 2$');
      assert.ok(value.spec.widget instanceof MathWidget, 'Decoration should contain a MathWidget');
      assert.strictEqual((value.spec.widget as MathWidget).latex, 'f(x) = 2');
      assert.strictEqual((value.spec.widget as MathWidget).displayMode, false);
    });

    assert.strictEqual(count, 1, 'Should create exactly 1 decoration replacement for inline math');
  });

  test('parses and replaces inline math \\(f(x) = 2\\) when cursor is outside', () => {
    const doc = `r"""Some text \\(f(x) = 2\\) inside docstring"""`;
    const { view, docstringExt } = setupEditor(doc, 0);

    const plugin = view.plugin(docstringExt as any) as unknown as DocstringPreviewPluginClass;
    let count = 0;
    plugin.decorations.between(0, doc.length, (from: number, to: number, value: Decoration) => {
      count++;
      assert.strictEqual(doc.slice(from, to), '\\(f(x) = 2\\)');
      assert.ok(value.spec.widget instanceof MathWidget);
      assert.strictEqual((value.spec.widget as MathWidget).latex, 'f(x) = 2');
    });

    assert.strictEqual(count, 1, 'Should create exactly 1 decoration replacement for \\( \\) inline math');
  });

  test('parses and replaces double-backtick ``code inline`` when cursor is outside', () => {
    const doc = `r"""Some text with \`\`code inline\`\` inside docstring"""`;
    const { view, docstringExt } = setupEditor(doc, 0);

    const plugin = view.plugin(docstringExt as any) as unknown as DocstringPreviewPluginClass;
    let count = 0;
    plugin.decorations.between(0, doc.length, (from: number, to: number, value: Decoration) => {
      count++;
      assert.strictEqual(doc.slice(from, to), '``code inline``');
      assert.ok(value.spec.widget instanceof InlineCodeWidget);
      const widgetDOM = value.spec.widget.toDOM();
      assert.strictEqual(widgetDOM.tagName, 'CODE');
      assert.strictEqual(widgetDOM.className, 'cm-docstring-inline-code');
      assert.strictEqual(widgetDOM.textContent, 'code inline');
    });

    assert.strictEqual(count, 1, 'Should replace double backticks with InlineCodeWidget');
  });

  test('click-to-edit: suppresses decoration when cursor is inside the target range', () => {
    const doc = `r"""Some text $f(x) = 2$ inside docstring"""`;
    const mathStart = doc.indexOf('$f(x) = 2$');
    const mathInsideCursor = mathStart + 3;

    const { view, docstringExt } = setupEditor(doc, mathInsideCursor);
    const plugin = view.plugin(docstringExt as any) as unknown as DocstringPreviewPluginClass;

    let count = 0;
    plugin.decorations.between(0, doc.length, () => {
      count++;
    });

    assert.strictEqual(count, 0, 'Decoration should be suppressed while cursor is inside math range');
  });

  test('handles multiline framed module docstrings with display math and double backticks', () => {
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
    const plugin = view.plugin(docstringExt as any) as unknown as DocstringPreviewPluginClass;

    let count = 0;
    plugin.decorations.between(0, doc.length, () => {
      count++;
    });

    assert.ok(count >= 4, `Expected at least 4 decorations, but found ${count}`);
  });
});
