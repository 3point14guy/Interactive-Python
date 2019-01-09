#get the code from the turtles module
import turtle

# create a canvas object
wn = turtle.Screen()
wn.bgcolor("blue")

# create a turtle object
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("yellow")
alex.pensize(3)

# call methods on the turtle object
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)

# window stays open until clicked on
wn.exitonclick()
