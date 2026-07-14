#!/usr/bin/env python3
"""
Utility functions for SageMath documentation processing.
This module contains functions that can be used independently of Streamlit.
"""

import ast
import os
from pathlib import Path
from typing import Any


def extract_python_docstrings(file_path: Path) -> str:
    """Extract docstrings and class/function definitions from Python files with enhanced SageMath support."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Skip empty files
        if not content.strip():
            return ""

        lines = content.split("\n")

        # Parse the AST to extract docstrings
        try:
            tree = ast.parse(content)
        except SyntaxError:
            # If we can't parse as Python, return enhanced raw content
            return extract_raw_content_enhanced(lines, file_path)

        extracted_content = []

        # Extract module-level docstring (often contains the main documentation)
        module_doc = ast.get_docstring(tree)
        if module_doc and module_doc.strip():
            # For SageMath files, module docstrings often contain the main class documentation
            enhanced_module_doc = enhance_sage_docstring(module_doc, file_path.name, 1)
            extracted_content.append(enhanced_module_doc)

        # Extract class and function docstrings with enhanced processing
        classes_found = []
        functions_found = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                docstring = ast.get_docstring(node)
                if docstring and docstring.strip():
                    enhanced_doc = enhance_sage_docstring(docstring, f"Class {node.name}", node.lineno)
                    classes_found.append(enhanced_doc)

                    # Also extract method docstrings for important classes
                    if any(keyword in node.name for keyword in ["Lattice", "Matrix", "Group", "Ring"]):
                        for method_node in node.body:
                            if isinstance(method_node, ast.FunctionDef):
                                method_doc = ast.get_docstring(method_node)
                                if method_doc and method_doc.strip():
                                    method_enhanced = enhance_sage_docstring(
                                        method_doc,
                                        f"Method {node.name}.{method_node.name}",
                                        method_node.lineno,
                                    )
                                    functions_found.append(method_enhanced)

            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Only extract top-level functions (not methods, which are handled above)
                if isinstance(node.parent if hasattr(node, "parent") else None, ast.Module):
                    docstring = ast.get_docstring(node)
                    if docstring and docstring.strip():
                        enhanced_doc = enhance_sage_docstring(docstring, f"Function {node.name}", node.lineno)
                        functions_found.append(enhanced_doc)

        # Combine all extracted content
        extracted_content.extend(classes_found)
        extracted_content.extend(functions_found)

        if extracted_content:
            return "\n\n".join(extracted_content)
        else:
            # Fallback to enhanced raw content extraction
            return extract_raw_content_enhanced(lines, file_path)

    except Exception:
        # Fallback to enhanced raw content
        try:
            with open(file_path, encoding="utf-8") as f:
                lines = f.readlines()
            return extract_raw_content_enhanced(lines, file_path)
        except Exception:
            return ""


def enhance_sage_docstring(docstring: str, context: str, line_no: int) -> str:
    """Enhance SageMath docstrings by preserving examples and improving structure."""
    lines = docstring.split("\n")
    enhanced_lines = [f"{context} (line {line_no}):"]

    in_example = False
    example_buffer = []

    for line in lines:
        stripped = line.strip()

        # Detect SageMath examples
        if stripped.startswith("sage:") or stripped.startswith(">>>"):
            if not in_example:
                in_example = True
                enhanced_lines.append("\nEXAMPLES:")
            example_buffer.append(line)
        elif in_example and (stripped.startswith("...") or stripped == "" or line.startswith("    ")):
            example_buffer.append(line)
        else:
            # End of example block
            if in_example and example_buffer:
                enhanced_lines.extend(example_buffer)
                example_buffer = []
                in_example = False

            # Regular documentation line
            if stripped:
                enhanced_lines.append(line)

    # Add any remaining examples
    if example_buffer:
        enhanced_lines.extend(example_buffer)

    return "\n".join(enhanced_lines)


def extract_raw_content_enhanced(lines: list[str], file_path: Path) -> str:
    """Enhanced raw content extraction for files that can't be parsed as Python."""
    enhanced_lines = []

    # Add file context
    enhanced_lines.append(f"File: {file_path.name}")

    # Look for important patterns in SageMath files
    in_docstring = False
    docstring_quotes = None
    current_section = []

    for i, line in enumerate(lines[:200], 1):  # Process more lines for better coverage
        stripped = line.strip()

        # Detect docstring start/end
        if not in_docstring and (stripped.startswith('r"""') or stripped.startswith('"""')):
            in_docstring = True
            docstring_quotes = '"""'
            current_section = [f"Documentation (line {i}):"]
            current_section.append(line.replace('r"""', "").replace('"""', "").strip())
        elif in_docstring and docstring_quotes is not None and docstring_quotes in line:
            in_docstring = False
            enhanced_lines.extend(current_section)
            enhanced_lines.append("")  # Add spacing
            current_section = []
        elif in_docstring:
            current_section.append(line)

        # Detect class/function definitions
        elif stripped.startswith("class ") or stripped.startswith("def "):
            enhanced_lines.append(f"Line {i}: {stripped}")

        # Detect important SageMath patterns
        elif any(keyword in stripped.lower() for keyword in ["lattice", "invariant", "matrix", "example"]):
            enhanced_lines.append(f"Line {i}: {stripped}")

    # Add any remaining docstring content
    if current_section:
        enhanced_lines.extend(current_section)

    return "\n".join(enhanced_lines) if enhanced_lines else ""


