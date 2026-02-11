"""
Docstring for app.schemas.response_model
API 요청 시 반환하는 Response Model을 작성
"""

from pydantic import BaseModel

class GameResultResponse(BaseModel):
    input : dict[str, str] = {'5678':'out'}
    status : str
    count : int = 2
    history : list[dict[str, dict[str, str]]] = [{'1': {'1234': '0S2B'}}, {'2': {'5678': 'out'}}]

class NowStatusResponse(BaseModel):
    status : str
    history : list[dict[str, dict[str, str]]] = [{'1': {'1234': '0S2B'}}, {'2': {'5678': 'out'}}]