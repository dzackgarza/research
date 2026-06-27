import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Globals to track managed server
managed_process = None
managed_port = None
managed_url = None

class IngestionHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean terminal output
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            html_path = REPO_ROOT / 'computations' / 'reports' / 'ingestion_dashboard.html'
            try:
                with open(html_path, 'rb') as f:
                    self.wfile.write(f.read())
            except OSError as e:
                self.send_error(500, f"Error reading dashboard file: {e}")
        
        elif self.path == '/api/jupyter_status':
            server = get_active_server()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            if server:
                self.wfile.write(json.dumps({
                    "status": "running",
                    "url": server["url"],
                    "port": server["port"],
                    "directory": str(server["directory"])
                }).encode('utf-8'))
            else:
                self.wfile.write(json.dumps({
                    "status": "stopped",
                    "url": None,
                    "port": None
                }).encode('utf-8'))
                
        elif self.path == '/api/notebooks':
            notebooks = get_notebooks_list()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(notebooks).encode('utf-8'))
            
        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        global managed_process, managed_port, managed_url
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        if self.path == '/api/create_notebook':
            try:
                data = json.loads(post_data.decode('utf-8'))
                filepath_str = data.get('filepath')
                template = data.get('template', 'blank')
                
                if not filepath_str:
                    self.send_error_response(400, "Missing filepath")
                    return
                
                # Safety check
                normalized_path = Path(filepath_str).relative_to(Path(filepath_str).anchor)
                target_path = (REPO_ROOT / normalized_path).resolve()
                
                if not str(target_path).startswith(str(REPO_ROOT)):
                    self.send_error_response(403, "Access denied: file path must be within the repository")
                    return
                
                # Only allow creation in specific subdirs
                allowed_prefixes = ['computations/notebooks/', 'computations/experiments/']
                is_allowed = any(str(normalized_path).startswith(prefix) for prefix in allowed_prefixes)
                if not is_allowed:
                    self.send_error_response(403, "Notebooks can only be created under computations/notebooks/ or computations/experiments/")
                    return
                
                # Check if file exists
                if target_path.exists():
                    self.send_error_response(400, "Notebook already exists at that path")
                    return
                
                # Define template content
                notebook_content = get_notebook_template(normalized_path.name, template)
                
                # Write notebook file
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with open(target_path, 'w', encoding='utf-8') as f:
                    json.dump(notebook_content, f, indent=1)
                
                # Calculate launch link if server is active
                launch_url = None
                server = get_active_server()
                if server:
                    launch_url = make_launch_url(normalized_path, server)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "path": str(normalized_path),
                    "launch_url": launch_url
                }).encode('utf-8'))
                
            except Exception as e:
                self.send_error_response(500, str(e))

        elif self.path == '/api/start_jupyter':
            try:
                data = json.loads(post_data.decode('utf-8'))
                port = int(data.get('port', 8888))
                
                # Check if running
                if managed_process and managed_process.poll() is None:
                    self.send_error_response(400, "A managed server is already running")
                    return
                
                # Launch Jupyter subprocess via uvx
                log_dir = REPO_ROOT / '.agents' / 'logs'
                log_dir.mkdir(parents=True, exist_ok=True)
                log_file_path = log_dir / 'jupyter.log'
                
                # Truncate old log
                with open(log_file_path, 'w') as lf:
                    lf.write(f"--- Jupyter Server Launching at {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                
                cmd = [
                    'uvx', '--from', 'jupyter-core', '--with', 'notebook', '--with', 'jupyter-client',
                    'jupyter', 'notebook', '--no-browser', f'--port={port}', f'--notebook-dir={REPO_ROOT}'
                ]
                
                log_file = open(log_file_path, 'a')
                managed_process = subprocess.Popen(cmd, stdout=log_file, stderr=log_file, cwd=str(REPO_ROOT))
                managed_port = port
                
                # Wait for token in log
                token_url = None
                for _ in range(30):  # Wait up to 6 seconds
                    time.sleep(0.2)
                    if log_file_path.exists():
                        with open(log_file_path, 'r') as lf:
                            log_content = lf.read()
                            urls = re.findall(r'http://(?:localhost|127\.0\.0\.1):\d+/\?token=\w+', log_content)
                            if urls:
                                token_url = urls[0]
                                break
                                
                if token_url:
                    # Clean up bahamut/127.0.0.1 to localhost
                    token_url = re.sub(r'http://(?:127\.0\.0\.1|[^:]+):', 'http://localhost:', token_url)
                    managed_url = token_url
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "success", "url": managed_url}).encode('utf-8'))
                else:
                    self.send_error_response(500, "Jupyter server started but token URL could not be parsed from logs.")
            except Exception as e:
                self.send_error_response(500, str(e))

        elif self.path == '/api/stop_jupyter':
            if managed_process and managed_process.poll() is None:
                managed_process.terminate()
                managed_process.wait(timeout=3)
                managed_process = None
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Stopped")
            else:
                self.send_error_response(400, "No managed server running")

        elif self.path == '/api/delete_notebook':
            try:
                data = json.loads(post_data.decode('utf-8'))
                filepath_str = data.get('filepath')
                if not filepath_str:
                    self.send_error_response(400, "Missing filepath")
                    return
                
                normalized_path = Path(filepath_str).relative_to(Path(filepath_str).anchor)
                target_path = (REPO_ROOT / normalized_path).resolve()
                
                if not str(target_path).startswith(str(REPO_ROOT)):
                    self.send_error_response(403, "Access denied")
                    return
                
                if not target_path.exists() or not filepath_str.endswith('.ipynb'):
                    self.send_error_response(400, "File not found or not a notebook")
                    return
                
                os.remove(target_path)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Deleted")
            except Exception as e:
                self.send_error_response(500, str(e))
        else:
            self.send_error(404, "API endpoint not found")

    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