def get_sage_path() -> Path:
    """Get the SageMath installation path from environment variables."""
    return Path(os.environ["SAGE_PATH"])


def get_sagemath_patterns() -> list[str]:
    """Get the file patterns for SageMath documentation."""
    return [
        "./src/doc/**/*.rst",  # Main documentation
        "./src/sage/**/*.py",  # Python source with docstrings
        "./src/sage/**/*.pyx",  # Cython source with docstrings
        "./src/doc/**/*.md",  # Markdown documentation
    ]


def find_sagemath_files(max_file_size_mb: int = 1) -> list[dict[str, Any]]:
    """Find and catalog SageMath documentation files."""
    sage_path = get_sage_path()
    patterns = get_sagemath_patterns()

    if not sage_path.exists():
        print(f"Warning: SageMath path not found at {sage_path}")
        return []

    files = []
    max_file_size = max_file_size_mb * 1024 * 1024

    for pattern in patterns:
        pattern_files = list(sage_path.glob(pattern))
        print(f"Found {len(pattern_files)} files matching pattern {pattern}")

        for p in pattern_files:
            # Skip very large files to avoid memory issues
            if p.stat().st_size > max_file_size:
                continue

            # Skip binary files and certain directories
            if any(skip in str(p) for skip in [".git", "__pycache__", ".pyc", "build", "dist"]):
                continue

            data = {
                "path": p,
                "meta": {
                    "url_source": f"file://{p}",
                    "suffix": p.suffix,
                    "source": "SageMath Local",
                    "relative_path": str(p.relative_to(sage_path)),
                },
            }
            files.append(data)

    return files


def convert_to_docs_url(relative_path: str) -> str | None:
    """
    Convert GitHub source URLs to rendered documentation URLs for .rst files.

    Converts:
    - src/doc/en/constructions/elliptic_curves.rst
    To:
    - https://doc.sagemath.org/html/en/constructions/elliptic_curves.html

    Args:
        relative_path: Original relative path from indexing

    Returns:
        Rendered documentation URL if it's a .rst file, None otherwise
    """
    # Only convert .rst documentation files
    if not relative_path.endswith(".rst"):
        return None

    # Remove any leading/trailing slashes
    path = relative_path.strip("/")

    # Convert src/doc/en/... to the documentation URL
    if path.startswith("src/doc/"):
        # Remove 'src/doc/' prefix
        doc_path = path[8:]  # Remove 'src/doc/'

        # Convert .rst to .html
        html_path = doc_path.replace(".rst", ".html")

        # Create the documentation URL
        docs_url = f"https://doc.sagemath.org/html/{html_path}"
        return docs_url

    # For other documentation paths, try to construct a reasonable URL
    elif "doc/" in path:
        # Find the part after 'doc/'
        doc_index = path.find("doc/") + 4
        doc_path = path[doc_index:]
        html_path = doc_path.replace(".rst", ".html")
        docs_url = f"https://doc.sagemath.org/html/{html_path}"
        return docs_url

    return None


