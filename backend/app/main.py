from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes_upload import router as upload_router
from app.api.routes_chat import router as chat_router

app = FastAPI(title="Chat with PDF")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "Chat with PDF backend is running",
    }

@app.get("/config-check")
def config_check():
    return {
        "has_gemini_key": bool(settings.GEMINI_API_KEY),
        "data_dir": str(settings.DATA_DIR),
        "storage_dir": str(settings.STORAGE_DIR),
    }

# Routers
app.include_router(upload_router)
app.include_router(chat_router)
