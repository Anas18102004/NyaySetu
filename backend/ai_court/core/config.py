import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional

# Load environment variables at the very beginning
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "LegalDebateAPI"
    PORT: int = 8000
    CORS_ORIGINS: str = Field(default="*", env="CORS_ORIGINS")  # Consider restricting in production
    UPLOADS_DIR: str = "uploads"

    QDRANT_URL: Optional[str] = Field(default=None, env="QDRANT_URL")
    QDRANT_API_KEY: Optional[str] = Field(default=None, env="QDRANT_API_KEY")

    GOOGLE_API_KEY: Optional[str] = Field(default=None, env="GOOGLE_API_KEY")
    GEMINI_MODEL_NAME: str = "gemini-1.5-flash"
    
    # ElevenLabs API Key for voice synthesis
    ELEVENLABS_API_KEY: str = Field(default="", env="ELEVENLABS_API_KEY")
    
    EMBEDDING_MODEL_NAME: str = "BAAI/bge-large-en-v1.5"
    
    QDRANT_QNA_COLLECTION: str = "legal_qna_bge_large"
    QDRANT_CASE_COLLECTION: str = "Judge_Lawyer_Case_Large"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
