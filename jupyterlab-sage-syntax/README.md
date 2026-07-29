# JupyterLab Sage syntax extension

This JupyterLab extension maps `.sage` files to CodeMirror's Python-family syntax highlighting by registering the `sage` file extension in the editor language registry.

It does not patch JupyterLab or Sage source.
Install it into the active JupyterLab app with:

```bash
npm install
npm run build
/home/dzack/gitclones/sage-dev-allopts/local/var/lib/sage/venv-python3.14/bin/jupyter labextension install . --no-build
/home/dzack/gitclones/sage-dev-allopts/local/var/lib/sage/venv-python3.14/bin/jupyter lab build
systemctl --user restart jupyter-sagemath.service
```
