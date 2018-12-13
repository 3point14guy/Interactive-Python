import turtle
import string
alphabet = string.ascii_uppercase

def make_table(turtle, rows, cols):
    for row in range(rows):
        for col in range(cols):
            turtle.down()
            turtle.write("{}{}".format(alphabet[row], col), font = ("Arial", 20, "normal"))
            turtle.up()
            turtle.forward(40)

        turtle.goto(-300, 270 - 30 * row)

def main():
    leo = turtle.Turtle()
    canvas = turtle.Screen()
    leo.speed(1)
    leo.up()
    leo.goto(-300, 300)
    make_table(leo, 5, 5)
    canvas.exitonclick()

main()
