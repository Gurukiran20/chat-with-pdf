from pathlib import Path
import uuid

import PyPDF2

from app.core.config import settings


def ensure_data_dir() -> Path:
    """Ensure the uploads directory exists and return it."""
    uploads_dir = settings.DATA_DIR
    uploads_dir.mkdir(parents=True, exist_ok=True)
    return uploads_dir


def save_pdf(file_obj, original_filename: str) -> Path:
    """
    Save uploaded PDF into data/uploads with a generated ID name.
    Returns full path to saved file.
    """
    uploads_dir = ensure_data_dir()

    # generate unique file name
    doc_id = str(uuid.uuid4())
    filename = f"{doc_id}.pdf"

    file_path = uploads_dir / filename

    # write file bytes
    with open(file_path, "wb") as f:
        f.write(file_obj.read())

    return file_path


def extract_text_from_pdf(path: Path) -> str:
    """Extract raw text from a PDF file."""
    text_parts = []

    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)

    return "\n".join(text_parts)
