# 숫자를 랜덤으로 3개를 생성하고, 순서대로 아래의 식에 대입한다.
# num1, num2, num3
# 식 : num1 * num2 - num3 = result

# 답 판정
# 정답 혹은 오답 결과 출력

# 오답이면 종료
# 정답이면 Count를 증가시킨다

# 힌트)

# 1. while문을 사용해야한다.
# 2. 3개의 숫자 생성, 값 입력, 답 판정

import random

# 전역변수 선언, 값을 누적하기
# 전역변수가 int, float일때는 0으로 초기화하고, 문자열이면 ""로 초기화한다.
count = 0
play = True

while play:
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 10)
  num3 = random.randint(0, 10)
  
  math_ex = num1 * num2 + num3

  print(f"문제는 {num1} * {num2} + {num3}입니다")

  result = int(input(f"{num1} * {num2} + {num3} = "))

  if math_ex == result:
    count += 1
    print(f"정답입니다! 현재 맞힌 문제 수는 {count}개입니다\n")
  else:
    print(f"오답입니다. 정답은 {math_ex}입니다.")
    print(f"지금까지 맞힌 문제 갯수는 {count}개입니다.")
    play = False