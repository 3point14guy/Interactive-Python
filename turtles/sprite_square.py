# Write a function called drawSprite that will draw a sprite. The function will need parameters for the turtle, the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.

# Write a function called fancySquare that will draw a square with a sprite at each of it's corners


import turtle

def draw_sprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        t.stamp()
        t.forward(-length)
        t.right(360/legs)

def fancy_square(t, legs, sprite_length):
    for i in range(4):
        t.width(3)
        t.forward(150)
        t.left(90)
        t.width(1)
        draw_sprite(t, legs, sprite_length)


leo = turtle.Turtle()
leo.speed(8)
#leo.shape("circle")
wn = turtle.Screen()

fancy_square(leo, 10, 25)

wn.exitonclick()
