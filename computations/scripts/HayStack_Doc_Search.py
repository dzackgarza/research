import subprocess
from pathlib import Path
from typing import List, Tuple
import os
import re
import ast
import pickle
import hashlib
import time
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from haystack.components.builders import AnswerBuilder, PromptBuilder
from haystack.components.converters import TextFileToDocument
from haystack.components.generators.openai import OpenAIGenerator
from haystack.components.preprocessors import (
    DocumentCleaner,
    DocumentSplitter,
)
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.writers import DocumentWriter
from haystack.core.pipeline import Pipeline
from haystack.dataclasses import GeneratedAnswer, Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.document_stores.types import DuplicatePolicy

# Import our SageMath utilities
from sagemath_utils import extract_python_docstrings, get_sage_path, get_sagemath_patterns

# Load the environment variables, we're going to need it for OpenAI
load_dotenv()

# Configuration for local vs remote OpenAI
LOCAL_OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:1337/v1")
USE_LOCAL_OPENAI = os.getenv("USE_LOCAL_OPENAI", "true").lower() == "true"
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Documentation search configuration
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "1"))
INCLUDE_SAGEMATH_DEFAULT = os.getenv("INCLUDE_SAGEMATH_DEFAULT", "true").lower() == "true"
INCLUDE_REMOTE_DEFAULT = os.getenv("INCLUDE_REMOTE_DEFAULT", "true").lower() == "true"

# This is the list of documentation that we're going to fetch
DOCUMENTATIONS = [
    (
        "Pandas",
        "https://github.com/pandas-dev/pandas",
        "./doc/source/**/*.rst",
    ),
    (
        "NumPy",
        "https://github.com/numpy/numpy",
        "./doc/**/*.rst",
    ),
]

DOCS_PATH = Path(__file__).parent / "downloaded_docs"
CACHE_PATH = Path(__file__).parent / "doc_cache"
# Get SageMath configuration from utility module
SAGE_PATH = get_sage_path()
SAGEMATH_PATTERNS = get_sagemath_patterns()

# Ensure cache directory exists
CACHE_PATH.mkdir(parents=True, exist_ok=True)


def get_cache_key(sources_config: dict) -> str:
    """Generate a cache key based on configuration and file timestamps."""
    key_data = {
        'sources': sources_config,
        'sage_path': str(SAGE_PATH),
        'max_file_size': MAX_FILE_SIZE_MB,
    }
    
    # Add SageMath directory modification time if it exists
    if SAGE_PATH.exists():
        try:
            # Get a representative timestamp from SageMath source
            sage_src = SAGE_PATH / "src" / "sage"
            if sage_src.exists():
                key_data['sage_mtime'] = sage_src.stat().st_mtime
        except:
            pass
    
    # Add timestamp for downloaded docs
    if DOCS_PATH.exists():
        try:
            key_data['docs_mtime'] = DOCS_PATH.stat().st_mtime
        except:
            pass
    
    return hashlib.md5(str(key_data).encode()).hexdigest()


def save_document_store_cache(doc_store: InMemoryDocumentStore, cache_key: str, file_stats: dict):
    """Save document store to cache."""
    cache_file = CACHE_PATH / f"docstore_{cache_key}.pkl"
    metadata_file = CACHE_PATH / f"metadata_{cache_key}.json"
    
    try:
        # Save document store
        with open(cache_file, 'wb') as f:
            pickle.dump(doc_store, f)
        
        # Save metadata
        import json
        metadata = {
            'timestamp': time.time(),
            'datetime': datetime.now().isoformat(),
            'file_count': file_stats.get('total_files', 0),
            'sources': file_stats.get('sources', {}),
            'cache_key': cache_key
        }
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
            
        return True
    except Exception as e:
        st.error(f"Failed to save cache: {e}")
        return False


def load_document_store_cache(cache_key: str):
    """Load document store from cache."""
    cache_file = CACHE_PATH / f"docstore_{cache_key}.pkl"
    metadata_file = CACHE_PATH / f"metadata_{cache_key}.json"
    
    if not cache_file.exists():
        return None, None
    
    try:
        # Load document store
        with open(cache_file, 'rb') as f:
            doc_store = pickle.load(f)
        
        # Load metadata
        metadata = None
        if metadata_file.exists():
            import json
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        
        return doc_store, metadata
    except Exception as e:
        st.warning(f"Failed to load cache: {e}")
        return None, None


