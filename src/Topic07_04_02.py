import turtle
import random

t = turtle.Pen()
# #RRGGBB
t.speed(0)
t.hideturtle()
turtle.bgcolor("magenta")
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]


def draw_smiley(x, y):
    # mutex_lock.acquire()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.setpos(x-15, y+60)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(x+15, y+60)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(x - 25, y + 40)
    t.pendown()
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
    t.penup()


def draw_kaleido(x, y):
    # t.pencolor(random.choice(colors))
    # size = random.randint(10, 40)
    draw_smiley(x, y)
    draw_smiley(-x, y)
    draw_smiley(x, -y)
    draw_smiley(-x, -y)


def draw_spiral(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()



turtle.onscreenclick(draw_kaleido)
turtle.mainloop()