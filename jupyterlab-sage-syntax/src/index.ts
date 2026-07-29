import type {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IEditorLanguageRegistry } from '@jupyterlab/codemirror';

/**
 * Register Sage source files with JupyterLab's CodeMirror language registry.
 *
 * JupyterLab's file editor asks the CodeMirror MIME service for a language by
 * filename extension. Upstream JupyterLab registers Python for py/pyw, but not
 * Sage's sage extension, so Sage source files fall through to text/plain.
 */
const plugin: JupyterFrontEndPlugin<void> = {
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
      mime: 'text/x-sage',
      extensions: ['sage'],
      load: async () => {
        const python = await languages.getLanguage('python');
        if (!python?.support) {
          throw new Error('Python CodeMirror language is not registered.');
        }
        return python.support;
      }
    });
  }
};

export default plugin;
