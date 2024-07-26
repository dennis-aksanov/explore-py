import turtle
import random
t = turtle.Pen()
# #RRGGBB
t.speed(10)
turtle.bgcolor("magenta")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def random_spiral():
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    width = random.randint(1, 7)
    x = random.randrange(-turtle.window_width() // 2,
                         turtle.window_width() // 2)
    y = random.randrange(-turtle.window_height() // 2,
                         turtle.window_height() // 2)
    t.penup()
    t.setpos(x, y)
    t.width(width)
    t.pendown()
    for m in range(size):
       t.forward(m*2)
       t.left(93)
for n in range(360):
    random_spiral()