def create_file_link(relative_path: str, line_number: int | None = None, link_type: str = "github") -> str:
    """
    Create a clickable link to open a file locally or on GitHub.
    For documentation files (.rst), prefer the rendered HTML documentation URL.

    Args:
        relative_path: Path relative to sage root (e.g., "src/sage/rings/integer.py")
        line_number: Optional line number to jump to
        link_type: "github" or "local"

    Returns:
        Markdown formatted link
    """
    if link_type == "github":
        # For documentation files, prefer the rendered documentation URL
        docs_url = convert_to_docs_url(relative_path)
        if docs_url:
            # For documentation, we don't include line numbers since they're rendered HTML
            return f"[{relative_path}]({docs_url})"

        # For source files, use GitHub blob URLs
        base_url = "https://github.com/sagemath/sage/blob/develop"
        github_path = fix_github_path(relative_path)

        if line_number:
            url = f"{base_url}/{github_path}#L{line_number}"
            return f"[{relative_path}:{line_number}]({url})"
        else:
            url = f"{base_url}/{github_path}"
            return f"[{relative_path}]({url})"
    else:  # local
        sage_path = get_sage_path()
        full_path = sage_path / relative_path
        if line_number:
            # For local files, we'll use file:// URL (works in some browsers/editors)
            url = f"file://{full_path}"
            return f"[{relative_path}:{line_number}]({url})"
        else:
            url = f"file://{full_path}"
            return f"[{relative_path}]({url})"


def fix_github_path(relative_path: str) -> str:
    """
    Fix the GitHub path to include proper directory structure.

    The SageMath GitHub repository has the structure:
    https://github.com/sagemath/sage/blob/develop/src/sage/...

    Args:
        relative_path: Original relative path from indexing

    Returns:
        Corrected path for GitHub links
    """
    # Remove any leading/trailing slashes
    path = relative_path.strip("/")

    # If the path already starts with 'src/', use it as-is
    if path.startswith("src/"):
        return path

    # If the path starts with 'sage/', prepend 'src/'
    if path.startswith("sage/"):
        return f"src/{path}"

    # For paths that don't include the sage prefix, try to construct the full path
    if "/" in path:
        # Check if it looks like a sage module path
        if any(
            sage_dir in path
            for sage_dir in [
                "modules",
                "rings",
                "groups",
                "geometry",
                "combinat",
                "algebras",
            ]
        ):
            return f"src/sage/{path}"

    # For single filenames or unclear paths, assume they're in the sage source
    if path.endswith(".py") or path.endswith(".pyx"):
        # Try to construct a reasonable path
        if "fgp_module.py" in path:
            return "src/sage/modules/fg_pid/fgp_module.py"
        elif "lattice" in path.lower():
            return f"src/sage/modules/{path}"
        else:
            return f"src/sage/{path}"

    # Default: assume it needs the src/sage prefix
    return f"src/sage/{path}"


def extract_line_numbers_from_content(content: str) -> list[int]:
    """Extract line numbers mentioned in content for linking purposes."""
    import re

    # Find patterns like "line 123", "Line 45", "(line 67)", etc.
    # Use raw strings to avoid SyntaxWarning about escape sequences
    line_patterns = re.findall(r"[Ll]ine (\d+)", content)
    parenthesis_patterns = re.findall(r"\(line (\d+)\)", content)

    all_lines = line_patterns + parenthesis_patterns
    return [int(line) for line in all_lines if line.isdigit()]


