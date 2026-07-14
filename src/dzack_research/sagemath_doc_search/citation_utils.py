#!/usr/bin/env python3
"""
Citation utilities for the enhanced inline citation system.
Provides necessary functions for creating links and processing citations.
"""

from pathlib import Path


def get_primary_line_number(content: str, file_path: str) -> int:
    """
    Extract a primary line number from content for citation purposes.

    Args:
        content: Document content
        file_path: Path to the file

    Returns:
        Line number (1-based) or 1 if not determinable
    """
    if not content:
        return 1

    lines = content.split("\n")

    # For Python files, look for class or function definitions
    if file_path.endswith((".py", ".pyx")):
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith(("class ", "def ")) and not stripped.startswith("def _"):
                return i

    # For RST files, look for section headers
    elif file_path.endswith(".rst"):
        for i, line in enumerate(lines, 1):
            if i < len(lines) and lines[i].strip() and len(set(lines[i].strip())) == 1:
                # This line is likely underlined (RST section header)
                if lines[i].strip()[0] in "=-~^\"'":
                    return i

    return 1


def create_file_link(file_path: str, line_number: int = 1, link_type: str = "local") -> str:
    """
    Create a clickable link for a file path.

    Args:
        file_path: Relative file path
        line_number: Line number to link to
        link_type: Type of link ("local", "github")

    Returns:
        HTML link string
    """
    if link_type == "github":
        # Create GitHub link
        clean_path = fix_github_path(file_path)

        # For documentation files, try to create docs URL
        if file_path.endswith(".rst"):
            docs_url = convert_to_docs_url(file_path)
            if docs_url:
                return f'<a href="{docs_url}" target="_blank">{Path(file_path).name}</a>'

        # Default to GitHub source view
        github_url = f"https://github.com/sagemath/sage/blob/develop/{clean_path}#L{line_number}"
        return f'<a href="{github_url}" target="_blank">{file_path}:{line_number}</a>'

    else:  # local
        # Create local file link
        return f'<a href="file://{Path(file_path).absolute()}" target="_blank">{file_path}:{line_number}</a>'


def fix_github_path(file_path: str) -> str:
    """
    Fix file path for GitHub URLs.

    Args:
        file_path: Original file path

    Returns:
        GitHub-compatible path
    """
    # Remove common prefixes
    for prefix in ["src/", "sage/", "./"]:
        if file_path.startswith(prefix):
            file_path = file_path[len(prefix) :]

    # Ensure it starts with 'src/' for SageMath
    if not file_path.startswith("src/"):
        file_path = "src/" + file_path

    return file_path


def convert_to_docs_url(file_path: str) -> str | None:
    """
    Convert a file path to SageMath documentation URL if possible.

    Args:
        file_path: File path to convert

    Returns:
        Documentation URL or None if not convertible
    """
    if not file_path.endswith(".rst"):
        return None

    # Extract the relevant part of the path
    path_parts = Path(file_path).parts

    # Look for documentation structure patterns
    if "doc" in path_parts and "en" in path_parts:
        # Find the index after 'en'
        en_index = path_parts.index("en")
        if en_index + 1 < len(path_parts):
            # Get the part after 'en'
            doc_path = "/".join(path_parts[en_index + 1 :])
            # Remove .rst extension
            doc_path = doc_path.replace(".rst", ".html")

            # Create docs URL
            base_url = "https://doc.sagemath.org/html/en"
            return f"{base_url}/{doc_path}"

    return None
