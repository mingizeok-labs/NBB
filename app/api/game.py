"""
Docstring for app.api.game
게임 진행을 위한 router 작성

### start
게임 시작 시, 게임 진행을 위한 초기화 설정을 한다.
- 세션 구성
- 랜덤 숫자 생성

** 기능 관련 로직은 services에 작성 **
"""
from fastapi import APIRouter, Request

from app.services import create, session


router = APIRouter(prefix='/nbb/api/v1', tags=['GAME'])

@router.post('/start', description='게임 초기화')
async def game_setting(request: Request):
    number = create.create_number() # 랜덤 숫자 생성
    session.init(request.session, number) # 세션 초기화 -> 구성
    test = {
        'number': request.session['answer'],
        'count': request.session['count'],
        'history': request.session['history']
    }
    return test