"""
Docstring for app.services.create
게임 시작 요청 시 초기화 로직 작성

- create_number : 4자리 랜덤 숫자 생성
"""
import random

# 랜덤 숫자 생성
def create_number():
    """
    0~9999까지의 랜덤 숫자를 생성한다.
    단, 3자리 이하의 숫자일 경우 zfill 메서드 활용해 앞에 0을 추가한다.
    """
    return str(random.randint(0,9999)).zfill(4) # 0000 ~ 9999 까지 랜덤 숫자 생성