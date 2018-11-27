# Extend the star function to draw an n pointed star. (Hint: n must be greater or equal to 3).

import turtle

def multiPointStar(t, n):
    if n >= 5 and (n % 2 == 1):
        for i in range(n):
            t.forward(150)
            t.left(180 + 360/(n * 2))
    elif n > 6 and n % 4 == 0:
        for i in range(n):
            t.forward(150)
            t.left(180 + 360/n)
    else:
        for i in range(n):
            t.forward(150)
            t.left(180 + 360/n * 2)
leo = turtle.Turtle()
leo.speed(0)

wn = turtle.Screen()

multiPointStar(leo, 15)

wn.exitonclick()
