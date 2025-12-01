import json
from pathlib import Path
from typing import List, Dict, Any
import uuid

import numpy as np

from app.core.config import settings
from app.services.embeddings import get_embedding

# index file path
INDEX_PATH = settings.STORAGE_DIR / "index.json"
INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_index() -> List[Dict[str, Any]]:
    if not INDEX_PATH.exists():
        return []
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index(index: List[Dict[str, Any]]) -> None:
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


def add_document_chunks(original_filename: str, chunks: List[str]) -> str:
    """
    Add all chunks of a document into the index with embeddings.
    Returns a generated doc_id for this document.
    """
    index = load_index()

    doc_id = str(uuid.uuid4())

    for chunk in chunks:
        if not chunk.strip():
            continue

        emb = get_embedding(chunk)

        index.append(
            {
                "doc_id": doc_id,
                "source_filename": original_filename,
                "text": chunk,
                "embedding": emb,
            }
        )

    save_index(index)
    return doc_id


def search_similar(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Search top_k most similar chunks to the query.
    """
    index = load_index()
    if not index:
        return []

    q_emb = np.array(get_embedding(query))

    scores = []
    for item in index:
        emb = np.array(item["embedding"])
        # cosine similarity
        sim = float(
            np.dot(q_emb, emb)
            / (np.linalg.norm(q_emb) * np.linalg.norm(emb) + 1e-10)
        )
        scores.append(sim)

    # sort by similarity
    sorted_pairs = sorted(zip(index, scores), key=lambda x: x[1], reverse=True)
    top_items = [item for item, _score in sorted_pairs[:top_k]]
    return top_items
