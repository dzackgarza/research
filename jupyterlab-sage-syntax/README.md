# JupyterLab Sage syntax extension

This JupyterLab extension provides three editor features for Sage source files:

- `.sage` files use CodeMirror's Python-family syntax highlighting.
- LaTeX in Python/Sage docstrings renders inline or as display mathematics. Supported
  delimiters are `$...$`, `\(...\)`, `$$...$$`, and `\[...\]`. The source delimiters
  are hidden while the preview is active and reappear when the cursor edits the span.
- reST inline literals such as ``FreeModuleOnSet(R, S)`` render as code with Python
  token highlighting. Function call targets use the current theme's definition color;
  arguments use its variable color.

The extension does not patch JupyterLab or Sage source. Install it into the active
JupyterLab app with:

```bash
npm install
npm run build
/home/dzack/gitclones/sage-dev-allopts/local/var/lib/sage/venv-python3.14/bin/jupyter labextension install . --no-build
/home/dzack/gitclones/sage-dev-allopts/local/var/lib/sage/venv-python3.14/bin/jupyter lab build
systemctl --user restart jupyter-sagemath.service
```

The extension's unit tests run with `npm test`. Browser behavior tests require the
live JupyterLab server at `http://localhost:8888` and run with:

```bash
npx playwright test e2e.behavior.test.js e2e.rendering.test.js
```
