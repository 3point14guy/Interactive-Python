# import turtle
#
# def tree(branchLen,t, i):
#
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen-15,t, i)
#         t.left(40)
#         tree(branchLen-15,t, i)
#         t.right(20)
#         t.backward(branchLen)
#
#
# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("brown")
#     t.speed(5)
#     tree(75,t, 0)
#     myWin.exitonclick()
#
# main()


import turtle
import random

def branch_width(branchLen, t):
    if branchLen > 60:
        t.width(6)
    elif branchLen > 45:
        t.width(4)
    elif branchLen > 30:
        t.width(3)
    elif branchLen > 15:
        t.width(2)

def draw_leaves(branchLen, t, color, degrees):
    t.fillcolor("green")
    t.color("green")
    # print(t.heading(), "before")
    for i in range(int(360/degrees)):
        if branchLen <= 20:
            radius = random.randrange(15, 25)
            t.left(degrees)
            t.begin_fill()
            t.circle(radius)
            t.end_fill()
            # draw_leaves(branchLen, t, color, degrees)
    # print(t.heading())
    t.color("brown")

def direction():
    coin_flip = random.choice([1, 2])
    if coin_flip == 1:
        return 1
    else:
        return -1

def tree(branchLen, t):
    shorten = random.randrange(10, 20)
    angle = random.randrange(15, 40)
    if branchLen < 15:
        t.color("green")
    if branchLen > 5:
        dir = direction()
        t.forward(branchLen)
        t.right(angle * dir)
        branch_width(branchLen, t)
        tree(branchLen - shorten,t)
        t.left((angle * (2 + random.randrange(1, 3)/15)) * dir)
        draw_leaves(branchLen, t, "green", 60)
        branch_width(branchLen, t)
        tree(branchLen - shorten,t)
        draw_leaves(branchLen, t, "green", 90)
        t.right(angle * dir)
        t.backward(branchLen)

def go():
    t.reset()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.speed(0)
    t.width(8)
    tree(random.randrange(65, 95, 5), t)



turtle.tracer(False)
turtle.hideturtle()
t = turtle.Turtle()

wn = turtle.Screen()
wn.onkey(go, "Up")
wn.listen()
turtle.update()
turtle.mainloop()
