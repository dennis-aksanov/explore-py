import turtle
t = turtle.Pen()
# #RRGGBB
number_of_circles = int(turtle.numinput("количество окружностей",
                                        "сколько окружностей вы хотите? ",
                                        45))
width = 10
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.bgcolor("magenta")

for x in range(3600):
    t.width(width)
    t.pencolor(colors[x%6])
    t.circle(number_of_circles + 10)
    t.left(360/number_of_circles)
    width = width + 0.2
