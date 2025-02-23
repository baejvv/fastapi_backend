from fastapi import APIRouter, HTTPException
from services.ollama_service import chat_with_llama3

router = APIRouter()

@router.get("/ollama3", summary="ollama3 모델 사용")
def chat_ollama3(prompt: str) -> str:
    return chat_with_llama3(prompt)