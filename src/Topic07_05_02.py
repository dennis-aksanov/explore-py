import turtle
import random
from threading import Lock
t = turtle.Pen()
# #RRGGBB
t.speed(0)
t.hideturtle()
turtle.bgcolor("magenta")
# mutex_lock = Lock()
number_of_circles = int(turtle.numinput("сколько смайлов",
                                        "сколько смайликов вы хотите? ",
                                        5))


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


    # mutex_lock.release()
for n in range(number_of_circles):
    x = random.randrange(-turtle.window_width() // 2,
                         turtle.window_width() // 2)
    y = random.randrange(-turtle.window_height() // 2,
                         turtle.window_height() // 2)
    t.pendown()
    draw_smiley(x, y)
    t.penup()


turtle.onscreenclick(draw_smiley)
turtle.mainloop()
