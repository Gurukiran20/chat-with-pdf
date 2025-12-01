from typing import List


def split_text_into_chunks(
    text: str,
    chunk_size: int = 800,
    overlap: int = 200,
) -> List[str]:
    """
    Split long text into overlapping chunks.

    - chunk_size: approx number of words per chunk
    - overlap: words repeated between chunks to keep context
    """
    words = text.split()
    chunks: List[str] = []

    if not words:
        return chunks

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)

        # move start forward with overlap
        start = end - overlap
        if start < 0:
            start = 0

    return chunks
