"use strict";
/**
 * Sage-construct highlighting driven by the tree-sitter-sage grammar.
 *
 * The base Python layer stays with CodeMirror's maintained Lezer grammar;
 * this overlay recognizes exactly the Sage language delta with the same
 * grammar that drives the preamble's compiler, so Sage recognition has one
 * source of truth.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.sageOverlay = sageOverlay;
const view_1 = require("@codemirror/view");
const state_1 = require("@codemirror/state");
const coreutils_1 = require("@jupyterlab/coreutils");
const web_tree_sitter_1 = require("web-tree-sitter");
function staticUrl(name) {
    return coreutils_1.URLExt.join(coreutils_1.PageConfig.getOption("fullLabextensionsUrl"), "@dzack/jupyterlab-sage-syntax", "static", name);
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
const MARKS = {
    "sage-parent": view_1.Decoration.mark({ class: "cm-sage-parent" }),
    "sage-generator": view_1.Decoration.mark({ class: "cm-sage-generator" }),
    "sage-function": view_1.Decoration.mark({ class: "cm-sage-function" }),
    "sage-number": view_1.Decoration.mark({ class: "cm-sage-number" }),
    "sage-operator": view_1.Decoration.mark({ class: "cm-sage-operator" }),
};
const sageTheme = view_1.EditorView.baseTheme({
    ".cm-sage-generator": { fontStyle: "italic" },
    ".cm-sage-parent": { fontWeight: "bold" },
    ".cm-sage-function": { fontStyle: "italic" },
    "&light .cm-sage-number": { color: "#116644" },
    "&dark .cm-sage-number": { color: "#7fd7a4" },
    "&light .cm-sage-operator": { color: "#aa22cc", fontWeight: "bold" },
    "&dark .cm-sage-operator": { color: "#d792ff", fontWeight: "bold" },
});
let loaded = null;
function loadLanguage() {
    if (loaded === null) {
        loaded = (async () => {
            await web_tree_sitter_1.Parser.init({
                locateFile: () => staticUrl("web-tree-sitter.wasm"),
            });
            const language = await web_tree_sitter_1.Language.load(staticUrl("tree-sitter-sage.wasm"));
            return { language, query: new web_tree_sitter_1.Query(language, HIGHLIGHTS) };
        })();
    }
    return loaded;
}
class SageOverlayPlugin {
    decorations = view_1.Decoration.none;
    parser = null;
    query = null;
    constructor(view) {
        void loadLanguage().then(({ language, query }) => {
            this.parser = new web_tree_sitter_1.Parser();
            this.parser.setLanguage(language);
            this.query = query;
            this.decorations = this.build(view);
            // Re-render with the now-available decorations.
            view.dispatch({});
        });
    }
    update(update) {
        if (update.docChanged || update.viewportChanged) {
            this.decorations = this.build(update.view);
        }
    }
    destroy() {
        this.parser?.delete();
    }
    build(view) {
        if (this.parser === null || this.query === null) {
            return view_1.Decoration.none;
        }
        const tree = this.parser.parse(view.state.doc.toString());
        if (tree === null) {
            return view_1.Decoration.none;
        }
        const builder = new state_1.RangeSetBuilder();
        const captures = this.query
            .captures(tree.rootNode)
            .filter((capture) => capture.name in MARKS)
            .sort((a, b) => a.node.startIndex - b.node.startIndex ||
            a.node.endIndex - b.node.endIndex);
        let previousEnd = -1;
        for (const capture of captures) {
            if (capture.node.startIndex < previousEnd) {
                continue; // overlapping capture from a nested pattern
            }
            builder.add(capture.node.startIndex, capture.node.endIndex, MARKS[capture.name]);
            previousEnd = capture.node.endIndex;
        }
        tree.delete();
        return builder.finish();
    }
}
/**
 * CodeMirror extension highlighting Sage constructs via tree-sitter-sage.
 */
function sageOverlay() {
    return [
        sageTheme,
        view_1.ViewPlugin.fromClass(SageOverlayPlugin, {
            decorations: (plugin) => plugin.decorations,
        }),
    ];
}
//# sourceMappingURL=sageOverlay.js.map