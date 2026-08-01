import type {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  CodeMirrorEditor,
  IEditorLanguageRegistry
} from '@jupyterlab/codemirror';
import { python } from '@codemirror/lang-python';
import { StateEffect } from '@codemirror/state';
import { ILatexTypesetter } from '@jupyterlab/rendermime';
import { createDocstringPreviewExtension } from './docstringPreview';

/**
 * Register Sage source files with JupyterLab's CodeMirror language registry using @codemirror/lang-python.
 */
const syntaxPlugin: JupyterFrontEndPlugin<void> = {
  id: '@dzack/jupyterlab-sage-syntax:plugin',
  description: 'Use Python-family CodeMirror highlighting for Sage source files.',
  autoStart: true,
  requires: [IEditorLanguageRegistry],
  activate: (_app: JupyterFrontEnd, languages: IEditorLanguageRegistry) => {
    if (languages.findByExtension('sage')) {
      return;
    }

    languages.addLanguage({
      name: 'sage',
      displayName: 'Sage',
      mime: ['text/x-sage', 'application/x-sage'],
      extensions: ['sage'],
      load: async () => {
        return python();
      }
    });
  }
};

/**
 * Reload clean file-editor documents when their on-disk model changes.
 */
const autoReloadPlugin: JupyterFrontEndPlugin<void> = {
  id: '@dzack/jupyterlab-sage-syntax:auto-reload',
  description: 'Reload file-editor documents when their on-disk file changes.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
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
const docstringPreviewPlugin: JupyterFrontEndPlugin<void> = {
  id: '@dzack/jupyterlab-sage-syntax:docstring-preview',
  description:
    'Live preview LaTeX math and double-backtick inline code inside Python/Sage docstrings.',
  autoStart: true,
  optional: [ILatexTypesetter],
  activate: (app: JupyterFrontEnd, typesetter: ILatexTypesetter | null) => {
    const ext = createDocstringPreviewExtension(typesetter);

    app.docRegistry.addWidgetExtension('Editor', {
      createNew: (widget: any, context: any) => {
        const inject = () => {
          const cmEditor = widget.content?.editor as CodeMirrorEditor | undefined;
          const view = cmEditor?.editor;
          if (view) {
            view.dispatch({
              effects: StateEffect.appendConfig.of(ext)
            });
          }
        };

        if (context.isReady) {
          inject();
        } else {
          void context.ready.then(() => {
            inject();
          });
        }

        return {
          isDisposed: false,
          dispose: () => {}
        };
      }
    });
  }
};

export default [syntaxPlugin, autoReloadPlugin, docstringPreviewPlugin];