# Helper functions
def discover_running_servers():
    try:
        res = subprocess.run([
            'uvx', '--from', 'jupyter-core', '--with', 'notebook', '--with', 'jupyter-client',
            'jupyter', 'notebook', 'list'
        ], capture_output=True, text=True, timeout=4)
        
        servers = []
        for line in res.stdout.splitlines():
            if ' :: ' in line:
                url, directory = line.split(' :: ', 1)
                servers.append({
                    "url": url.strip(),
                    "directory": Path(directory.strip()).resolve()
                })
        return servers
    except Exception:
        return []

def get_active_server():
    global managed_process, managed_port, managed_url
    # 1. First prioritize our own subprocess if active
    if managed_process and managed_process.poll() is None:
        return {
            "url": managed_url,
            "port": managed_port,
            "directory": REPO_ROOT.resolve()
        }
    
    # 2. Query environment
    servers = discover_running_servers()
    for s in servers:
        try:
            if REPO_ROOT.resolve().is_relative_to(s["directory"]):
                port_match = re.search(r':(\d+)/', s["url"])
                port = int(port_match.group(1)) if port_match else 8888
                return {
                    "url": s["url"],
                    "port": port,
                    "directory": s["directory"]
                }
        except ValueError:
            pass
    return None

def make_launch_url(notebook_rel_path, server):
    abs_notebook_path = (REPO_ROOT / notebook_rel_path).resolve()
    server_root = server["directory"]
    
    try:
        rel_to_server = abs_notebook_path.relative_to(server_root)
    except ValueError:
        rel_to_server = notebook_rel_path
        
    base_url = server["url"]
    
    if "/?token=" in base_url:
        host_part, token_part = base_url.split("/?token=", 1)
        token_str = f"?token={token_part}"
    elif "?" in base_url:
        host_part, query_part = base_url.split("?", 1)
        token_str = f"?{query_part}"
    else:
        host_part = base_url.rstrip('/')
        token_str = ""
        
    # Standardize hostname to localhost
    host_part = re.sub(r'http://(?:127\.0\.0\.1|[^:]+):', 'http://localhost:', host_part)
    
    return f"{host_part}/notebooks/{rel_to_server.as_posix()}{token_str}"

def get_notebooks_list():
    notebooks = []
    exclude_dirs = {'.git', 'node_modules', '__pycache__', '.venv', '.cache', '.worktrees'}
    
    # Get active server mapping info if any
    server = get_active_server()
    
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith('.ipynb'):
                full_path = Path(root) / file
                rel_path = full_path.relative_to(REPO_ROOT)
                stat = full_path.stat()
                
                launch_url = None
                if server:
                    launch_url = make_launch_url(rel_path, server)
                
                notebooks.append({
                    "name": file,
                    "path": str(rel_path),
                    "size_kb": round(stat.st_size / 1024, 1),
                    "modified": stat.st_mtime,
                    "launch_url": launch_url
                })
    # Sort by modification time descending
    notebooks.sort(key=lambda x: x['modified'], reverse=True)
    return notebooks

def get_notebook_template(name, template_type):
    title = name.replace('.ipynb', '').replace('-', ' ').title()
    cells = []
    
    if template_type == 'sage-lattice':
        cells = [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    "Lattice theory research calculations."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "from sage.all import *\n",
                    "# Load category specs if inside project environment\n",
                    "import sys\n",
                    "sys.path.append('projects/lattice-research')\n",
                    "print(\"SageMath environment initialized.\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Define a quadratic form matrix\n",
                    "M = matrix(ZZ, [[0, 1], [1, 0]])\n",
                    "print(M)\n",
                    "# check quadratic form properties here"
                ]
            }
        ]
    else:
        cells = [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    "Calculation scratchpad."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": []
            }
        ]
        
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "SageMath",
                "language": "sagemath",
                "name": "sagemath"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

def run(server_class=HTTPServer, handler_class=IngestionHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Jupyter Dashboard Server starting on http://localhost:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Jupyter Dashboard Server...")
        global managed_process
        if managed_process and managed_process.poll() is None:
            managed_process.terminate()
            managed_process.wait()
        print("Stopped.")

if __name__ == '__main__':
    port_to_use = 8080
    if len(sys.argv) > 1:
        try:
            port_to_use = int(sys.argv[1])
        except ValueError:
            pass
    run(port=port_to_use)
