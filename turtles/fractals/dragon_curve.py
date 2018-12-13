import turtle

def applyRules(left_side_char):
    right_side_char = ""
    if left_side_char == "X":
        right_side_char = "X+YF+"
    elif left_side_char == "Y":
        right_side_char = "-FX-Y"
    else:
        right_side_char = left_side_char
    return right_side_char


def processString(old_string):
    new_string = ""
    for character in old_string:
        new_string = new_string + applyRules(character)
    return new_string

def createLSystem(num_iterations, axiom):
    start_string = axiom
    end_string = ""
    for i in range(num_iterations):
        end_string = processString(start_string)
        start_string = end_string
    return end_string


def drawLSystem(turtle, instructions, angle, distance):
    saved_state_list = []
    for character in instructions:
        if character == 'F':
            turtle.forward(distance)
        elif character == 'B':
            turtle.backwards(distance)
        elif character == '+':
            turtle.right(angle)
        elif character == '-':
            turtle.left(angle)
    


def main():
    t = turtle.Turtle()
    t.speed(0)
    t.fillcolor("purple")
    wn = turtle.Screen()

    # unable to color fill here
    # t.begin_fill()
    instructions = createLSystem(12, "FX")
    # t.end_fill()


    drawLSystem(t, instructions, 90, 2)
    wn.exitonclick()

main()
