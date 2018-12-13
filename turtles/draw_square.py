# Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

import turtle

def draw_square(t, length):
    """Get turtle t to draw a square of length side"""
    for i in range(5):
        for i in range(4):
            t.forward(length)
            t.left(90)
        t.penup()
        t.forward(length * 2)
        t.pendown()

def main():
    wn = turtle.Screen()
    wn.bgcolor("blue")

    length = 20

    alex = turtle.Turtle()
    alex.color("yellow")
    alex.pensize(3)

    draw_square(alex,length)

    wn.exitonclick()

if __name__ == "__main__":
    main()
