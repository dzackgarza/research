"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const codemirror_1 = require("@jupyterlab/codemirror");
const apputils_1 = require("@jupyterlab/apputils");
const lang_python_1 = require("@codemirror/lang-python");
const state_1 = require("@codemirror/state");
const rendermime_1 = require("@jupyterlab/rendermime");
const docstringPreview_1 = require("./docstringPreview");
/**
 * Register Sage source files with JupyterLab's CodeMirror language registry using @codemirror/lang-python.
 */
const syntaxPlugin = {
    id: "@dzack/jupyterlab-sage-syntax:plugin",
    description: "Use Python-family CodeMirror highlighting for Sage source files.",
    autoStart: true,
    requires: [codemirror_1.IEditorLanguageRegistry],
    activate: (_app, languages) => {
        if (languages.findByExtension("sage")) {
            return;
        }
        languages.addLanguage({
            name: "sage",
            displayName: "Sage",
            mime: ["text/x-sage", "application/x-sage"],
            extensions: ["sage"],
            load: async () => {
                return (0, lang_python_1.python)();
            },
        });
    },
};
/**
 * Reload clean file-editor documents when their on-disk model changes.
 *
 * If the open editor is dirty, show the standard JupyterLab confirmation dialog
 * before replacing the editor contents with the version on disk.
 */
const autoReloadPlugin = {
    id: "@dzack/jupyterlab-sage-syntax:auto-reload",
    description: "Reload file-editor documents when their on-disk file changes.",
    autoStart: true,
    activate: (app) => {
        app.docRegistry.addWidgetExtension("Editor", {
            createNew: (_widget, context) => {
                const intervalMs = 1000;
                let isDisposed = false;
                let isChecking = false;
                let promptOpen = false;
                let lastKnownModified = context.contentsModel?.last_modified ?? null;
                let lastPromptedModified = null;
                context.fileChanged.connect((_sender, model) => {
                    lastKnownModified = model.last_modified;
                    lastPromptedModified = null;
                });
                const checkForDiskChange = async () => {
                    if (isDisposed || isChecking || !context.isReady) {
                        return;
                    }
                    isChecking = true;
                    try {
                        await context.ready;
                        if (isDisposed) {
                            return;
                        }
                        const latest = await app.serviceManager.contents.get(context.path, {
                            content: false,
                        });
                        const latestModified = latest.last_modified;
                        if (!latestModified || latestModified === lastKnownModified) {
                            return;
                        }
                        if (!context.model.dirty) {
                            await context.revert();
                            lastKnownModified =
                                context.contentsModel?.last_modified ?? latestModified;
                            lastPromptedModified = null;
                            return;
                        }
                        if (promptOpen || lastPromptedModified === latestModified) {
                            return;
                        }
                        promptOpen = true;
                        lastPromptedModified = latestModified;
                        const result = await (0, apputils_1.showDialog)({
                            title: "File Changed on Disk",
                            body: `"${context.path}" changed on disk. Reload from disk and discard unsaved editor changes?`,
                            buttons: [
                                apputils_1.Dialog.cancelButton({ label: "Keep Editing" }),
                                apputils_1.Dialog.warnButton({
                                    label: "Reload from Disk",
                                    actions: ["reload"],
                                }),
                            ],
                        });
                        promptOpen = false;
                        if (isDisposed) {
                            return;
                        }
                        if (result.button.actions.includes("reload")) {
                            await context.revert();
                            lastKnownModified =
                                context.contentsModel?.last_modified ?? latestModified;
                            lastPromptedModified = null;
                        }
                    }
                    catch (error) {
                        promptOpen = false;
                        console.warn("Unable to check file for on-disk changes.", error);
                    }
                    finally {
                        isChecking = false;
                    }
                };
                const timer = window.setInterval(() => {
                    void checkForDiskChange();
                }, intervalMs);
                return {
                    get isDisposed() {
                        return isDisposed;
                    },
                    dispose: () => {
                        if (isDisposed) {
                            return;
                        }
                        isDisposed = true;
                        window.clearInterval(timer);
                    },
                };
            },
        });
    },
};
/**
 * Live preview LaTeX math and reST double-backtick code inside Python/Sage docstrings.
 */
const docstringPreviewPlugin = {
    id: "@dzack/jupyterlab-sage-syntax:docstring-preview",
    description: "Live preview LaTeX math and double-backtick inline code inside Python/Sage docstrings.",
    autoStart: true,
    optional: [rendermime_1.ILatexTypesetter],
    activate: (app, typesetter) => {
        const ext = (0, docstringPreview_1.createDocstringPreviewExtension)(typesetter);
        app.docRegistry.addWidgetExtension("Editor", {
            createNew: (widget, context) => {
                const inject = () => {
                    const cmEditor = widget.content?.editor;
                    const view = cmEditor?.editor;
                    if (view) {
                        view.dispatch({
                            effects: state_1.StateEffect.appendConfig.of(ext),
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
                    dispose: () => { },
                };
            },
        });
    },
};
exports.default = [syntaxPlugin, autoReloadPlugin, docstringPreviewPlugin];
//# sourceMappingURL=index.js.map