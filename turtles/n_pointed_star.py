# Extend the star function to draw an n pointed star. (Hint: n must be greater or equal to 3).

import turtle

def multi_point_star(t, n):
    if n == 5 and (n % 2 == 1):
        for i in range(n):
            t.forward(250)
            t.left(180 + 360/(n * 2))
    elif n > 6 and n % 4 == 0:
        t.fillcolor("red")
        t.begin_fill()
        for i in range(n):
            t.forward(250)
            t.left(180 + 360/n)
        t.end_fill()
    else:
        t.fillcolor("green")
        t.begin_fill()
        for i in range(n):
            t.forward(250)
            t.left(180 + 360/n * 2)
        t.end_fill()
leo = turtle.Turtle()
leo.speed(0)
leo.color("blue")
wn = turtle.Screen()
wn.bgcolor("yellow")
leo.goto(-125, 0)
multi_point_star(leo, 5)

wn.exitonclick()
