import type { JupyterFrontEndPlugin } from '@jupyterlab/application';
/**
 * Register Sage source files with JupyterLab's CodeMirror language registry.
 *
 * JupyterLab's file editor asks the CodeMirror MIME service for a language by
 * filename extension. Upstream JupyterLab registers Python for py/pyw, but not
 * Sage's sage extension, so Sage source files fall through to text/plain.
 */
declare const plugin: JupyterFrontEndPlugin<void>;
export default plugin;
//# sourceMappingURL=index.d.ts.map