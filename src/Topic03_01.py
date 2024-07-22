import turtle
t = turtle.Pen()
# #RRGGBB
t.speed(10)
t.width(7)
turtle.bgcolor("magenta")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
sides = int(turtle.numinput("ведите от 1 до 27 сторон:", 27, 4, 1))
for x in range(3600):
    t.pencolor(colors[x%6])
    t.forward(x * 3/sides + x)
    t.right(360/sides + 1)
