# Colorful 3d screensaver using simple python code in python


import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for i in range(400):
    t.pencolor(colors[i%6])

    t.width(i/100 +1)
    t.forward(i)
    t.left(58)

turtle.done()







