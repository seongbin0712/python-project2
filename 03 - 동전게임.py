# spec.
# 1. 컴퓨터가 동전을 던지고, 사용자는 앞/뒤면을 맞춘다.
# 2. 사용자는 앞/뒤면을 입력한다.
# 3. 컴퓨터가 동전을 던진 결과와 사용자가 입력한 값이 같으면,
# "맞추었습니다" 라는 문고를 출력하고, 틀렸으면, "틀렸습니다."를 출력한다.

# 힌트
# 1. 컴퓨터가 동전을 던질 때는, random.randint(0, 1) 함수를 사용한다.

import random


#게임 소개
print("=" * 50)
print(" 동전 던지기 게임에 오신 것을 환영합니다.\n")
print("'던져진 동전의 앞/뒤면을 맞추는 게임입니다'")
print("=" * 50)

com = random.randint(0,1)

#던져진 동전의 앞/뒤면 맞추기
print("컴퓨터가 동전을 던졌습니다! 앞이라면 0, 뒤라면 1을 입력해주세요")

user = input("입력 : ")
int(user)

print()

# 동전 던지기
if com:
  print("컴퓨터의 선택은 '뒤'입니다.\n")
else:
  print("컴퓨터의 선택은 '앞'입니다.\n")

# 사용자의 선택
if user == 0:
  print("사용자님의 선택은 '앞'입니다\n")


# 판정
if user == com:
  print("정답입니다!")
else:
  print("틀렸습니다.")