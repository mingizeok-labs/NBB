"""
Docstring for app.services.game
유저가 입력한 숫자 값을 검증하는 로직 작성

- 정답 검증
- strike 검증
- ball 검증
- 해당사항 없을 때, `out` return
"""

class Verification:
    """
    Docstring for Verification
    숫자야구 숫자 검증 로직
    """
    def __init__(self, input_number: str, answer: str):
        self.input_number = input_number # 유저가 입력한 값
        self.answer = answer # 정답
        self.list_answer = list(answer)

    def check_logic(self):
        check = self._correct()
        if check[self.input_number] == '정답':
            return check
        else:
            strike = self._strike()
            ball = self._ball()
            if ball == 0 and strike == 0:
                return {self.input_number: 'out'}
            return {self.input_number: f'{strike}S{ball}B'}

    def _correct(self):
        if self.input_number == self.answer:
            return {self.input_number: '정답'}
        return {self.input_number: '오답'}

    def _strike(self):
        strike_count = 0
        for i in range(4):
            if self.input_number[i] == self.answer[i]:
                strike_count += 1
                self.list_answer[i] = None
        return strike_count

    def _ball(self):
        ball_count = 0
        for i in range(4):
            if self.input_number[i] != self.answer[i]:
                if self.input_number[i] in self.list_answer:
                    ball_count += 1
                    idx = self.list_answer.index(self.input_number[i]) ### 중복 인식 방지하기 위한 안전장치
                    self.list_answer[idx] = None
        return ball_count
