# 1. 컴퓨터와 사용자가 가위바위보 게임을 한다.
# 2. 컴퓨터는 random()함수를 사용해서 선택하고,
# 3. 사용자는 입력을 통해 선택할 수 있게 한다.
# 4. 가위 : 0, 바위 : 1, 보 : 2로 한다.
# 5. 결과를 판정해서 누가 이겼는지를 출력한다.
# 6. 게임을 종료를 선택할 때까지, 계속하게 한다.
# 7. 최종 결과를 컴퓨터, 사용자 각각에 대해 승 수를 카운트한다.

# 힌트 : 가위바위보를 리스트로 만들어 놓고 시작한다.

import random

game_over = True
Stop = 0
com_score = 0
user_score = 0

game_list = ['scissors', 'rock', 'paper']

while game_over:
  com = random.randint(0, 2)
  user = int(input("가위(0), 바위(1), 보(2)를 입력하세요 : "))

  print(f"컴퓨터 : {game_list[com]}")
  print(f"사용자 : {game_list[user]}")

  if com == user:
    print("비겼습니다.")
  elif (com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1):
    print("컴퓨터가 이겼습니다.")
    com_score += 1
  else:
    print("사용자가 이겼습니다.")
    user_score += 1
  print()

  Stop == input("게임을 종료하시겠습니까? 종료(y), 계속(n) :")
  if Stop == 'y':
    game_over = False

print(f"컴퓨터 : {com_score}승, 사용자 :{user_score}승")