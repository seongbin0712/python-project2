# random 모듈을 import
import random

# random 함수 종류
# 1. randint (숫자의 시작값과 끝값정하기)

result = random.randint(0, 100) # result = 0 ~ 100 사이의 수중 무작위로 가져옴

# 2. choice (리스트나 튜플 등 정해진 값에서 하나를 선택하는 경우)
colors = ["red", "blue", "green", "skyblue"]
result = random.choice(colors) # result = colors(리스트)에서 [리스트 안에 있는 값] 중 무작위로 선택함

# 3. uniform (실수의 범위에서 무작위 값을 반환)

result = random.uniform(0.2, 0.9) # 0.2 ~ 0.9 중 무작위 값을 반환함

# 4. shuffle

colors = ["red", "blue", "green", "skyblue"]
result = random.shuffle(colors) # colors(리스트)에서 순서를 무작위로 변경함
                                # 실행 결과 예시 : colors = ["blue", "green", "red", "skyblue"]