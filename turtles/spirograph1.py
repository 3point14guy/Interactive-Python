# draw the pattern of repeating squares shown below

import turtle

def drawSquare(t, sz):
    for i in range(20):

        for i in range(4):
            t.forward(sz)
            t.left(90)
        t.left(360/20)

leo = turtle.Turtle()
leo.color("blue")
leo.pensize(3)
leo.speed(0)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

drawSquare(leo, 100)

wn.exitonclick()
