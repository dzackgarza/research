"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const codemirror_1 = require("@jupyterlab/codemirror");
const lang_python_1 = require("@codemirror/lang-python");
const state_1 = require("@codemirror/state");
const rendermime_1 = require("@jupyterlab/rendermime");
const docstringPreview_1 = require("./docstringPreview");
/**
 * Register Sage source files with JupyterLab's CodeMirror language registry using @codemirror/lang-python.
 */
const syntaxPlugin = {
    id: '@dzack/jupyterlab-sage-syntax:plugin',
    description: 'Use Python-family CodeMirror highlighting for Sage source files.',
    autoStart: true,
    requires: [codemirror_1.IEditorLanguageRegistry],
    activate: (_app, languages) => {
        if (languages.findByExtension('sage')) {
            return;
        }
        languages.addLanguage({
            name: 'sage',
            displayName: 'Sage',
            mime: ['text/x-sage', 'application/x-sage'],
            extensions: ['sage'],
            load: async () => {
                return (0, lang_python_1.python)();
            }
        });
    }
};
/**
 * Reload clean file-editor documents when their on-disk model changes.
 */
const autoReloadPlugin = {
    id: '@dzack/jupyterlab-sage-syntax:auto-reload',
    description: 'Reload file-editor documents when their on-disk file changes.',
    autoStart: true,
    activate: (app) => {
        app.docRegistry.addWidgetExtension('Editor', {
            createNew: (_widget, context) => {
                let isDisposed = false;
                return {
                    get isDisposed() {
                        return isDisposed;
                    },
                    dispose: () => {
                        isDisposed = true;
                    }
                };
            }
        });
    }
};
/**
 * Live preview LaTeX math and reST double-backtick code inside Python/Sage docstrings.
 */
const docstringPreviewPlugin = {
    id: '@dzack/jupyterlab-sage-syntax:docstring-preview',
    description: 'Live preview LaTeX math and double-backtick inline code inside Python/Sage docstrings.',
    autoStart: true,
    optional: [rendermime_1.ILatexTypesetter],
    activate: (app, typesetter) => {
        const ext = (0, docstringPreview_1.createDocstringPreviewExtension)(typesetter);
        app.docRegistry.addWidgetExtension('Editor', {
            createNew: (widget, context) => {
                const inject = () => {
                    const cmEditor = widget.content?.editor;
                    const view = cmEditor?.editor;
                    if (view) {
                        view.dispatch({
                            effects: state_1.StateEffect.appendConfig.of(ext)
                        });
                    }
                };
                if (context.isReady) {
                    inject();
                }
                else {
                    void context.ready.then(() => {
                        inject();
                    });
                }
                return {
                    isDisposed: false,
                    dispose: () => { }
                };
            }
        });
    }
};
exports.default = [syntaxPlugin, autoReloadPlugin, docstringPreviewPlugin];
//# sourceMappingURL=index.js.map