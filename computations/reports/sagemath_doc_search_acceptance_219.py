"""Acceptance survey for research#219, including the independent audit finding."""
import sys, types, tempfile

sys.path.insert(0, 'computations/scripts')
sys.path.insert(0, 'computations/scripts/sagemath_doc_search')

hay = types.ModuleType('haystack'); haydc = types.ModuleType('haystack.dataclasses')
class Document:
    def __init__(self, content=None, meta=None):
        self.content, self.meta = content, meta or {}
haydc.Document = Document; hay.dataclasses = haydc
sys.modules['haystack'] = hay; sys.modules['haystack.dataclasses'] = haydc
sd = types.ModuleType('sagemath_doc_search')
sd.__path__ = ['computations/scripts/sagemath_doc_search']
sys.modules.setdefault('sagemath_doc_search', sd)

import inline_citation_enhancer as ice
import sagemath_utils as su
import citation_utils as cu
sys.modules['sagemath_doc_search.citation_utils'] = cu

fails = []

# 1. read/parse boundary
try:
    su.extract_python_docstrings(tempfile.mktemp(suffix='.py'))
    fails.append('read/parse returned silently')
except su.DocumentationReadError:
    pass
class Ghost:
    name = 'ghost.py'
try:
    su.extract_python_docstrings(Ghost())
    fails.append('unreadable object returned silently')
except su.DocumentationReadError:
    pass

# 2. metadata-enhancement boundary
class BadMeta(dict):
    def copy(self):
        raise RuntimeError('boom')
try:
    ice.InlineCitationEnhancer().enhance_document_metadata(
        [types.SimpleNamespace(content='x', meta=BadMeta())])
    fails.append('enhancement returned the original silently')
except ice.DocumentationEnhancementError as exc:
    assert 'boom' in str(exc)

# 3. AUDITED FINDING: _add_source_list must not substitute a bare-path
#    "successful-looking" line for the requested link.
orig = cu.create_file_link
cu.create_file_link = lambda *a, **k: (_ for _ in ()).throw(KeyError('badlink'))
try:
    ice.InlineCitationEnhancer().post_process_response_citations(
        "answer (src1).",
        [ice.Document(content='c', meta={'citation_id': 'src1',
                                         'relative_path': 'src/x.py',
                                         'citation_display': 'X'})])
    fails.append('_add_source_list substituted a bare path silently')
except ice.CitationLinkError as exc:
    assert 'src/x.py' in str(exc) and 'badlink' in str(exc)
finally:
    cu.create_file_link = orig

# 4. functionality preserved on the happy path
resp = ice.InlineCitationEnhancer().post_process_response_citations(
    "answer.",
    [ice.Document(content='c', meta={'citation_id': 'src1',
                                     'relative_path': 'src/x.py',
                                     'citation_display': 'X'})])
if 'src/x.py' not in resp:
    fails.append('happy path lost the source list')

print('ACCEPTANCE #219:', 'PASS' if not fails else 'FAIL: %s' % fails)
sys.exit(1 if fails else 0)
