import turtle
import time

def drawTriangle(points,myTurtle):
    # myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    #myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    #myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    # time.sleep(3)
    drawTriangle(points,myTurtle)
    if degree > 0:

        #myTurtle.fillcolor("red")
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

        #myTurtle.fillcolor("blue")
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)

        #myTurtle.fillcolor("yellow")
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

        # myTurtle.color("green")


def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myTurtle.shape("turtle")
   myTurtle.speed(2)
   myTurtle.fillcolor("white")
   myPoints = [[-200,-100],[0,200],[200,-100]]
   sierpinski(myPoints,4,myTurtle)
   myWin.exitonclick()

main()
