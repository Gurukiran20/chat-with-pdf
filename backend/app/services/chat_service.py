from typing import List, Dict

import google.generativeai as genai

from app.core.config import settings
from app.services.vector_store import search_similar

# configure Gemini (safe to call again)
genai.configure(api_key=settings.GEMINI_API_KEY)


def build_context_from_chunks(chunks: List[Dict]) -> str:
    """
    Build a big context string from the retrieved chunks.
    """
    parts = []
    for i, ch in enumerate(chunks, start=1):
        source = ch.get("source_filename", "unknown.pdf")
        text = ch.get("text", "")
        parts.append(f"[Chunk {i} | Source: {source}]\n{text}")
    return "\n\n".join(parts)


def chat_with_pdf(user_message: str) -> str:
    """
    Retrieve relevant chunks for the question, and ask Gemini to answer based on them.
    """
    # 1) retrieve similar chunks
    chunks = search_similar(user_message, top_k=5)

    if not chunks:
        return "I couldn't find any indexed documents. Please upload a PDF first and try again."

    # 2) build context
    context = build_context_from_chunks(chunks)

    # 3) build prompt for Gemini
    prompt = f"""
You are a helpful AI assistant that answers questions based ONLY on the PDF content provided.

If the answer is not clearly present in the PDF content, say:
"I’m not sure from the given PDFs." and maybe suggest what they could look for.

PDF content (from multiple chunks):

{context}

User question: {user_message}

Now answer the user's question in a clear, concise way based only on the PDF content above.
"""

    model = genai.GenerativeModel(settings.CHAT_MODEL)
    try:
        response = model.generate_content(prompt)
    except Exception as e:
        # avoid 500 in frontend, return readable error instead
        return f"Error while calling Gemini: {e}"

    return response.text or "I couldn't generate a response. Please try rephrasing your question."
