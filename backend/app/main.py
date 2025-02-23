import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Query
from api.routers import router

app = FastAPI(title="종원 테스트서버")
# 라우터 바인딩
app.include_router(router)