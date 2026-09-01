#!/usr/bin/env python3
"""
Simple webpage to markdown converter using multiple methods.
Tries html-to-markdown first, falls back to html2text if needed.
"""

import sys
import requests
from pathlib import Path

def fetch_and_convert(url, output_file=None):
    """Fetch a webpage and convert it to markdown."""
    
    # Fetch the webpage
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
    
    # Try html-to-markdown first (if available)
    try:
        from html_to_markdown import convert_to_markdown
        markdown = convert_to_markdown(
            html_content,
            # Options for better mathematical content handling
            heading_style='atx',
            keep_data_uri_images=False,
            keep_inline_style_comments=False,
            add_meta_data_header=True,
            full_input_file_path=url
        )
        print("Converted using html-to-markdown")
    except ImportError:
        # Fall back to html2text
        try:
            import html2text
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.body_width = 0  # Don't wrap lines
            h.unicode_snob = True
            markdown = h.handle(html_content)
            print("Converted using html2text")
        except ImportError:
            # Last resort: basic pandoc
            import subprocess
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(html_content)
                temp_html = f.name
            
            result = subprocess.run(
                ['pandoc', '-f', 'html', '-t', 'markdown', temp_html],
                capture_output=True,
                text=True
            )
            markdown = result.stdout
            Path(temp_html).unlink()
            print("Converted using pandoc")
    
    # Save to file if specified
    if output_file:
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Saved to {output_file}")
    
    return markdown


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python webpage_to_markdown.py <url> [output_file]")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    markdown = fetch_and_convert(url, output_file)
    if markdown and not output_file:
        print("\n" + "="*80 + "\n")
        print(markdown)