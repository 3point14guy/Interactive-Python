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
    # t.tracer(False)
    # t.fillcolor("lightblue")
    # t.begin_fill()
    for char in instructions:
        if char == "F":
            t.forward(distance)
        elif char == "B":
            t.backward(distance)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
    # t.end_fill()

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.width(3)
    t.speed(0)
    t.up()
    t.goto(-350, 350)
    t.down()

    inst = createLSystem(8, "L")
    # print(inst)

    drawSystem(t, inst, 90, 5)

    wn.exitonclick()
    # turtle.update()
    # turtle.mainloop()
main()
