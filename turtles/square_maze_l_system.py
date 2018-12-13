# hilbert cure == continuous fractal space filling cureve
import turtle

def applyRules(char):
    new_string = ""
    if char == "L":
        new_string = "+RF-LFL-FR+"
    elif char == "R":
        new_string = "-LF+RFR+FL-"
    else:
        new_string = char
    return new_string


def processString(oldStr):
    new_string = ""
    for char in oldStr:
        new_string = new_string + applyRules(char)
    return new_string

def createLSystem(numIter, axiom):
    start_string = axiom
    end_string = ""
    for i in range(numIter):
        end_string = processString(start_string)
        start_string = end_string
    return end_string

def drawSystem(t, instructions, angle, distance):
    for char in instructions:
        if char == "F":
            t.forward(distance)
        elif char == "B":
            t.backward(distance)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)
    inst = createLSystem(4, "L")
    print(inst)

    drawSystem(t, inst, 90, 10)

    wn.exitonclick()

main()
