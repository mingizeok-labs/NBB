"""
Docstring for app.schemas.game_setting
게임 세팅과 관련된 스키마 관리
"""

from pydantic import BaseModel, field_validator

class SessionData(BaseModel):
    """
    Docstring for SessionData
    세션에 저장되어있는 정보
    - answer : 정답
    - count : 시도 횟수
    - history : 제출 이력
    """
    answer : str
    count : int
    history : dict[str, str]


class RandomInt(BaseModel):
    """
    Docstring for RandomInt
    랜덤으로 생성된 숫자가 문제 없이 생성 되었는지 검증
    """
    number : str

    @field_validator('number')
    @classmethod
    def is_valid_number(cls, v):
        if len(v) != 4: # 4자리로 이루어져있는지 검증
            raise ValueError('랜덤숫자 생성 오류: 4자리 숫자가 아닙니다.')
        if not v.isdigit(): # 만들어진 숫자에 다른 문자열이 포함되어있는지 검증
            raise ValueError('랜덤숫자 생성 오류: 숫자가 아닌 문자열이 포함되어있습니다.')
        return v
    

class InputNumber(BaseModel):
    """
    Docstring for InputNumber
    유저가 입력한 데이터가 숫자로 구성된 4자리의 문자열인지 검증
    """
    input : str

    @field_validator('input')
    @classmethod
    def is_valid_input(cls, v):
        if not v.isdigit():
            raise ValueError('입력 오류: 숫자만 입력해주세요.')
        if len(v) != 4:
            raise ValueError('입력 오류: 4자리 숫자만 입력해주세요.')
        return v
    