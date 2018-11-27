#approximate pi by graphing a random distribution of points within a circle of radius 1 unit inside a square with sides equal to 2 units

import turtle
import math
import random

def posNeg():
    value = random.random()
    if value <= 0.5:
        modifier = -1
    else:
        modifier = 1
    return modifier

def makeDot(t, x, y):
    t.color(setColor(getDistance(t, x, y)))
    t.goto(x, y)
    t.dot()

def getDistance(t, x, y):
    t.home()
    distance = t.distance(x, y)
    return distance

def setColor(distance):
    if distance <= 1:
        color = "red"
    else:
        color = "blue"
    return color

def getCount(distance):
    if distance <= 1:
        count = count + 1
    else:
        count = count
    return count

def pi(t, x, y):
    ans = 4 * (getCount(getDistance(t, x, y)) / numdarts)
    return ans

fred = turtle.Turtle()
fred.speed(0)
wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

fred.up()

count = 0
numdarts = 1000
for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x = randx * posNeg()
    y = randy * posNeg()

    makeDot(fred, x, y)

print(pi)

wn.exitonclick()
