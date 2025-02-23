from fastapi import APIRouter
from backend.app.api.endpoints import ollama

router = APIRouter()
# LLM
router.include_router(ollama.router, prefix="/chat", tags=["LLM"])