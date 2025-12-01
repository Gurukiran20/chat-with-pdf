from typing import List

import google.generativeai as genai

from app.core.config import settings

# configure Gemini client once
genai.configure(api_key=settings.GEMINI_API_KEY)


def get_embedding(text: str) -> List[float]:
    """
    Get embedding vector for a given text using Gemini.
    """
    result = genai.embed_content(
        model=settings.EMBEDDING_MODEL,
        content=text,
    )
    # result["embedding"] is a list of floats
    return result["embedding"]
