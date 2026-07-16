#!/usr/bin/env python3
"""
Inline Citation Enhancer for SageMath Documentation Search.

This module provides LlamaIndex-style inline citations by:
1. Enhancing document metadata with section/page information
2. Improving prompts to request inline citations
3. Post-processing responses to ensure citations are included
4. Supporting both page-style citations (for docs) and line-based citations (for source)
"""

import logging
import re
from pathlib import Path
from typing import Any, TypedDict

logger = logging.getLogger(__name__)

from haystack.dataclasses import Document


class _CitationTarget(TypedDict):
    file_path: str
    line_number: int | None


class InlineCitationEnhancer:
    """Enhances the citation system to provide consistent inline citations."""

    def __init__(self) -> None:
        self.citation_formats = {
            "inline_doc": "({filename}, section {section})",
            "inline_source": "({filename}:{line})",
            "inline_short": "({source_id})",
            "footnote": "[^{id}]",
        }

    def enhance_document_metadata(self, documents: list[Document]) -> list[Document]:
        """
        Enhance document metadata with better citation information.

        Args:
            documents: List of Haystack documents

        Returns:
            Enhanced documents with improved metadata for citations
        """
        enhanced_docs = []

        for i, doc in enumerate(documents):
            try:
                # Create enhanced metadata
                enhanced_meta = doc.meta.copy()

                # Add citation ID
                enhanced_meta["citation_id"] = f"src{i + 1}"

                # Extract section information for documentation files
                if doc.meta.get("relative_path", "").endswith(".rst"):
                    section_info = self._extract_rst_section_info(doc.content or "")
                    enhanced_meta.update(section_info)

                # Extract class/function information for Python files
                elif doc.meta.get("relative_path", "").endswith((".py", ".pyx")):
                    code_info = self._extract_python_code_info(doc.content or "")
                    enhanced_meta.update(code_info)

                # Add citation display name
                enhanced_meta["citation_display"] = self._create_citation_display(
                    enhanced_meta
                )

                # Create enhanced document
                enhanced_doc = Document(content=doc.content, meta=enhanced_meta)
                enhanced_docs.append(enhanced_doc)

            except Exception as e:
                logger.warning(f"Failed to enhance document metadata: {e}")
                enhanced_docs.append(doc)  # Keep original on error

        return enhanced_docs

    def _extract_rst_section_info(self, content: str) -> dict[str, Any]:
        """Extract section information from RST content."""
        info = {}

        # Look for RST section headers
        lines = content.split("\n")
        current_section = None

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Check for RST title patterns
            if i < len(lines) - 1:
                next_line = lines[i + 1].strip()
                if next_line and len(set(next_line)) == 1 and next_line[0] in "=-~^\"'":
                    # This is likely a section header
                    if (
                        len(next_line) >= len(stripped) * 0.8
                    ):  # Underline is roughly the same length
                        current_section = stripped
                        break

            # Also look for explicit .. _section references
            if stripped.startswith(".. _"):
                section_ref = stripped[4:].rstrip(":")
                if section_ref:
                    current_section = section_ref.replace("-", " ").replace("_", " ")

        if current_section:
            info["section"] = current_section
            info["content_type"] = "documentation"
        else:
            info["section"] = "Introduction"  # Default section
            info["content_type"] = "documentation"

        return info

    def _extract_python_code_info(self, content: str) -> dict[str, Any]:
        """Extract class/function information from Python content."""
        info = {}

        lines = content.split("\n")
        primary_symbol = None
        symbol_type = None

        for line in lines:
            stripped = line.strip()

            # Look for class definitions
            if stripped.startswith("class ") and ":" in stripped:
                class_name = stripped.split()[1].split("(")[0].split(":")[0]
                primary_symbol = class_name
                symbol_type = "class"
                break

            # Look for function definitions
            elif stripped.startswith("def ") and "(" in stripped:
                func_name = stripped.split()[1].split("(")[0]
                if not func_name.startswith("_"):  # Prefer public functions
                    primary_symbol = func_name
                    symbol_type = "function"
                    # Continue looking for classes (preferred)

        if primary_symbol:
            info["primary_symbol"] = primary_symbol
            if symbol_type is not None:
                info["symbol_type"] = symbol_type
            info["content_type"] = "source_code"
        else:
            info["content_type"] = "source_code"

        return info

    def _create_citation_display(self, meta: dict[str, Any]) -> str:
        """Create a display name for citations."""
        rel_path = str(meta.get("relative_path", "unknown"))

        if meta.get("content_type") == "documentation":
            filename = Path(rel_path).stem
            section = meta.get("section", "unknown")
            return f"{filename}, {section}"

        elif meta.get("content_type") == "source_code":
            filename = Path(rel_path).name
            symbol = meta.get("primary_symbol")
            if symbol:
                return f"{filename} ({symbol})"
            else:
                return filename

        else:
            return Path(rel_path).name if rel_path != "unknown" else "unknown"

    def create_enhanced_prompt_with_citations(
        self, question: str, documents: list[Document], link_type: str = "github"
    ) -> str:
        """
        Create a structured, pedagogical prompt with a full example template for consistent formatting.
        """

        # Include the exact example from ModelOutput.md as a template
        example_template = """### 🔹 Computing Invariants of an Integral Lattice in SageMath

Solution: use the `IntegralLattice` method to construct at `FreeQuadraticModule_integer_symmetric` object.

Key methods:

- `L.signature_pair()`
- `L.index()`
- `L.discriminant()`
- `L.discriminant_group()`
- `L.is_even()`
- `L.is_unimodular()`
- `L.dual_lattice()`
- `L.orthogonal_group()`

---

### 🧪 SageMath Code

```python
from sage.all import *

# Define a lattice via a symmetric Gram matrix
M = Matrix([[2, 1], [1, 3]])
L = IntegralLattice(M)

print("Rank:", L.rank())
print("Gram matrix:\n", L.gram_matrix())
print("Discriminant:", L.discriminant())
print("Signature:", L.signature())
print("Dual basis:\n", L.dual().basis_matrix())
print("Discriminant group:", L.discriminant_group())
```

---

### 🔗 References

* [`IntegralLattice`](https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module_integer.html#sage.modules.free_module_integer.IntegralLattice)
* See also:
    - [`QuadraticForm`](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/quadratic_form__integer.html)

---

*IMPORTANT: Do not reference any external books or articles not present in the indexed documentation or codebase. Do not include a 'Mathematical Context' or 'Explanation of Outputs' section. Always cite the specific code or documentation source for every method or property listed.*"""

        prompt = (
            "You are an expert mathematical assistant answering questions about advanced mathematics and SageMath.\n\n"
            "CRITICAL: You must follow the EXACT Markdown structure shown in the example below.\n"
            "- Use ### for section headers with emojis\n"
            "- Use --- for section separators\n"
            "- Use bullet points (*) for lists\n"
            "- Use LaTeX math notation ($...$) for mathematical expressions\n"
            "- Use proper code blocks with ```python\n"
            "- Include clickable links in References section\n"
            "- End with a concrete 'Next steps' suggestion\n"
            "- Be confident and precise - never apologize or hedge\n\n"
            "CRITICAL CODE REQUIREMENTS:\n"
            "- For all code examples, use `from sage.all import *` as the import statement.\n"
            "- ONLY use method calls, classes, and parameters that appear in the provided sources or the validated sidebar list.\n"
            "- NEVER invent method names, parameters, or constructors.\n"
            "- Do NOT generate or list all methods. Do NOT include a 'Complete List of Methods' section. Refer to the sidebar for validated methods.\n"
            "- Base ALL code examples directly on patterns shown in the documentation.\n"
            "- If the sources show 'sage:' examples, adapt those exactly.\n"
            "- If you're unsure about a method signature, don't guess - use what's documented.\n"
            "- Test your mental model: would this code actually run based on the sources?\n"
            "- Look for concrete 'sage:' examples in the sources and adapt them.\n"
            "- If no working examples exist in sources, explain the concept without providing broken code.\n\n"
            "## TEMPLATE TO FOLLOW EXACTLY:\n"
            f"{example_template}\n\n"
            "## Provided Sources:\n"
        )

        # Add source information
        for doc in documents:
            citation_id = doc.meta.get("citation_id", "src?")
            citation_display = doc.meta.get("citation_display", "unknown")
            content = doc.content or ""
            content_preview = content[:600] + "..." if len(content) > 600 else content
            prompt += f"**{citation_id}**: {citation_display}\n```\n{content_preview}\n```\n\n"

        prompt += (
            f"## USER QUESTION: {question}\n\n"
            "## YOUR RESPONSE:\n"
            "Follow the template structure exactly. Use the same emojis, section headers, formatting, and style.\n"
            "Adapt the content to answer the specific question, but maintain the exact Markdown structure.\n"
            "IMPORTANT: Your code examples must use ONLY the classes, methods, and parameters shown in the provided sources above.\n"
            "Do not invent or guess method names - if it's not in the sources, don't use it.\n\n"
        )

        return prompt

    def post_process_response_citations(
        self, response: str, documents: list[Document]
    ) -> str:
        """
        Post-process the response minimally to preserve clean Markdown formatting.

        Args:
            response: LLM response text
            documents: Source documents used

        Returns:
            Response with minimal citation processing to preserve formatting
        """
        try:
            # Check if response already has some citations - if so, leave it mostly alone
            citation_pattern = r"\(src\d+\)"
            existing_citations = re.findall(citation_pattern, response)

            # Only process if there are absolutely no citations and the response seems incomplete
            if len(existing_citations) == 0 and len(response.strip()) < 100:
                logger.warning(
                    "Very short response with no citations, adding minimal citation..."
                )
                response = self._add_single_citation(response, documents)

            # Add source list at the end (but only if it doesn't already have a References section)
            if "### 🔗 References" not in response and "References:" not in response:
                response = self._add_source_list(response, documents)

            return response

        except Exception as e:
            logger.error(f"Error post-processing citations: {e}")
            return response  # Return original on error

    def _add_single_citation(self, response: str, documents: list[Document]) -> str:
        """Add a single citation to very short responses that have none."""
        if not documents:
            return response

        # Just add one citation to the end if the response is very short
        best_doc = documents[0]  # Use first document
        citation_id = best_doc.meta.get("citation_id", "src1")

        if response.strip().endswith("."):
            return response.rstrip(".") + f" ({citation_id})."
        else:
            return response + f" ({citation_id})"

    def _add_source_list(self, response: str, documents: list[Document]) -> str:
        """Add a formatted source list at the end of the response."""

        if not documents:
            return response

        # First, process inline citations to convert (src1) to proper links
        citation_map: dict[str, _CitationTarget] = {}
        for doc in documents:
            citation_id = str(doc.meta.get("citation_id", "src?"))
            rel_path = str(doc.meta.get("relative_path", "unknown"))
            citation_map[citation_id] = {
                "file_path": rel_path,
                "line_number": self._get_line_number(doc.content or "", rel_path),
            }

        # Convert inline citations to superscript links
        processed_response = self._process_inline_citations(response, citation_map)

        # Create sources section
        source_lines = ["\n\n---\n\n**Sources:**\n"]

        for doc in documents:
            citation_id = doc.meta.get("citation_id", "src?")
            citation_display = doc.meta.get("citation_display", "unknown")
            rel_path = str(doc.meta.get("relative_path", "unknown"))

            # Create appropriate link
            try:
                from dzack_research.sagemath_doc_search.citation_utils import (
                    create_file_link,
                    get_primary_line_number,
                )

                line_no = get_primary_line_number(doc.content or "", rel_path)
                if rel_path.endswith(".rst"):
                    file_link = create_file_link(rel_path, line_no, "github")
                else:
                    file_link = create_file_link(rel_path, line_no, "local")

                source_lines.append(
                    f'<p id="ref-{citation_id}"><strong>[{citation_id}]</strong> {file_link} - {citation_display}</p>'
                )

            except Exception as e:
                logger.warning(f"Failed to create link for {rel_path}: {e}")
                # Fallback if link creation fails
                source_lines.append(
                    f'<p id="ref-{citation_id}"><strong>[{citation_id}]</strong> {rel_path} - {citation_display}</p>'
                )

        return processed_response + "\n".join(source_lines)

    def _process_inline_citations(
        self, text: str, citation_map: dict[str, _CitationTarget]
    ) -> str:
        """Process inline citations and convert them to direct source file links."""

        def replace_citation(match: re.Match[str]) -> str:
            citation_id = match.group(1)
            if citation_id in citation_map:
                file_path = citation_map[citation_id]["file_path"]
                line_number = citation_map[citation_id]["line_number"]

                # Create direct link to source file instead of internal anchor
                try:
                    from dzack_research.sagemath_doc_search.citation_utils import (
                        create_file_link,
                    )

                    if file_path.endswith(".rst"):
                        # For documentation files, prefer GitHub/docs URLs
                        file_link = create_file_link(
                            file_path, line_number or 1, "github"
                        )
                    else:
                        # For source files, use local links
                        file_link = create_file_link(
                            file_path, line_number or 1, "local"
                        )

                    # Extract just the href attribute for the inline citation
                    import re

                    href_match = re.search(r'href="([^"]+)"', file_link)
                    if href_match:
                        href_url = href_match.group(1)
                        return f'<sup><a href="{href_url}" target="_blank" class="citation-link">[{citation_id}]</a></sup>'
                    else:
                        # Fallback to internal reference if link creation fails
                        return f'<sup><a href="#ref-{citation_id}" class="citation-link">[{citation_id}]</a></sup>'

                except Exception as e:
                    logger.warning(
                        f"Failed to create direct citation link for {file_path}: {e}"
                    )
                    # Fallback to internal reference
                    return f'<sup><a href="#ref-{citation_id}" class="citation-link">[{citation_id}]</a></sup>'
            else:
                return match.group(0)  # Return original if not found

        # Replace (src1), (src2), etc. with direct source file links
        pattern = r"\((src\d+)\)"
        return re.sub(pattern, replace_citation, text)

    def _get_line_number(self, content: str, file_path: str) -> int | None:
        """Get line number for citation purposes."""
        try:
            from dzack_research.sagemath_doc_search.citation_utils import (
                get_primary_line_number,
            )

            return get_primary_line_number(content, file_path)
        except ImportError:
            return 1  # Fallback


