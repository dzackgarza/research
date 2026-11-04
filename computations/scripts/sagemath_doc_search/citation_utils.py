#!/usr/bin/env python3
"""
Citation utilities for the enhanced inline citation system.
Provides necessary functions for creating links and processing citations.
"""

import re
from pathlib import Path


class CitationSourceError(ValueError):
    """A source cannot be rendered as a citation because it carries no file path.

    Raised instead of emitting a placeholder such as a bare ``unknown`` where a path
    belongs, which reads like a rendered source when it is not one (#219).
    """

    def __init__(self, citation_id, meta):
        self.citation_id = citation_id
        self.meta = meta
        super().__init__(
            "cannot render source %s: the document carries no relative_path in %r"
            % (citation_id, meta)
        )


def require_file_path(meta, citation_id) -> str:
    """Return the cited document's usable file path, else reject it precisely.

    Absent, None, blank or the ``"unknown"`` sentinel are all pathless; renderers must
    not turn any of them into a working-directory link presented as a real source.
    """
    rel_path = meta.get("relative_path")
    if rel_path is None or str(rel_path).strip() in ("", "unknown"):
        raise CitationSourceError(citation_id, meta)
    return str(rel_path)


def get_primary_line_number(content: str, file_path: str) -> int | None:
    """
    Extract a primary line number from content for citation purposes.

    Args:
        content: Document content
        file_path: Path to the file

    Returns:
        Line number (1-based), or None when no line is determinable.  None is a real
        answer -- an unknown line -- and is never flattened into line 1, which would
        point a reader at the top of a file the content says nothing about.
    """
    if not content:
        return None

    lines = content.split("\n")

    # For Python files, look for class or function definitions
    if file_path.endswith((".py", ".pyx")):
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith(("class ", "def ")) and not stripped.startswith(
                "def _"
            ):
                return i

    # For RST files, look for section headers
    elif file_path.endswith(".rst"):
        for i, line in enumerate(lines, 1):
            if i < len(lines) and lines[i].strip() and len(set(lines[i].strip())) == 1:
                # This line is likely underlined (RST section header)
                if lines[i].strip()[0] in "=-~^\"'":
                    return i

    return None


def create_file_link(
    file_path: str, line_number: int | None = None, link_type: str = "local"
) -> str:
    """
    Create a clickable link for a file path.

    Args:
        file_path: Relative file path
        line_number: Line to jump to, or None when the line is unknown; no anchor is
            emitted for None rather than a guessed one
        link_type: Type of link ("local", "github")

    Returns:
        HTML link string

    Raises:
        ValueError: ``file_path`` is blank.  A blank path would resolve to the current
            working directory, which is a successful-looking bogus link.
    """
    if not file_path or not file_path.strip():
        raise ValueError("a file link needs a real path, got %r" % (file_path,))

    suffix = f":{line_number}" if line_number else ""

    if link_type == "github":
        # Create GitHub link
        clean_path = fix_github_path(file_path)

        # For documentation files, try to create docs URL
        if file_path.endswith(".rst"):
            docs_url = convert_to_docs_url(file_path)
            if docs_url:
                return (
                    f'<a href="{docs_url}" target="_blank">{Path(file_path).name}</a>'
                )

        # Default to GitHub source view
        anchor = f"#L{line_number}" if line_number else ""
        github_url = (
            f"https://github.com/sagemath/sage/blob/develop/{clean_path}{anchor}"
        )
        return f'<a href="{github_url}" target="_blank">{file_path}{suffix}</a>'

    else:  # local
        # Create local file link
        return f'<a href="file://{Path(file_path).absolute()}" target="_blank">{file_path}{suffix}</a>'


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
        # Find the index after 'en'. The membership test above guarantees index() cannot
        # raise, so the old catch-and-pass is gone rather than kept unreachable.
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


def create_citation_link(
    citation_id: str, display_text: str, file_path: str, line_number: int = 1
) -> str:
    """
    Create a properly formatted citation link.

    Args:
        citation_id: Citation ID (e.g., "src1")
        display_text: Text to display for the link
        file_path: File path to link to
        line_number: Line number

    Returns:
        HTML link with citation formatting
    """
    file_link = create_file_link(file_path, line_number, "local")
    return f'<sup><a href="#citation-{citation_id}" class="citation-ref">[{citation_id}]</a></sup>'


def process_inline_citations(
    text: str, citation_map: dict[str, dict[str, object]]
) -> str:
    """
    Process inline citations in text and convert them to proper links.

    Args:
        text: Text containing (src1), (src2) style citations
        citation_map: Map from citation_id to document info

    Returns:
        Text with processed citations
    """

    def replace_citation(match: re.Match[str]) -> str:
        citation_id = match.group(1)
        if citation_id in citation_map:
            doc_info = citation_map[citation_id]
            file_path = doc_info.get("file_path", "unknown")
            line_no = doc_info.get("line_number", 1)

            # Create a simple superscript link
            return f'<sup><a href="#ref-{citation_id}" class="citation-link">[{citation_id}]</a></sup>'
        else:
            return match.group(0)  # Return original if not found

    # Replace (src1), (src2), etc. with superscript links
    pattern = r"\((src\d+)\)"
    return re.sub(pattern, replace_citation, text)


def create_sources_section(documents: list, enhanced_docs: list) -> str:
    """
    Create a properly formatted sources section with clickable links.

    Args:
        documents: Original documents
        enhanced_docs: Enhanced documents with citation metadata

    Returns:
        HTML formatted sources section
    """
    if not enhanced_docs:
        return ""

    source_lines = []
    source_lines.append("\n\n---\n\n**Sources:**\n")

    for doc in enhanced_docs:
        citation_id = doc.meta.get("citation_id", "src?")
        citation_display = doc.meta.get("citation_display", "unknown")

        # Absent, None, blank or sentinel paths all fail closed identically, so a
        # working-directory or placeholder link can never stand as a rendered source.
        rel_path = require_file_path(doc.meta, citation_id)

        # Get line number from content
        line_no = get_primary_line_number(doc.content, rel_path)

        # Create appropriate link based on file type
        if rel_path.endswith(".rst"):
            docs_url = convert_to_docs_url(rel_path)
            if docs_url:
                file_link = f'<a href="{docs_url}" target="_blank">{Path(rel_path).name}</a>'
            else:
                file_link = create_file_link(rel_path, line_no, "github")
        else:
            file_link = create_file_link(rel_path, line_no, "local")

        source_lines.append(
            f'<p id="ref-{citation_id}"><strong>[{citation_id}]</strong> {file_link} - {citation_display}</p>'
        )

    return "\n".join(source_lines)
