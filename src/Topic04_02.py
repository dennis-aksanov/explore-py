import turtle
t = turtle.Pen()
# #RRGGBB
t.penup()
t.speed(21)
width = 0.1
turtle.bgcolor("magenta")

number_of_circles = int(turtle.numinput("количество окружностей",
                                        "сколько окружностей вы хотите? ",
                                        5))
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray"]
for m in range(3600):
    t.forward(m * 3)
    position = t.position()
    heading = t.heading()
    for n in range(number_of_circles):
        t.width(width)
        t.pendown()
        t.pencolor(colors[n%7])
        t.circle(m * 0.21)
        t.right(360/number_of_circles -2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/number_of_circles + 2)
    width = width + 0.018