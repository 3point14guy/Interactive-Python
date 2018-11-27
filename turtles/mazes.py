#create the shapes below. Hint: the only difference is rotation

import turtle

def continuous(t, angle):
    n = 1
    for i in range(80):
        n = n + 2
        t.right(angle)
        t.forward(n)

leo = turtle.Turtle()
leo.color("blue")
leo.speed(0)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

leo.up()
leo.goto(-110,0)
leo.down()
continuous(leo, 90)
leo.up()
leo.goto(110, 0)

leo.down()
continuous(leo, 91)

wn.exitonclick()
