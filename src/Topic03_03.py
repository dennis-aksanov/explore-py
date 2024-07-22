import turtle
t = turtle.Pen()
# #RRGGBB
t.speed(10)

turtle.bgcolor("magenta")
sides = eval(input("ведите от 2 до скольки угодно сторон:"))
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range(3600):
    t.pencolor(colors[x%6])
    t.forward(x * 3/sides + x)
    t.right(360/sides + 35)
    t.width(x * sides/100)
