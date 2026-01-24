"""
Docstring for app.api.test_router
API test 진행하기 위한 Session Setting
"""
from fastapi import APIRouter, Request

from app.services import session

router = APIRouter(prefix='/__test__')

@router.post('/session/mock')
def set_session(request: Request):
    """
    Docstring for set_session
    API test를 위한 세션에 데이터 저장
    """
    session.init(request.session, number='0987')
    return {'Are YOU Ready?': 'Yes!'}