"""
숫자야구
랜덤의 4자리 숫자를 맞춰야 한다.

### num = 맞춰야 하는 4자리 숫자
### 

#### 4자리 숫자 조건
0000 ~ 9999
같은 숫자를 여러번 사용할 수 있으며, 섞어서 사용할 수 있다.
** 첫자리에 0을 사용하려면 값을 정수(int)가 아닌 문자열(str)로 받아야 한다.


#### 숫자야구 룰
`strike` 일치하는 숫자가 있을 때 (위치까지 일치)
`ball` 위치는 다르지만 일치하는 숫자는 있을때 (위치 X, 숫자 O)
`out` 일치하는 숫자가 존재하지 않을때.
"""
import random


# 랜덤 숫자 생성
def create_num():
    # int_num = random.randint(0000, 9999) # 4자리의 랜덤 숫자 생성
    # if len(str(int_num)) == 3: # 만약 숫자가 3자리로 생성 되었을 때
    #     num = '0' + str(int_num) # 앞에 0을 추가해줌.
    #     return num
    # else:
    #     return str(int_num) # 아닌 경우 str 문자열로 return.
    return str(random.randint(0, 9999)).zfill(4) #
    
def check_strike(in_num: str, num: str):
    check_ball = []
    strike_count = 0
    if in_num[0] == num[0]:
        strike_count += 1
        check_ball.append('-')
    else:
        check_ball.append(in_num[0])
    if in_num[1] == num[1]:
        strike_count += 1
        check_ball.append('-')
    else:
        check_ball.append(in_num[1])
    if in_num[2] == num[2]:
        strike_count += 1
        check_ball.append('-')
    else:
        check_ball.append(in_num[2])
    if in_num[3] == num[3]:
        strike_count += 1
        check_ball.append('-')
    else:
        check_ball.append(in_num[3])

    return strike_count, check_ball

def check_ball(check_ball_list, num):
    ball_count = 0
    num = list(num) # 정답 숫자 list 화
    ball_list = check_ball_list.copy() ### list 복사
    for i in num:
        if i in ball_list:
            ball_count += 1
            ball_list.remove(i) ### 중복 인식 방지하기 위한 안전장치
    return ball_count
    
# 검증 로직
def check_num(in_num: str, num: str):
    # 정답
    if in_num == num:
        return 'strike!!!'
    # list화
    in_num = list(in_num)
    # strike 개수 확인
    strike_count, check_ball_list = check_strike(in_num, num)
    # ball 개수 확인
    ball_count = check_ball(check_ball_list, num)
    if ball_count == 0 and strike_count == 0: ###
            return 'out!!!'
    else:
        return f'{strike_count} Strike, {ball_count} Ball.'
    
# 게임 로직
def start_game():
    num = create_num() # 숫자 생성
    challenge_count = 0 # 도전 횟수 카운팅을 위한 초기값.
    print(num)
    while num:
        in_num = input('4자리 숫자를 입력하세요. : ') # 숫자 유추 과정.
        check = check_num(in_num, num) # 검증 로직 작동
        challenge_count += 1
        print(f'{challenge_count} 번째 시도, {check}') # 검증 로직 결과 출력.
        if check == 'strike!!!': # 정답일 경우 반복문 종료
            break
        


def NBB_game():
    start = input('게임을 시작하겠습니까? (y, n) : ')
    while start == 'y':
        start_game() # 게임 로직 실행 (함수 호출)
        restart = input('다시 도전하시겠습니까? (y, n) : ')
        if restart == 'n':
            break
        # if restart == 'y':
        #     return start_game()
        # else:
        #     print('goodbye:)')
    if start == 'n':
        return 'goodbye:)'
    else:
        print('잘못된 입력입니다.')
        return start_game()



NBB_game()