def get_cache_info():
    """Get information about existing caches."""
    cache_files = list(CACHE_PATH.glob("metadata_*.json"))
    caches = []
    
    for metadata_file in cache_files:
        try:
            import json
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
                caches.append(metadata)
        except:
            continue
    
    return sorted(caches, key=lambda x: x.get('timestamp', 0), reverse=True)


def clear_all_caches():
    """Clear all cached document stores."""
    try:
        for cache_file in CACHE_PATH.glob("docstore_*.pkl"):
            cache_file.unlink()
        for metadata_file in CACHE_PATH.glob("metadata_*.json"):
            metadata_file.unlink()
        return True
    except Exception as e:
        st.error(f"Failed to clear caches: {e}")
        return False


@st.cache_data(show_spinner=False)
def fetch_sagemath_files():
    """Fetch local SageMath documentation and source files."""
    files = []
    
    if not SAGE_PATH.exists():
        st.warning(f"SageMath path not found at {SAGE_PATH}. Skipping SageMath indexing.")
        return files
    
    st.write(f"Indexing local SageMath installation at {SAGE_PATH}")
    
    # Limit file size to avoid memory issues
    max_file_size = MAX_FILE_SIZE_MB * 1024 * 1024
    
    for pattern in SAGEMATH_PATTERNS:
        pattern_files = list(SAGE_PATH.glob(pattern))
        st.write(f"Found {len(pattern_files)} files matching pattern {pattern}")
        
        for p in pattern_files:
            try:
                # Skip very large files to avoid memory issues
                if p.stat().st_size > max_file_size:
                    continue
                    
                # Skip binary files and certain directories
                if any(skip in str(p) for skip in ['.git', '__pycache__', '.pyc', 'build', 'dist']):
                    continue
                
                data = {
                    "path": p,
                    "meta": {
                        "url_source": f"file://{p}",
                        "suffix": p.suffix,
                        "source": "SageMath Local",
                        "relative_path": str(p.relative_to(SAGE_PATH))
                    },
                }
                files.append(data)
            except (OSError, ValueError):
                # Skip files that can't be accessed
                continue
    
    st.write(f"Total SageMath files selected for indexing: {len(files)}")
    return files

@st.cache_data(show_spinner=False)
def fetch(documentations: List[Tuple[str, str, str]], include_sagemath: bool = True):
    files = []
    # Create the docs path if it doesn't exist
    DOCS_PATH.mkdir(parents=True, exist_ok=True)

    # Fetch remote documentation
    for name, url, pattern in documentations:
        st.write(f"Fetching {name} repository")
        repo = DOCS_PATH / name
        # Attempt cloning only if it doesn't exist
        if not repo.exists():
            subprocess.run(["git", "clone", "--depth", "1", url, str(repo)], check=True)
        res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            check=True,
            capture_output=True,
            encoding="utf-8",
            cwd=repo,
        )
        branch = res.stdout.strip()
        for p in repo.glob(pattern):
            data = {
                "path": p,
                "meta": {
                    "url_source": f"{url}/tree/{branch}/{p.relative_to(repo)}",
                    "suffix": p.suffix,
                    "source": name
                },
            }
            files.append(data)
    
    # Fetch local SageMath files if requested
    if include_sagemath:
        sagemath_files = fetch_sagemath_files()
        files.extend(sagemath_files)

    return files


def get_or_create_document_store(cache_key: str, index: str = "documentation"):
    """Get document store from cache or create new one."""
    # Try to load from cache first
    cached_store, metadata = load_document_store_cache(cache_key)
    
    if cached_store is not None:
        st.success(f"📁 Loaded cached index from {metadata.get('datetime', 'unknown time')} "
                  f"({metadata.get('file_count', 0)} files)")
        return cached_store, True  # True indicates cache hit
    
    # Create new document store if cache miss
    return InMemoryDocumentStore(index=index), False  # False indicates cache miss


