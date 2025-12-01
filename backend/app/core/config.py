import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # points to backend/

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    DATA_DIR: Path = Path(os.getenv("DATA_DIR", BASE_DIR / "data" / "uploads"))
    STORAGE_DIR: Path = Path(os.getenv("STORAGE_DIR", BASE_DIR / "storage"))
    EMBEDDING_MODEL: str = "models/text-embedding-004"
    CHAT_MODEL: str = "gemini-2.5-flash"

settings = Settings()
