#!/usr/bin/env python3
"""
Export Jupyter notebook to LLM-friendly formats.

This script creates clean, structured exports that are optimized for LLM processing.
"""

import json
import argparse
import re
from pathlib import Path

def clean_code_cell(source):
    """Clean and format code cell content."""
    if isinstance(source, list):
        source = ''.join(source)
    
    # Remove magic commands that aren't useful for LLMs
    source = re.sub(r'^%.*$', '', source, flags=re.MULTILINE)
    source = re.sub(r'^!.*$', '', source, flags=re.MULTILINE)
    
    # Remove empty lines at start/end
    source = source.strip()
    
    return source

def clean_markdown_cell(source):
    """Clean and format markdown cell content."""
    if isinstance(source, list):
        source = ''.join(source)
    
    return source.strip()

def export_notebook_clean_text(notebook_path, output_path):
    """Export notebook as clean text optimized for LLMs."""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    output_lines = []
    output_lines.append(f"# Notebook: {notebook_path.name}")
    output_lines.append("=" * 60)
    output_lines.append("")
    
    cell_count = 0
    code_cell_count = 0
    markdown_cell_count = 0
    
    for cell in notebook['cells']:
        cell_count += 1
        cell_type = cell['cell_type']
        source = cell.get('source', [])
        
        if not source:
            continue
            
        if cell_type == 'markdown':
            markdown_cell_count += 1
            content = clean_markdown_cell(source)
            if content:
                output_lines.append(f"## Markdown Cell {markdown_cell_count}")
                output_lines.append("")
                output_lines.append(content)
                output_lines.append("")
                output_lines.append("-" * 40)
                output_lines.append("")
                
        elif cell_type == 'code':
            code_cell_count += 1
            content = clean_code_cell(source)
            if content:
                output_lines.append(f"## Code Cell {code_cell_count}")
                output_lines.append("")
                output_lines.append("```python")
                output_lines.append(content)
                output_lines.append("```")
                output_lines.append("")
                output_lines.append("-" * 40)
                output_lines.append("")
    
    # Add summary
    output_lines.append("# Summary")
    output_lines.append(f"- Total cells: {cell_count}")
    output_lines.append(f"- Code cells: {code_cell_count}")
    output_lines.append(f"- Markdown cells: {markdown_cell_count}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Exported clean text to: {output_path}")
    print(f"📊 Stats: {code_cell_count} code cells, {markdown_cell_count} markdown cells")

def export_notebook_code_only(notebook_path, output_path):
    """Export only code cells as a clean Python/Sage file."""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    output_lines = []
    output_lines.append(f'"""')
    output_lines.append(f'Code extracted from: {notebook_path.name}')
    output_lines.append(f'This file contains only the code cells from the notebook.')
    output_lines.append(f'"""')
    output_lines.append("")
    
    code_cell_count = 0
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = cell.get('source', [])
            if source:
                code_cell_count += 1
                content = clean_code_cell(source)
                if content:
                    output_lines.append(f"# === Code Cell {code_cell_count} ===")
                    output_lines.append("")
                    output_lines.append(content)
                    output_lines.append("")
                    output_lines.append("")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Exported code-only to: {output_path}")
    print(f"📊 Extracted {code_cell_count} code cells")

def main():
    parser = argparse.ArgumentParser(description='Export Jupyter notebook for LLM processing')
    parser.add_argument('notebook', help='Path to the Jupyter notebook')
    parser.add_argument('--format', choices=['clean', 'code', 'both'], default='both',
                       help='Export format: clean text, code only, or both')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    
    args = parser.parse_args()
    
    notebook_path = Path(args.notebook)
    output_dir = Path(args.output_dir)
    
    if not notebook_path.exists():
        print(f"❌ Notebook not found: {notebook_path}")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    base_name = notebook_path.stem
    
    if args.format in ['clean', 'both']:
        clean_output = output_dir / f"{base_name}_LLM_Clean.txt"
        export_notebook_clean_text(notebook_path, clean_output)
    
    if args.format in ['code', 'both']:
        code_output = output_dir / f"{base_name}_Code_Only.py"
        export_notebook_code_only(notebook_path, code_output)

if __name__ == '__main__':
    main() 