# 숫자 기억하기
# 컴퓨터에서 무작위로 숫자를 보여준다.
# 보여줘야 하는 숫자의 갯수는 사용자로 부터 입력 받는다.
# 컴퓨터가 입력 받은 숫자 갯수 만큼 random으로 생성하고,
# 각 숫자를 1초씩 화면에서 보여준다.
# 사용자가 기억한 숫자를 입력하고,
# 결과를 판정한다.

import turtle as t
import time
import random

play = True
score = 0

t.bgcolor("pink")
t.ht()
t.up()

go_on = "y"

while play:
  num = ""

  num_times = int(t.textinput("숫자 기억 게임", "몇개의 숫자로 진행하시겠습니까?"))
  t.clear()
  t.goto(0, 0)
  t.write("숫자 기억하기 게임을 시작합니다.", False, "center", ("", 30))

  time.sleep(3)
  t.clear()

  for x in range(num_times):
    rand_num = random.randint(1, 30)
    t.write(rand_num, False, "center", ("", 70))
    num = num + str(rand_num) + " "
    time.sleep(1)
    t.clear()

  user_input = t.textinput("숫자 기억 게임", "기억한 숫자를 입력하세요. (숫자 사이 공백)")

  # strip - 앞뒤 공백 제거
  if user_input == num.strip():
    t.write("정답입니다", False, "center", ("", 30))
    score += 1
    t.goto(0, -100)
    t.write(f"지금까지 성공한 게임은 {score}판입니다.", False, "center", ("", 30))
    time.sleep(2)
    t.clear()
  else:
    t.goto(0, 0)
    t.write("오답입니다.", False, "center", ("", 30))
    t.goto(0, -50)
    t.write(f"정답은 {num}입니다.", False, "center", ("", 30))
    t.goto(0, -100)
    t.write(f"입력한 숫자는 {user_input}입니다.", False, "center", ("", 30))
    t.goto(0, -150)
    t.write(f"지금까지 성공한 게임은 {score}판입니다.", False, "center", ("", 30))
    time.sleep(2)
    t.clear()
  
  re_go = t.textinput("숫자 기억하기", "게임을 종료하시겠습니까?")
  if re_go == go_on:
    play = False
  
t.mainloop()