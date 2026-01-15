from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Number_BaseBall": "야구는 그리 좋아하진 않지만 숫자야구는 그래도 해볼만 하지 않나."}
