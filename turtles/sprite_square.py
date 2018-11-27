# Write a function called drawSprite that will draw a sprite. The function will need parameters for the turtle, the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.

# Write a function called fancySquare that will draw a square with a sprite at each of it's corners


import turtle

def drawSprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        t.stamp()
        t.forward(-length)
        t.right(360/legs)

def fancySquare(t, legs, length):
    for i in range(4):
        t.forward(150)
        t.left(90)
        drawSprite(t, legs, length)


leo = turtle.Turtle()
leo.speed(8)
wn = turtle.Screen()

fancySquare(leo, 10, 15)

wn.exitonclick()