def create_citation_enhanced_prompt(
    question: str, documents: list[Document], link_type: str = "github"
) -> str:
    """
    Convenience function to create an enhanced prompt with citation requirements.

    Args:
        question: User's question
        documents: List of source documents
        link_type: Type of links to generate

    Returns:
        Enhanced prompt with inline citation requirements
    """
    enhancer = InlineCitationEnhancer()

    # Enhance document metadata first
    enhanced_docs = enhancer.enhance_document_metadata(documents)

    # Create enhanced prompt
    return enhancer.create_enhanced_prompt_with_citations(
        question, enhanced_docs, link_type
    )


def enhance_response_with_citations(response: str, documents: list[Document]) -> str:
    """
    Convenience function to enhance a response with better citations.

    Args:
        response: LLM response text
        documents: Source documents used

    Returns:
        Enhanced response with improved citations
    """
    enhancer = InlineCitationEnhancer()

    # Enhance document metadata first
    enhanced_docs = enhancer.enhance_document_metadata(documents)

    # Post-process the response
    return enhancer.post_process_response_citations(response, enhanced_docs)


# Example usage and testing
if __name__ == "__main__":
    print("🔗 Testing Inline Citation Enhancer")

    # Create test documents
    test_docs = [
        Document(
            content="class IntegralLattice:\n    def discriminant(self):\n        '''Compute discriminant'''\n        pass",
            meta={"relative_path": "src/sage/modules/lattice.py"},
        ),
        Document(
            content="Tutorial on Lattices\n====================\n\nLattices are discrete subgroups of Euclidean space.",
            meta={"relative_path": "src/doc/en/tutorial/lattices.rst"},
        ),
    ]

    enhancer = InlineCitationEnhancer()
    enhanced_docs = enhancer.enhance_document_metadata(test_docs)

    print("Enhanced document metadata:")
    for doc in enhanced_docs:
        print(f"- {doc.meta['citation_id']}: {doc.meta['citation_display']}")

    # Test prompt creation
    prompt = enhancer.create_enhanced_prompt_with_citations(
        "How do I compute the discriminant of a lattice?", enhanced_docs
    )

    print("\nExample enhanced prompt length:", len(prompt))

    # Test response enhancement
    test_response = "You can compute the discriminant using the discriminant method. This is available in the IntegralLattice class."
    enhanced_response = enhancer.post_process_response_citations(
        test_response, enhanced_docs
    )

    print("\nEnhanced response:")
    print(enhanced_response)
