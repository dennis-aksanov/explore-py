import turtle
width = 10
wn = turtle.Screen()
tpen = turtle.Pen()
tpen.width(width)
tpen.pencolor("yellow")
tpen.fillcolor("yellow")
tpen.speed(0)
tpen.turtlesize(2, 2, 2)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray"]
# number_of_circles = int(turtle.numinput("сколько смайлов",
#                                         "сколько смайликов вы хотите? ",
#                                         5))a
angle = 90


def changeAngle():
    global angle
    angle = 45
    # angle = int(turtle.numinput("какой угол поворота","какой угл поворота вы хотите? ",90))




def setColorRed():
    tpen.pencolor("red")
    tpen.fillcolor("red")


def setColorYellow():
    tpen.pencolor("yellow")
    tpen.fillcolor("yellow")


def setColorGreen():
    tpen.pencolor("green")
    tpen.fillcolor("green")


def setColorBlue():
    tpen.pencolor("blue")
    tpen.fillcolor("blue")


def setColorPurple():
    tpen.pencolor("purple")
    tpen.fillcolor("purple")


def forward():
    tpen.forward(50)


def left():
    global angle
    tpen.left(angle)


def right():
    global angle
    tpen.right(angle)


def backward():
    tpen.backward(50)


turtle.onkeyrelease(forward, "Up")
turtle.onkeyrelease(left, "Left")
turtle.onkeyrelease(right, "Right")
turtle.onkeyrelease(backward, "Down")
turtle.onkeyrelease(setColorRed, "1")
turtle.onkeyrelease(setColorYellow, "2")
turtle.onkeyrelease(setColorGreen, "3")
turtle.onkeyrelease(setColorBlue, "4")
turtle.onkeyrelease(setColorPurple, "5")
turtle.onkeyrelease(changeAngle, " ")
turtle.listen()
turtle.mainloop()


