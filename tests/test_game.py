from fastapi.testclient import TestClient
from pydantic import ValidationError
from pytest import raises

from app.main import app
from app.services.create import create_number
from app.services.game import Verification
from app.schemas.game_setting import RandomInt

client = TestClient(app)

# 게임 시작 시, 초기화 test
def test_game_setting(): # API test / session 생성 확인
    response = client.post('/nbb/api/v1/start')
    assert response.status_code == 200 # 초기화 성공

# 랜덤숫자 생성 test
def test_create_number():
    number = create_number()
    valid = RandomInt(number=number)
    assert valid.number.isdecimal() == True

# RandomInt 검증로직 실패케이스
class RandomIntFailCaseTest:
    ### 1 글자수 오류
    def test_randomint_fail_1():
        with raises(ValidationError): # 오류 발생 시 test 통과
            RandomInt(number='012')

        with raises(ValidationError):
            RandomInt(number='99999')

    ### 2 숫자가 아닌 다른 문자열 포함 오류
    def test_randomint_fail_2():
        with raises(ValidationError):
            RandomInt(number='테스트 케이스 작성 중')

        with raises(ValidationError):
            RandomInt(number='ab34')

    ### 3 데이터가 없을 때
    def test_randomint_fail_3():
        with raises(ValidationError):
            RandomInt(number='')

# 숫자 검증 로직 test
class TestVerification:
    def test_success_case_1(self):
        v = Verification(input_number='1234', answer='1234')
        assert v.check_logic()['1234'] == '정답'

    def test_success_case_2(self):
        v = Verification(input_number='1256', answer='1234')
        assert v.check_logic()['1256'] == '2S0B'

    def test_success_case_3(self):
        v = Verification(input_number='1243', answer='1234')
        assert v.check_logic()['1243'] == '2S2B'

    def test_success_case_4(self):
        v = Verification(input_number='3412', answer='1234')
        assert v.check_logic()['3412'] == '0S4B'
    
    def test_success_case_5(self):
        v = Verification(input_number='0909', answer='1234')
        assert v.check_logic()['0909'] == 'out'