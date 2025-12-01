from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_loader import save_pdf, extract_text_from_pdf
from app.services.text_splitter import split_text_into_chunks
from app.services.vector_store import add_document_chunks

router = APIRouter(prefix="/api", tags=["upload"])


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # save file
    saved_path = save_pdf(file.file, file.filename)

    # extract text
    text = extract_text_from_pdf(saved_path)

    # split into chunks
    chunks = split_text_into_chunks(text)

    # store chunks + embeddings in vector index
    doc_id = add_document_chunks(file.filename, chunks)

    return {
        "doc_id": doc_id,
        "filename": file.filename,
        "saved_path": str(saved_path),
        "num_characters": len(text),
        "num_chunks": len(chunks),
        "first_chunk_preview": chunks[0][:500] if chunks else "",
    }
