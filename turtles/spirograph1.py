# draw the pattern of repeating squares shown below

import turtle

def draw_poly(t, num_sides, side_length):
    for i in range(20):
        for i in range(num_sides):
            t.forward(side_length)
            t.left(360/num_sides)
        t.left(360/20)

def draw_square(t, length):
    for i in range(20):
        for i in range(4):
            t.forward(length)
            t.left(90)
        t.left(360/20)

leo = turtle.Turtle()
leo.color("blue")
leo.pensize(3)
leo.speed(0)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

draw_poly(leo, 6, 100)

wn.exitonclick()
