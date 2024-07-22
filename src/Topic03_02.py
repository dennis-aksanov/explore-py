import turtle
t = turtle.Pen()
# #RRGGBB

turtle.bgcolor("magenta")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
your_name = turtle.textinput("ведите своё имя:",
    "как тебя зовут")
for x in range(360):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x * 4)
    t.write(your_name, font = ("Arial", int((x + 4) / 4), "bold"))
    t.left(92)

