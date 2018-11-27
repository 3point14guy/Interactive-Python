# draw consecutively larger squares

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


def bigger(t, n):
    for i in range(5):
        drawSquare(leo, 20 + n * 2)
        n = n + 20
        t.up()
        t.goto(-n, -n)
        t.down()


leo = turtle.Turtle()
leo.color("hotpink")
leo.pensize(3)

n = 0

wn = turtle.Screen()
wn.bgcolor("lightgreen")

bigger(leo, n)

wn.exitonclick()
