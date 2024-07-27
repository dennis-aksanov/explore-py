import turtle
tpen = turtle.Pen()


def left():
    tpen.left(90)


def right():
    tpen.right(90)


turtle.onkeyrelease(left, "Left")
turtle.onkeyrelease(right, "Right")
turtle.mainloop()