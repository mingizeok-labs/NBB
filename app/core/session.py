"""
Docstring for app.api.session
Session에 저장되어있는 데이터 관리 로직 작성

"""
from fastapi import Request

from app.schemas.game_setting import SessionData

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