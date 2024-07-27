import turtle
width = 10
wn = turtle.Screen()
# wn.title("Button Counting")
# wn.bgcolor("white")
# wn.setup(width=800, height=800)
# t = turtle.Turtle()
tpen = turtle.Pen()
tpen.width(width)
tpen.pencolor("yellow")
tpen.fillcolor("yellow")
tpen.speed(0)
# tpen.color("black")
# tpen.hideturtle()
# tpen.goto(0, 0)


def fnClick(x, y):
    print("({},{})".format(x, y))
    tpen.setpos(x, y)


wn.onclick(fnClick)
wn.mainloop()
