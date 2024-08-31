from turtle import Turtle, Screen
import time
import random

def create_snake(pos):
  snake_body = Turtle()
  snake_body.shape("square")
  snake_body.color("orangered")
  snake_body.up()
  snake_body.goto(pos)
  snakes.append(snake_body)

def rand_pos():
  rand_X = random.randint(-250, 250)
  rand_Y = random.randint(-250, 250)
  return rand_X, rand_Y

def up():
  if snakes[0].heading() != 270:
    snakes[0].setheading(90)

def down():
  if snakes[0].heading() != 90:
    snakes[0].setheading(270)

def left():
  if snakes[0].heading() != 0:
    snakes[0].setheading(180)

def right():
  if snakes[0].heading() != 180:
    snakes[0].setheading(0)

def score_update():
  global score
  score += 1
  score_pen.clear()
  score_pen.write(f'점수 : {score}', font=("", 15 , "bold"))

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0) # 화면이 덜 깜빡이게 하기 위해서 사용... screen.update와 함께 사용됨

# snake 만들기

start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
score = 0

for pos in start_pos:
  create_snake(pos)

# 먹이 만들기

food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

# 점수 표시

score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"점수 : {score}", font=("", 15, "bold"))

screen.listen()
screen.onkeypress(up , "Up")
screen.onkeypress(down , "Down")
screen.onkeypress(left , "Left")
screen.onkeypress(right , "Right")

game_on = True

while game_on:
  screen.update() # 꼬리가 모두 이동한 다음에 화면을 update함
  time.sleep(0.1)
  for i in range(len(snakes) -1, 0, -1):
    snakes[i].goto(snakes[i-1].pos())

  snakes[0].forward(10) # 머리 이동

  # 경계선에 닿으면 게임 Over....
  
  if snakes[0].xcor() > 280 or snakes[0].xcor() <-280 \
      or snakes[0].ycor() > 280 or snakes[0].ycor() <-280:
    game_on = False
    score_pen.goto(0, 0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))
  
  # 자기에 꼬리에 닿으면 game over...

  for body in snakes[1:]:
    if snakes[0].distance(body) < 9:
      game_on = False
      score_pen.goto(0, 0)
      score_pen.write("Game Over", False, "center", ("", 30, "bold"))

  # 먹이를 먹었을 때...

  if snakes[0].distance(food) < 15:

    score_update()

    food.goto(rand_pos())
    create_snake(snakes[-1].pos()) # snake의 마지막 body에 새로 하나 생성

screen.mainloop()