def index_files(files, doc_store: InMemoryDocumentStore, cache_key: str):
    """Index files into the document store and save to cache."""
    # Create documents with special handling for Python files
    documents = []
    skipped_empty = 0
    
    for f in files:
        file_path = f["path"]
        meta = f["meta"]
        
        try:
            # Special handling for Python/Cython files
            if file_path.suffix in ['.py', '.pyx']:
                content = extract_python_docstrings(file_path)
            else:
                # Regular text file handling
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
            
            # Skip empty content to avoid warnings
            if not content or len(content.strip()) < 10:
                skipped_empty += 1
                continue
            
            # Create document
            doc = Document(
                content=content,
                meta=meta
            )
            documents.append(doc)
            
        except Exception as e:
            st.warning(f"Could not process file {file_path}: {e}")
            continue
    
    if skipped_empty > 0:
        st.info(f"Skipped {skipped_empty} files with empty or minimal content")
    
    if not documents:
        st.warning("No documents were successfully processed.")
        return {}
    
    st.info(f"Processing {len(documents)} documents for indexing...")
    
    # Create components for processing
    document_cleaner = DocumentCleaner()
    document_splitter = DocumentSplitter(split_length=500, split_overlap=50)
    document_writer = DocumentWriter(
        document_store=doc_store, policy=DuplicatePolicy.OVERWRITE
    )

    # Process documents through the pipeline
    cleaned_docs = document_cleaner.run(documents=documents)["documents"]
    split_docs = document_splitter.run(documents=cleaned_docs)["documents"]
    
    # Filter out any remaining empty documents after splitting
    non_empty_docs = [doc for doc in split_docs if doc.content and len(doc.content.strip()) > 10]
    
    if len(non_empty_docs) != len(split_docs):
        st.info(f"Filtered out {len(split_docs) - len(non_empty_docs)} empty document chunks")
    
    document_writer.run(documents=non_empty_docs)
    
    # Collect statistics for caching
    source_counts = {}
    for f in files:
        source = f["meta"].get("source", "Unknown")
        source_counts[source] = source_counts.get(source, 0) + 1
    
    file_stats = {
        'total_files': len(files),
        'processed_files': len(documents),
        'final_chunks': len(non_empty_docs),
        'sources': source_counts
    }
    
    # Save to cache
    st.info("💾 Saving to cache...")
    save_document_store_cache(doc_store, cache_key, file_stats)
    
    return file_stats


def search(question: str, doc_store: InMemoryDocumentStore) -> GeneratedAnswer:
    retriever = InMemoryBM25Retriever(document_store=doc_store, top_k=8)

    template = (
        "You are a mathematical expert assistant with access to SageMath, NumPy, and Pandas documentation. "
        "Provide a comprehensive and accurate answer to the mathematical or programming question based on the provided context. "
        "Use inline citations in the format [Source: filename] when referencing specific documentation. "
        "If the question involves mathematical concepts, explain them clearly. "
        "If it involves code, provide examples when possible. "
        "If the answer cannot be deduced from the context, clearly state that.\n\n"
        "For each document, I'll provide the source information:\n"
        "{% for doc in documents %}"
        "Document {{ loop.index }}: {{ doc.meta.relative_path or doc.meta.url_source or 'Unknown source' }}\n"
        "Content: {{ doc.content }}\n"
        "---\n"
        "{% endfor %}\n"
        "Question: {{ query }}\n\n"
        "Answer with inline citations:"
    )
    prompt_builder = PromptBuilder(template, required_variables=["documents", "query"])

    # Configure generator for local or remote OpenAI
    if USE_LOCAL_OPENAI:
        generator = OpenAIGenerator(
            model=OPENAI_MODEL,
            api_base_url=LOCAL_OPENAI_BASE_URL
        )
    else:
        generator = OpenAIGenerator(model=OPENAI_MODEL)
    
    answer_builder = AnswerBuilder()

    query_pipeline = Pipeline()

    query_pipeline.add_component("docs_retriever", retriever)
    query_pipeline.add_component("prompt_builder", prompt_builder)
    query_pipeline.add_component("llm", generator)
    query_pipeline.add_component("answer_builder", answer_builder)

    query_pipeline.connect("docs_retriever.documents", "prompt_builder.documents")
    query_pipeline.connect("prompt_builder.prompt", "llm.prompt")
    query_pipeline.connect("docs_retriever.documents", "answer_builder.documents")
    query_pipeline.connect("llm.replies", "answer_builder.replies")
    res = query_pipeline.run({"query": question})
    return res["answer_builder"]["answers"][0]


# Configuration sidebar
st.sidebar.header("Configuration")
include_sagemath = st.sidebar.checkbox("Include SageMath Documentation", value=INCLUDE_SAGEMATH_DEFAULT, 
                                      help="Include local SageMath installation in search")
include_remote = st.sidebar.checkbox("Include Remote Documentation", value=INCLUDE_REMOTE_DEFAULT,
                                    help="Include Pandas and NumPy documentation from GitHub")

