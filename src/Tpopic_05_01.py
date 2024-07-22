import turtle
t = turtle.Pen()
# #RRGGBB
sides = int(turtle.numinput("Количиство сторон",
                            "сколько сторон будет у вашей спирали? ",
                            5))
t.speed(21)
width = 0.1
turtle.bgcolor("magenta")


colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray"]
for m in range(3600):
    t.pencolor(colors[m % 7])
    t.left(360 /sides + 5)
    t.width(width)
    t.penup()
    t.forward(m * 3)
    t.pendown()
    if (m % 2 ==0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360 / sides)
            width = width + 0.018
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360 / sides)
            width = width + 0.018

