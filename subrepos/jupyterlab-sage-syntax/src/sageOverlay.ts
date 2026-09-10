/**
 * Sage-construct highlighting driven by the tree-sitter-sage grammar.
 *
 * The base Python layer stays with CodeMirror's maintained Lezer grammar;
 * this overlay recognizes exactly the Sage language delta with the same
 * grammar that drives the preamble's compiler, so Sage recognition has one
 * source of truth.
 */

import {
  Decoration,
  DecorationSet,
  EditorView,
  ViewPlugin,
  ViewUpdate,
} from "@codemirror/view";
import { Extension, RangeSetBuilder } from "@codemirror/state";
import { PageConfig, URLExt } from "@jupyterlab/coreutils";
import { Language, Parser, Query } from "web-tree-sitter";

function staticUrl(name: string): string {
  return URLExt.join(
    PageConfig.getOption("fullLabextensionsUrl"),
    "@dzack/jupyterlab-sage-syntax",
    "static",
    name,
  );
}

const HIGHLIGHTS = `
(sage_generator_assignment name: (identifier) @sage-parent)
(sage_generator_assignment generator: (identifier) @sage-generator)
(sage_symbolic_function_assignment name: (identifier) @sage-function)
(sage_symbolic_function_assignment parameter: (identifier) @sage-generator)
(sage_generator_index) @sage-number
(sage_raw_literal) @sage-number
(sage_ellipsis) @sage-operator
(sage_ellipsis_span ".." @sage-operator)
".<" @sage-operator
`;

const MARKS: Record<string, Decoration> = {
  "sage-parent": Decoration.mark({ class: "cm-sage-parent" }),
  "sage-generator": Decoration.mark({ class: "cm-sage-generator" }),
  "sage-function": Decoration.mark({ class: "cm-sage-function" }),
  "sage-number": Decoration.mark({ class: "cm-sage-number" }),
  "sage-operator": Decoration.mark({ class: "cm-sage-operator" }),
};

const sageTheme = EditorView.baseTheme({
  ".cm-sage-generator": { fontStyle: "italic" },
  ".cm-sage-parent": { fontWeight: "bold" },
  ".cm-sage-function": { fontStyle: "italic" },
  "&light .cm-sage-number": { color: "#116644" },
  "&dark .cm-sage-number": { color: "#7fd7a4" },
  "&light .cm-sage-operator": { color: "#aa22cc", fontWeight: "bold" },
  "&dark .cm-sage-operator": { color: "#d792ff", fontWeight: "bold" },
});

let loaded: Promise<{ language: Language; query: Query }> | null = null;

function loadLanguage(): Promise<{ language: Language; query: Query }> {
  if (loaded === null) {
    loaded = (async () => {
      await Parser.init({
        locateFile: () => staticUrl("web-tree-sitter.wasm"),
      });
      const language = await Language.load(staticUrl("tree-sitter-sage.wasm"));
      return { language, query: new Query(language, HIGHLIGHTS) };
    })();
  }
  return loaded;
}

class SageOverlayPlugin {
  decorations: DecorationSet = Decoration.none;
  private parser: Parser | null = null;
  private query: Query | null = null;

  constructor(view: EditorView) {
    void loadLanguage().then(({ language, query }) => {
      this.parser = new Parser();
      this.parser.setLanguage(language);
      this.query = query;
      this.decorations = this.build(view);
      // Re-render with the now-available decorations.
      view.dispatch({});
    });
  }

  update(update: ViewUpdate): void {
    if (update.docChanged || update.viewportChanged) {
      this.decorations = this.build(update.view);
    }
  }

  destroy(): void {
    this.parser?.delete();
  }

  private build(view: EditorView): DecorationSet {
    if (this.parser === null || this.query === null) {
      return Decoration.none;
    }
    const tree = this.parser.parse(view.state.doc.toString());
    if (tree === null) {
      return Decoration.none;
    }
    const builder = new RangeSetBuilder<Decoration>();
    const captures = this.query
      .captures(tree.rootNode)
      .filter((capture) => capture.name in MARKS)
      .sort(
        (a, b) =>
          a.node.startIndex - b.node.startIndex ||
          a.node.endIndex - b.node.endIndex,
      );
    let previousEnd = -1;
    for (const capture of captures) {
      if (capture.node.startIndex < previousEnd) {
        continue; // overlapping capture from a nested pattern
      }
      builder.add(
        capture.node.startIndex,
        capture.node.endIndex,
        MARKS[capture.name],
      );
      previousEnd = capture.node.endIndex;
    }
    tree.delete();
    return builder.finish();
  }
}

/**
 * CodeMirror extension highlighting Sage constructs via tree-sitter-sage.
 */
export function sageOverlay(): Extension {
  return [
    sageTheme,
    ViewPlugin.fromClass(SageOverlayPlugin, {
      decorations: (plugin) => plugin.decorations,
    }),
  ];
}
