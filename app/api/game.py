"""
Docstring for app.api.game
게임 진행을 위한 router 작성

** 기능 관련 로직은 services에 작성 **
"""
from fastapi import APIRouter, Request, Depends
from fastapi.responses import ORJSONResponse

from app.core.session import init, SessionDataGroup, get_session_data, SessionUpdate, session_reset
from app.schemas.game_setting import InputNumber
from app.schemas.response_model import GameResultResponse, NowStatusResponse
from app.services import create, game


router = APIRouter(prefix='/nbb/api/v1', tags=['GAME'])

@router.post('/start', description='게임 초기화', status_code=201)
async def game_setting(request: Request):
    """
    ### start
    게임 시작 시, 게임 진행을 위한 초기화 설정을 한다.
    - 세션 구성
    - 랜덤 숫자 생성
    """
    number = create.create_number() # 랜덤 숫자 생성
    init(request.session, number) # 세션 초기화 -> 구성
    test = {
        'status': request.session['status'],
        'number': request.session['answer'],
        'count': request.session['count'],
        'history': request.session['history']
    }
    return test


@router.post('/lets_play', description='게임 진행', response_class=ORJSONResponse, response_model=GameResultResponse)
async def playing_game(
    input_num: InputNumber, # 유저가 입력한 값이 숫자인지 검증
    session_data: SessionDataGroup = Depends(get_session_data), # 의존성 부여, Sessiondata 불러오는 함수 먼저 실행
    request: Request = Depends
    ):
    """
    ### lets_play
    게임 진행 관련 로직실행
    - 유저에게 숫자 입력을 받음 : input_number -> InputNumber
    - 정답과 비교한 값을 리턴 : Verification.check_logic()
    """
    v = game.Verification( # 비교 로직
        input_number=input_num.input, # 유저가 입력한 검증된 데이터 값
        answer=session_data.answer # 세션에 저장되어있는 정답을 가져옴
        )
    
    result = v.check_logic() # 비교 값 -> history에 함께 넣기 위해 변수 할당


    session_update = SessionUpdate(request)

    update_status = session_data.status # 기본값 할당

    if result[input_num.input] == '정답':
        update_status = session_update.update_status_end()
    
    elif session_data.status != 'in_progress':
        update_status = session_update.update_status_ing()

    update_history = session_update.update_history(result)
    update_count = session_update.counting()
    
    return {
        'input': result,
        'status': update_status,
        'count': update_count,
        'history': update_history
    }


@router.get('/lets_play', description='게임 상태 조회', response_class=ORJSONResponse, response_model=NowStatusResponse)
def now_status(session_data : SessionDataGroup = Depends(get_session_data)):
    return {
        'status': session_data.status,
        'history': session_data.history
    }
    

@router.post('/reset', description='게임 종료', status_code=204)
def reset_session(request: Request):
    reset_msg = session_reset(request.session)
    return {'게임 종료': reset_msg}