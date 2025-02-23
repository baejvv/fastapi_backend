import uvicorn
from fastapi import FastAPI, Query
from backend.app.api.routers import router


app = FastAPI(title="종원 테스트서버")

# 라우터 바인딩
app.include_router(router)