def create_sage_ctags_index(force_rebuild: bool = False) -> bool:
    """
    Create a comprehensive ctags index for the entire Sage repository.

    Args:
        force_rebuild: If True, rebuild even if index exists

    Returns:
        True if index was created/exists, False otherwise
    """
    import subprocess
    from pathlib import Path

    sage_path = get_sage_path()
    if not sage_path.exists():
        return False

    # Store the ctags file in the doc search directory
    ctags_file = Path(__file__).parent / "sage_ctags_index"

    # Check if we need to rebuild
    if ctags_file.exists() and not force_rebuild:
        # Check if the index is reasonably recent (less than 7 days old)
        import time

        age_days = (time.time() - ctags_file.stat().st_mtime) / (24 * 3600)
        if age_days < 7:
            return True

    print("🏗️  Building comprehensive ctags index for Sage repository...")
    print("   This may take a few minutes but will greatly speed up line number detection.")

    try:
        # Create ctags for the entire sage source tree
        result = subprocess.run(
            [
                "ctags",
                "-R",  # Recursive
                "-f",
                str(ctags_file),
                "--languages=Python",
                "--python-kinds=-i",  # Exclude imports
                "--fields=+n",  # Include line numbers
                "--sort=yes",  # Sort for faster lookups
                str(sage_path / "src" / "sage"),  # Only index the main sage source
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )  # 5 minute timeout

        if result.returncode == 0:
            print(f"✅ Successfully created ctags index: {ctags_file}")
            print(f"   Index size: {ctags_file.stat().st_size / 1024 / 1024:.1f} MB")
            return True
        else:
            print(f"❌ Failed to create ctags index: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("❌ Ctags indexing timed out - repository too large")
        return False
    except FileNotFoundError:
        print("❌ ctags not found - please install universal-ctags")
        return False
    except Exception as e:
        print(f"❌ Error creating ctags index: {e}")
        return False


def find_symbol_line_with_sage_index(symbol_name: str, file_hint: str | None = None) -> tuple[int | None, str | None]:
    """
    Use the comprehensive Sage ctags index to find symbol definitions.

    Args:
        symbol_name: Name of the symbol to find
        file_hint: Optional hint about which file the symbol might be in

    Returns:
        Tuple of (line_number, file_path) if found, (None, None) otherwise
    """
    ctags_file = Path(__file__).parent / "sage_ctags_index"

    if not ctags_file.exists():
        # Try to create the index
        if not create_sage_ctags_index():
            return None, None

    try:
        with open(ctags_file) as f:
            matches: list[tuple[int, str]] = []
            for line in f:
                if line.startswith("!_TAG_"):
                    continue

                parts = line.strip().split("\t")
                if len(parts) >= 4:
                    tag_name = parts[0]
                    file_path = parts[1]

                    if tag_name == symbol_name:
                        # Extract line number
                        line_number = None
                        for part in parts[3:]:
                            if part.startswith("line:"):
                                try:
                                    line_number = int(part.split(":")[1])
                                    break
                                except ValueError, IndexError:
                                    continue

                        if line_number:
                            matches.append((line_number, file_path))

            if matches:
                # If we have a file hint, prefer matches from that file
                if file_hint:
                    for line_no, file_path in matches:
                        if file_hint in file_path:
                            return line_no, file_path

                # Otherwise return the first match
                return matches[0]

    except Exception as e:
        print(f"Warning: Error reading ctags index: {e}")

    return None, None


def get_symbol_from_content(content: str) -> str | None:
    """Extract the main symbol (class or function name) from content."""
    lines = content.split("\n")

    # Look for class definitions first (higher priority)
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("class ") and ":" in stripped:
            # Extract class name
            class_part = stripped[6:].split(":")[0].split("(")[0].strip()
            return class_part

    # Look for function definitions
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("def ") and "(" in stripped:
            # Extract function name
            func_part = stripped[4:].split("(")[0].strip()
            if not func_part.startswith("_"):  # Prefer public functions
                return func_part

    return None


def get_primary_line_number(content: str, relative_path: str | None = None) -> int | None:
    """Get the most relevant line number from content, using ctags if available."""
    # First try explicit line number references
    line_numbers = extract_line_numbers_from_content(content)
    if line_numbers:
        return line_numbers[0]

    # If we have the file path and it's a source file, try ctags
    if relative_path and relative_path.endswith((".py", ".pyx")):
        # Try to find the main symbol in this content
        symbol = get_symbol_from_content(content)
        if symbol:
            line_no, found_file = find_symbol_line_with_sage_index(symbol, relative_path)
            if line_no:
                return line_no

    # Fallback to heuristic estimation for source code
    lines = content.split("\n")

    # Look for class definitions (usually near the beginning of important content)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("class ") and ":" in stripped:
            # Estimate that this class might be around line i*2 + 1 in the original file
            # This is a rough heuristic since we don't know where in the file this chunk came from
            return min(i * 2 + 1, 100)  # Cap at line 100 for reasonable estimates

    # Look for function definitions
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("def ") and "(" in stripped and ":" in stripped:
            return min(i * 2 + 1, 50)  # Cap at line 50 for function definitions

    # Look for docstring starts (often indicate beginning of classes/functions)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('r"""') or stripped.startswith('"""') or stripped.startswith("'''"):
            return min(i + 1, 20)  # Assume docstrings are near the beginning

    # If no specific indicators found, return None (no line number)
    return None
