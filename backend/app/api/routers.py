from fastapi import APIRouter
from api.endpoints import ollama, user

router = APIRouter()
# LLM
router.include_router(ollama.router, prefix="/chat", tags=["LLM"])
# user
router.include_router(user.router, prefix="/users", tags=["user"])