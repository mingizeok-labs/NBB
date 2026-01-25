"""
Docstring for app.core.session
Session에 저장되어있는 데이터 관리 로직 작성

"""
from fastapi import Request

from app.schemas.game_setting import SessionData

# 세션 초기화
def init(session: dict, number):
    """
    Docstring for init
    게임 시작 시, 세션 초기화 함수
    """
    session.clear() # 이전 게임 기록 제거
    
    session['answer'] = number # 정답
    session['count'] = 0 # 시도 횟수 카운트 초기화
    session['history'] = [] # 답안 제출 이력 초기화 ex) '첫번째 답안': 1234

class SessionDataGroup:
    """
    Docstring for SessionDataGroup
    세션에 저장되어있는 데이터 객체화를 위한 class 정의
    """
    def __init__(self, request: Request):
        data = SessionData(**request.session) # 세션 불러오기

        # 변수에 데이터 할당
        self.answer = data.answer
        self.count = data.count
        self.history = data.history

def get_session_data(request: Request) -> SessionDataGroup:
    """
    Docstring for get_session_data
    SessionDataGrop 객체화를 위한 함수
    ex)
    Depends(get_session_data)

    :param request: Description
    :type request: Request
    :return: Description
    :rtype: SessionDataGroup
    """
    return SessionDataGroup(request)

class SessionUpdate:
    """
    Docstring for SessionUpdate
    게임 진행 중 업데이트 사항들을 세션에 반영
    - update_history : 제출 이력
    - counting : 제출 횟수
    """
    def __init__(self, request: Request):
        self.org = get_session_data(request)
        self.session = request.session

    def update_history(self, input_data: dict):
        data = {str(self.org.count + 1): input_data}
        self.session['history'].append(data)
        return self.session['history']

    def counting(self):
        self.session['count'] = self.org.count + 1
        return self.session['count']