from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.config import settings

app = FastAPI()

app.add_middleware( # SessionMiddleware 추가
    SessionMiddleware,
    secret_key = settings.SESSION_KEY
)


@app.get("/")
def read_root():
    return {"Number_BaseBall": "야구는 그리 좋아하진 않지만 숫자야구는 그래도 해볼만 하지 않나."}
