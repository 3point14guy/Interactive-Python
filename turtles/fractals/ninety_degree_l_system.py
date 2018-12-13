# # Hilbert Curve

import turtle

def createLSystem(numIters, axiom):
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
    if ch == 'L':
        newstr = '+RF-LFL-FR+'   # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'
    else:
        newstr = ch     # no rules apply so keep the character

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

def main():
    inst = createLSystem(4, "L")  # create the string
    print(inst)
    t = turtle.Turtle()
    l = turtle.Turtle()
    t.color("red")           # create the turtle
    wn = turtle.Screen()

    t.up()
    l.up()
    t.goto(-350, 200)
    l.goto(-346, 196)
    t.down()
    l.down()
    t.speed(0)
    l.speed(0)
    drawLsystem(t, inst, 90, 7)   # draw the picture
    drawLsystem(l, inst, 90, 7)   # draw the picture
                                  # angle 90, segment length 5
    wn.exitonclick()

main()


# # dragon curve, continuous, self-avoiding
#
# import turtle
#
# def turn(i):
#     left = (((i & -i) << 1) & i) != 0
#     return 'L' if left else 'R'
#
# def curve(iteration):
#     return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])
#
# if __name__ == '__main__':
#     turtle.showturtle()
#     turtle.hideturtle()
#     turtle.speed(0)
#     i = 1
#     while True:
#         if turn(i) == 'L':
#             turtle.circle(-4, 90, 36)
#         else:
#             turtle.circle(4, 90, 36)
#         i += 1



# # Fractal Squares
#
# from turtle import *
# delay(0)
# speed(4)
#
# def square(length, level):
#     if level == 0:
#         return
#     else:
#         # Start from the bottom-left corner
#         forward(length)
#         # Right square
#         square(length // 2, level - 1)
#         lt(90)
#
#         for i in range(3):
#             forward(length)
#             lt(90)
#         #
#         # forward(length)
#         # lt(90)
#         # #
#         # forward(length)
#         # lt(90)
#
#         ### Try moving backward before drawing
#         backward(length // 2)
#
#         # Left square
#         square(length // 2, level - 1)
#
#         forward(length // 2)
#
# square(110, 5)
#
# exitonclick()



# # Koch curve

# import turtle
#
# def createLSystem(numIters,axiom):
#     startString = axiom
#     endString = ""
#     for i in range(numIters):
#         endString = processString(startString)
#         startString = endString
#
#     return endString
#
# def processString(oldStr):
#     newstr = ""
#     for ch in oldStr:
#         newstr = newstr + applyRules(ch)
#
#     return newstr
#
# def applyRules(ch):
#     newstr = ""
#     if ch == 'F':
#         newstr = 'F+F--F+F'   # Rule 1
#     else:
#         newstr = ch    # no rules apply so keep the character
#
#     return newstr
#
# def drawLsystem(aTurtle, instructions, angle, distance):
#     aTurtle.begin_fill()
#     for cmd in instructions:
#         if cmd == 'F':
#             aTurtle.forward(distance)
#         elif cmd == 'B':
#             aTurtle.backward(distance)
#         elif cmd == '+':
#             aTurtle.right(angle)
#         elif cmd == '-':
#             aTurtle.left(angle)
#     aTurtle.end_fill()
#
# def main():
#     inst = createLSystem(4, "F")   # create the string
#     print(inst)
#     t = turtle.Turtle()
#     t.fillcolor('blue')          # create the turtle
#     wn = turtle.Screen()
#
#
#     t.up()
#     t.back(300)
#     t.right(90)
#     t.back(300)
#     t.left(45)
#     t.down()
#     t.speed(0)
#     drawLsystem(t, inst, 60, 10)   # draw the picture
#                                   # angle 60, segment length 5
#     wn.exitonclick()
#
# main()


# # Seaweed

# import turtle
#
# def createLSystem(numIters, axiom):
#     startString = axiom
#     endString = ""
#     for i in range(numIters):
#         endString = processString(startString)
#         startString = endString
#
#     return endString
#
# def processString(oldStr):
#     newstr = ""
#     for ch in oldStr:
#         newstr = newstr + applyRules(ch)
#
#     return newstr
#
# def applyRules(ch):
#     newstr = ""
#     if ch == 'F':
#         newstr = 'F[-F]F[+F]F'   # Rule 1
#     elif ch == 'X':
#         newstr = 'X[-FFF][+FFF]FX'
#     else:
#         newstr = ch     # no rules apply so keep the character
#
#     return newstr
#
# def drawLsystem(aTurtle, instructions, angle, distance):
#     savedInfoList = []
#     for cmd in instructions:
#         if cmd == 'F':
#             aTurtle.forward(distance)
#         elif cmd == 'B':
#             aTurtle.backward(distance)
#         elif cmd == '+':
#             aTurtle.right(angle)
#         elif cmd == '-':
#             aTurtle.left(angle)
#         elif cmd == '[':
#             savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
#             #print(savedInfoList)
#         elif cmd == ']':
#             newInfo = savedInfoList.pop()
#             aTurtle.setheading(newInfo[0])
#             aTurtle.setposition(newInfo[1], newInfo[2])
#
#
# def main():
#     inst = createLSystem(4, "F")   # create the string
#     print(inst)
#     t = turtle.Turtle()            # create the turtle
#     wn = turtle.Screen()
#     t.up()
#     t.back(200)
#     t.down()
#     t.speed(9)
#     drawLsystem(t, inst, 25, 5)  # draw the picture
#
#     wn.exitonclick()
#
# main()
