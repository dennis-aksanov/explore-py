import turtle
import random
t = turtle.Pen()
# #RRGGBB
t.speed(10)
turtle.bgcolor("magenta")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for n in range(360):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    width = random.randint(6, 20)
    x = random.randrange(-turtle.window_width() // 2,
                         turtle.window_width() // 2)
    y = random.randrange(-turtle.window_height() // 2,
                         turtle.window_height() // 2)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.width(width)
    t.circle(size)


