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

cleo = turtle.Turtle()
cleo.color("purple")
cleo.speed(0)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

leo.up()
leo.goto(-110,0)
leo.down()
continuous(leo, 90)

cleo.up()
cleo.goto(110, 0)
cleo.down()
continuous(cleo, 91)

wn.exitonclick()
