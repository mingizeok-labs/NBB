"""
Docstring for app.services.session
게임 진행을 위한 세션 관련 로직 작성

- init : 세션 초기화 
"""
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

