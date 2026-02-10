from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.api.game import router as game_router
from app.api.test_router import router as test_router

from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = list(settings.ALLOWED_ORIGINS), # 브라우저 주소 허용
    allow_credentials = True, # 세션 쿠키 통과
    allow_methods = settings.ALLOWED_METHODS,
    allow_headers = settings.ALLOWED_HEADERS,
)

app.add_middleware( # SessionMiddleware 추가
    SessionMiddleware,
    secret_key = settings.SESSION_KEY,
    max_age=settings.SESSION_MAX_AGE,
    https_only=settings.USE_HTTPS,
)

# Router
app.include_router(game_router)

# Test Router
if settings.ENV == 'test':
    app.include_router(test_router)

@app.get("/")
def read_root():
    return {"Number_BaseBall": "야구는 그리 좋아하진 않지만 숫자야구는 그래도 해볼만 하지 않나."}
