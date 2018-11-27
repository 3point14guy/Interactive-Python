# Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    t.up()
    t.goto(-130, 0)
    t.down()
    for i in range(5):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        t.up()
        t.forward(sz * 2)
        t.down()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

sz = 20
border = 40

alex = turtle.Turtle()
alex.color("pink")
alex.pensize(3)

drawSquare(alex,sz)

wn.exitonclick()
