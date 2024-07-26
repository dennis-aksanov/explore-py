import turtle
import random

t = turtle.Pen()
# #RRGGBB
t.speed(0)
turtle.bgcolor("magenta")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]


def draw_kaleido(x, y):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    draw_spiral(x, y, size)
    draw_spiral(-x, y, size)
    draw_spiral(x, -y, size)
    draw_spiral(-x, -y, size)


def draw_spiral(x, y, size):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for m in range(size):
       t.forward(m*2)
       t.left(92)


turtle.onscreenclick(draw_kaleido)
turtle.mainloop()