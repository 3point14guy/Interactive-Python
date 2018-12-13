import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        # newstr = 'F-F++F-F'   # Rule 1 Kock Curve
        newstr = 'F+F--F+F'   # Rule 1 Kock Snowflake
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

#
def main():
    # inst = createLSystem(4, "F")   # create the string for the curve
    inst = createLSystem(3, "+F--F--F")   # create the string for the snowflake
    t = turtle.Turtle()  # create a turtle object
    # setting tracer to false will just generate final picture
    # t.tracer(False)
    # creates an environment for the turtle to "live"
    wn = turtle.Screen()


    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 4)      # draw the picture
                                    # angle 60, segment length 5
    turtle.update()
    wn.exitonclick()

main()
