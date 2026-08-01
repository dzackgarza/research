import {
  EditorView,
  ViewPlugin,
  ViewUpdate,
  Decoration,
  DecorationSet,
  WidgetType
} from '@codemirror/view';
import { RangeSetBuilder, Extension } from '@codemirror/state';
import { pythonLanguage } from '@codemirror/lang-python';
import type { ILatexTypesetter } from '@jupyterlab/rendermime';
import { classHighlighter, highlightTree } from '@lezer/highlight';

export class MathWidget extends WidgetType {
  constructor(
    readonly latex: string,
    readonly displayMode: boolean,
    readonly typesetter?: ILatexTypesetter | null
  ) {
    super();
  }

  eq(other: MathWidget): boolean {
    return (
      other.latex === this.latex &&
      other.displayMode === this.displayMode &&
      other.typesetter === this.typesetter
    );
  }

  toDOM(): HTMLElement {
    const container = document.createElement(this.displayMode ? 'div' : 'span');
    container.className = this.displayMode
      ? 'cm-docstring-math-block'
      : 'cm-docstring-math-inline';

    const delim = this.displayMode ? '$$' : '$';
    container.textContent = `${delim}${this.latex}${delim}`;

    if (this.typesetter) {
      void this.typesetter.typeset(container);
    } else if (typeof (window as any)?.MathJax?.typesetPromise === 'function') {
      void (window as any).MathJax.typesetPromise([container]);
    }

    return container;
  }

  ignoreEvent(event: Event): boolean {
    return event.type !== 'click';
  }
}

export class InlineCodeWidget extends WidgetType {
  constructor(readonly code: string) {
    super();
  }

  eq(other: InlineCodeWidget): boolean {
    return other.code === this.code;
  }

  toDOM(): HTMLElement {
    const el = document.createElement('code');
    el.className = 'cm-docstring-inline-code';

    let offset = 0;
    highlightTree(
      pythonLanguage.parser.parse(this.code),
      classHighlighter,
      (from, to, classes) => {
        if (from > offset) {
          el.append(document.createTextNode(this.code.slice(offset, from)));
        }

        const token = document.createElement('span');
        const isFunctionCall =
          classes.split(' ').includes('tok-variableName') && /^\s*\(/.test(this.code.slice(to));
        token.className = isFunctionCall ? `${classes} tok-function` : classes;
        token.textContent = this.code.slice(from, to);
        el.append(token);
        offset = to;
      }
    );

    if (offset < this.code.length) {
      el.append(document.createTextNode(this.code.slice(offset)));
    }

    return el;
  }

  ignoreEvent(event: Event): boolean {
    return event.type !== 'click';
  }
}

interface MatchItem {
  from: number;
  to: number;
  widget: WidgetType;
}

export class DocstringPreviewPluginClass {
  decorations: DecorationSet;

  constructor(readonly view: EditorView, readonly typesetter?: ILatexTypesetter | null) {
    this.decorations = this.buildDecorations(view);
  }

  update(update: ViewUpdate) {
    if (update.docChanged || update.selectionSet || update.viewportChanged) {
      this.decorations = this.buildDecorations(update.view);
    }
  }

  buildDecorations(view: EditorView): DecorationSet {
    const builder = new RangeSetBuilder<Decoration>();
    const selection = view.state.selection.main;
    const cursor = selection.head;
    const doc = view.state.doc;

    const hiddenMark = Decoration.mark({ class: 'cm-docstring-math-hidden' });

    for (const { from, to } of view.visibleRanges) {
      const text = doc.sliceString(from, to);
      const matches: MatchItem[] = [];

      const docstringBlockRegex = /(?:r|u|b|rf|fr)?(?:"""([\s\S]*?)"""|'''([\s\S]*?)''')/g;
      let docstringMatch: RegExpExecArray | null;

      while ((docstringMatch = docstringBlockRegex.exec(text)) !== null) {
        const blockStart = from + docstringMatch.index;
        const blockContent = docstringMatch[0];

        const combinedRegex = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<!\$)\$([^$\n]+?)\$(?!\$)|``([^`\n]+?)``/g;
        let m: RegExpExecArray | null;

        while ((m = combinedRegex.exec(blockContent)) !== null) {
          const matchStart = blockStart + m.index;
          const matchEnd = matchStart + m[0].length;

          let widget: WidgetType;
          if (m[1] !== undefined || m[2] !== undefined) {
            const latex = (m[1] || m[2] || '').trim();
            widget = new MathWidget(latex, true, this.typesetter);
          } else if (m[3] !== undefined || m[4] !== undefined) {
            const latex = (m[3] || m[4] || '').trim();
            widget = new MathWidget(latex, false, this.typesetter);
          } else {
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
            builder.add(m.from, m.to, Decoration.replace({ widget: m.widget }));
          } else {
            const line1End = Math.min(lineAtStart.to, m.to);
            builder.add(m.from, line1End, Decoration.replace({ widget: m.widget }));
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

export function createDocstringPreviewExtension(
  typesetter?: ILatexTypesetter | null
): Extension {
  return ViewPlugin.define(
    view => new DocstringPreviewPluginClass(view, typesetter),
    {
      decorations: plugin => plugin.decorations
    }
  );
}
