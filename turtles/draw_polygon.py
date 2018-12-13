# draw a polygon

import turtle

def draw_poly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()
wn.bgcolor("purple")

tess = turtle.Turtle()
tess.color('orange')
tess.pensize(3)

draw_poly(tess, 8, 50)

wn.exitonclick()