# Cache management
with st.sidebar.expander("🗂️ Cache Management"):
    caches = get_cache_info()
    if caches:
        st.write(f"**{len(caches)} cache(s) available:**")
        for cache in caches[:3]:  # Show last 3 caches
            dt = datetime.fromisoformat(cache['datetime']).strftime('%m/%d %H:%M')
            st.write(f"• {dt} - {cache.get('file_count', 0)} files")
    else:
        st.write("No caches found")
    
    force_reindex = st.button("🔄 Force Re-index", help="Clear cache and rebuild index")
    if st.button("🗑️ Clear All Caches"):
        if clear_all_caches():
            st.success("Caches cleared!")
            st.rerun()

# Advanced settings
with st.sidebar.expander("Advanced Settings"):
    st.write(f"Max file size: {MAX_FILE_SIZE_MB} MB")
    st.write(f"SageMath path: `{SAGE_PATH}`")
    st.write(f"Using {'Local' if USE_LOCAL_OPENAI else 'Remote'} OpenAI")
    st.write(f"Cache path: `{CACHE_PATH}`")

# Determine what to include and generate cache key
sources_config = {
    'include_sagemath': include_sagemath,
    'include_remote': include_remote,
    'remote_docs': [d[0] for d in DOCUMENTATIONS] if include_remote else []
}

cache_key = get_cache_key(sources_config)
docs_to_include = DOCUMENTATIONS if include_remote else []
all_sources = [d[0] for d in docs_to_include]
if include_sagemath:
    all_sources.append("SageMath Local")

# Handle force reindex
if force_reindex:
    # Clear specific cache
    cache_file = CACHE_PATH / f"docstore_{cache_key}.pkl"
    metadata_file = CACHE_PATH / f"metadata_{cache_key}.json"
    if cache_file.exists():
        cache_file.unlink()
    if metadata_file.exists():
        metadata_file.unlink()
    st.success("Cache cleared! Re-indexing...")
    st.rerun()

# Get or create document store
doc_store, cache_hit = get_or_create_document_store(cache_key)

# Index files if cache miss
if not cache_hit:
    with st.status(
        "📚 Building documentation index...",
        expanded=st.session_state.get("expanded", True),
    ) as status:
        if include_remote:
            status.update(label="Fetching remote repositories...")
        files = fetch(docs_to_include, include_sagemath=include_sagemath)
        status.update(label="Indexing documentation...")
        file_stats = index_files(files, doc_store, cache_key)
        status.update(
            label="✅ Indexing complete and cached!", state="complete", expanded=False
        )
        st.session_state["expanded"] = False
else:
    # Still fetch files for statistics display
    files = fetch(docs_to_include, include_sagemath=include_sagemath)
    file_stats = {
        'total_files': len(files),
        'sources': {}
    }
    for f in files:
        source = f["meta"].get("source", "Unknown")
        file_stats['sources'][source] = file_stats['sources'].get(source, 0) + 1


st.header("🔎 Mathematical Documentation Finder", divider="rainbow")

if all_sources:
    st.caption(
        f"Search through documentation for: {', '.join(all_sources)}"
    )
else:
    st.warning("No documentation sources selected. Please enable at least one source in the sidebar.")

if all_sources and (question := st.text_input(
    label="What do you need to know?", 
    placeholder="What is a Coxeter group? How do I compute lattice invariants? What is a DataFrame?"
)):
    with st.spinner("Searching through documentation..."):
        answer = search(question, doc_store)

    if not st.session_state.get("run_once", False):
        st.balloons()
        st.session_state["run_once"] = True

    st.markdown(answer.data)
    
    # Show source references in a compact format
    if answer.documents:
        with st.expander(f"📚 Source References ({len(answer.documents)} documents)", expanded=False):
            for i, document in enumerate(answer.documents, 1):
                source = document.meta.get("source", "Unknown")
                relative_path = document.meta.get("relative_path", "")
                url_source = document.meta.get("url_source", "")
                
                st.write(f"**Document {i}:** `{relative_path or url_source or 'Unknown'}` ({source})")
                if len(document.content) > 200:
                    st.text(document.content[:200] + "...")
                else:
                    st.text(document.content)
                if i < len(answer.documents):
                    st.divider()

# Show statistics
if all_sources:
    st.sidebar.header("📊 Documentation Statistics")
    if 'file_stats' in locals():
        st.sidebar.metric("Total Files", file_stats.get('total_files', 0))
        
        # Show cache status
        cache_status = "🟢 Cached" if cache_hit else "🔄 Fresh Index"
        st.sidebar.write(f"**Status:** {cache_status}")
        
        # Count by source
        source_counts = file_stats.get('sources', {})
        for source, count in source_counts.items():
            st.sidebar.metric(f"{source} Files", count)