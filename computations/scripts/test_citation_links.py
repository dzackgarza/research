#!/usr/bin/env python3
"""
Test script to verify that citation links now go directly to source files.
"""

from inline_citation_enhancer import InlineCitationEnhancer
from haystack.dataclasses import Document

def test_direct_citation_links():
    """Test that citations link directly to source files."""
    
    # Create test documents
    test_docs = [
        Document(
            content="class IntegralLattice:\n    def discriminant(self):\n        '''Compute discriminant'''\n        pass",
            meta={"relative_path": "src/sage/modules/lattice.py"}
        ),
        Document(
            content="Tutorial on Lattices\n====================\n\nLattices are discrete subgroups of Euclidean space.",
            meta={"relative_path": "src/doc/en/tutorial/lattices.rst"}
        )
    ]
    
    enhancer = InlineCitationEnhancer()
    enhanced_docs = enhancer.enhance_document_metadata(test_docs)
    
    # Test response with inline citations
    test_response = "You can compute the discriminant using the discriminant method (src1). This is documented in the lattice tutorial (src2)."
    
    # Process the response
    enhanced_response = enhancer.post_process_response_citations(test_response, enhanced_docs)
    
    print("🔗 Testing Citation Link Generation")
    print("=" * 50)
    print(f"Original response: {test_response}")
    print()
    print("Enhanced response:")
    print(enhanced_response)
    print()
    
    # Check if the links are direct (not internal anchors)
    import re
    
    # Find all href attributes in the enhanced response
    href_pattern = r'href="([^"]+)"'
    links = re.findall(href_pattern, enhanced_response)
    
    print("Found links:")
    for i, link in enumerate(links, 1):
        if link.startswith('#'):
            print(f"  ❌ Link {i}: {link} (internal anchor - should be direct file link)")
        elif link.startswith('http') or link.startswith('file://'):
            print(f"  ✅ Link {i}: {link} (direct link)")
        else:
            print(f"  ⚠️  Link {i}: {link} (unknown type)")
    
    # Verify the inline citations were converted properly
    if '(src1)' in enhanced_response or '(src2)' in enhanced_response:
        print("❌ Original (src1) format still present - conversion failed")
    else:
        print("✅ Original (src1) format converted to links")
    
    print()
    print("Test complete!")

if __name__ == "__main__":
    test_direct_citation_links() 