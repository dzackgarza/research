"use strict";
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/* eslint-disable @typescript-eslint/no-explicit-any */
/**
 * @packageDocumentation
 * @module mathjax-extension
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.MathJaxTypesetter = void 0;
const coreutils_1 = require("@lumino/coreutils");
const rendermime_1 = require("@jupyterlab/rendermime");
const coreutils_2 = require("@jupyterlab/coreutils");
const translation_1 = require("@jupyterlab/translation");
var CommandIDs;
(function (CommandIDs) {
    /**
     * Copy raw LaTeX to clipboard.
     */
    CommandIDs.copy = 'mathjax:clipboard';
    /**
     * Scale MathJax elements.
     */
    CommandIDs.scale = 'mathjax:scale';
})(CommandIDs || (CommandIDs = {}));
/**
 * The MathJax Typesetter.
 */
class MathJaxTypesetter {
    async _ensureInitialized() {
        if (!this._initialized) {
            this._mathDocument = await Private.ensureMathDocument();
            this._initialized = true;
        }
    }
    /**
     * Get an instance of the MathDocument object.
     */
    async mathDocument() {
        await this._ensureInitialized();
        return this._mathDocument;
    }
    /**
     * Typeset the math in a node.
     */
    async typeset(node) {
        try {
            await this._ensureInitialized();
        }
        catch (e) {
            console.error(e);
            return;
        }
        this._mathDocument.options.elements = [node];
        this._mathDocument.clear().render();
        delete this._mathDocument.options.elements;
        Private.hardenAnchorLinks(node);
    }
    _initialized = false;
    _mathDocument;
}
exports.MathJaxTypesetter = MathJaxTypesetter;
/**
 * The MathJax extension.
 */
const mathJaxPlugin = {
    id: '@dzack/mathjax-extension:plugin',
    description: 'Provides the LaTeX mathematical expression interpreter.',
    provides: rendermime_1.ILatexTypesetter,
    optional: [translation_1.ITranslator],
    activate: (app, translator) => {
        const trans = (translator ?? translation_1.nullTranslator).load('jupyterlab');
        const typesetter = new MathJaxTypesetter();
        app.commands.addCommand(CommandIDs.copy, {
            execute: async () => {
                const md = await typesetter.mathDocument();
                const oJax = md.outputJax;
                await navigator.clipboard.writeText(oJax.math.math);
            },
            label: trans.__('MathJax Copy Latex'),
            describedBy: {
                args: {
                    type: 'object',
                    properties: {}
                }
            }
        });
        app.commands.addCommand(CommandIDs.scale, {
            execute: async (args) => {
                const md = await typesetter.mathDocument();
                const scale = args['scale'] || 1.0;
                md.outputJax.options.scale = scale;
                md.rerender();
                // Harden only the re-rendered anchors
                for (const math of md.math) {
                    const root = math.typesetRoot;
                    if (root) {
                        Private.hardenAnchorLinks(root);
                    }
                }
            },
            label: args => trans.__('Mathjax Scale ') +
                (args['scale'] ? `x${args['scale']}` : trans.__('Reset')),
            describedBy: {
                args: {
                    type: 'object',
                    properties: {
                        scale: {
                            type: 'number',
                            description: trans.__('The scale factor for MathJax rendering')
                        }
                    }
                }
            }
        });
        return typesetter;
    },
    autoStart: true
};
exports.default = mathJaxPlugin;
/**
 * A namespace for module-private functionality.
 */
var Private;
(function (Private) {
    let _loading = null;
    async function ensureMathDocument() {
        if (!_loading) {
            _loading = new coreutils_1.PromiseDelegate();
            void Promise.resolve().then(() => __importStar(require('mathjax-full/js/input/tex/require/RequireConfiguration')));
            const [{ mathjax }, { CHTML }, { TeX }, { TeXFont }, { AllPackages }, { SafeHandler }, { HTMLHandler }, { browserAdaptor }, { AssistiveMmlHandler }] = await Promise.all([
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/mathjax'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/output/chtml'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/input/tex'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/output/chtml/fonts/tex'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/input/tex/AllPackages'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/ui/safe/SafeHandler'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/handlers/html/HTMLHandler'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/adaptors/browserAdaptor'))),
                Promise.resolve().then(() => __importStar(require('mathjax-full/js/a11y/assistive-mml')))
            ]);
            mathjax.handlers.register(AssistiveMmlHandler(SafeHandler(new HTMLHandler(browserAdaptor()))));
            class EmptyFont extends TeXFont {
                static defaultFonts = {};
            }
            const chtml = new CHTML({
                // Override dynamically generated fonts in favor of our font css
                font: new EmptyFont()
            });
            const pageBuffer = Number.parseInt(coreutils_2.PageConfig.getOption('mathjaxMaxBuffer') || '', 10);
            const maxBuffer = Number.isFinite(pageBuffer) && pageBuffer > 0 ? pageBuffer : undefined;
            const tex = new TeX({
                packages: AllPackages.concat('require'),
                inlineMath: [
                    ['$', '$'],
                    ['\\(', '\\)']
                ],
                displayMath: [
                    ['$$', '$$'],
                    ['\\[', '\\]']
                ],
                processEscapes: true,
                processEnvironments: true,
                ...(maxBuffer ? { maxBuffer } : {}),
            });
            const mathDocument = mathjax.document(window.document, {
                InputJax: tex,
                OutputJax: chtml
            });
            _loading.resolve(mathDocument);
        }
        return _loading.promise;
    }
    Private.ensureMathDocument = ensureMathDocument;
    /**
     * Utility function to harden anchor links in a given element
     */
    function hardenAnchorLinks(element) {
        const anchors = element.querySelectorAll('.MathJax a');
        anchors.forEach(anchor => {
            // Add rel="noopener" if not already present
            const existingRel = anchor.rel || '';
            const relValues = existingRel.split(/\s+/).filter(v => v.length > 0);
            if (!relValues.includes('noopener')) {
                relValues.push('noopener');
            }
            anchor.rel = relValues.join(' ');
            // Add target="_blank" if not already present
            if (anchor.target !== '_blank') {
                anchor.target = '_blank';
            }
        });
    }
    Private.hardenAnchorLinks = hardenAnchorLinks;
})(Private || (Private = {}));
//# sourceMappingURL=index.js.map