import turtle as t
import random

def draw_stars():
  t.color(random.choice(color))
  t.begin_fill()
  star_size = random.randint(5, 15)
  for i in range(5):
    t.forward(star_size)
    t.left(72)
    t.forward(star_size)
    t.right(144)
  t.end_fill()

color = ("red", "orange", "blue", "green", "white", "yellow", "indigo", "pink")

t.bgcolor("black")
t.speed(0)

for x in range(20):
  t.up()
  t.goto(random.randint(-300, 300), random.randint(-300, 300))
  t.down

  # t.dot(5, random.choice(color))

  # 별 그리기
  draw_stars()

t.mainloop()