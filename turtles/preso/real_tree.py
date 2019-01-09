import turtle
import random

def branch_width(branch_length, t):
    """Decrease branch width with decrease in length."""
    if branch_length > 60:
        t.width(6)
    elif branch_length > 45:
        t.width(4)
    elif branch_length > 30:
        t.width(3)
    elif branch_length > 15:
        t.width(2)

def draw_leaves(branch_length, t, color, degrees):
    """Make a 'florette' of leaves at the branch tip."""
    t.fillcolor("green")
    t.color("green")
    # draw leaves all around branch tip"
    for i in range(int(360/degrees)):
        if branch_length <= 20:
            radius = random.randrange(15, 25)
            t.left(degrees)
            t.begin_fill()
            t.circle(radius)
            t.end_fill()
    t.color("brown")

def rand_direction():
    coin_flip = random.choice([1, 2])
    if coin_flip == 1:
        return 1
    else:
        return -1

def tree(branch_length, t):
    """'draw' a 'life-like' tree"""
    # returns an int between 10 - 19
    shorten = random.randrange(10, 20)
    # returns an int between 15 - 39
    angle = random.randrange(15, 40)
    if branch_length < 15:
        t.color("green")
    if branch_length > 5:
        dir = rand_direction()
        t.forward(branch_length)
        # t.right to a negative angle is the same as t.left
        t.right(angle * dir)
        branch_width(branch_length, t)
        new_branch_length = branch_length - shorten

        tree(new_branch_length, t)
        t.left((angle * (2 + random.randrange(1, 3)/15)) * dir)
        draw_leaves(branch_length, t, "green", 60)
        branch_width(branch_length, t)
        new_branch_length = branch_length - shorten

        tree(new_branch_length,t)
        draw_leaves(branch_length, t, "green", 90)
        t.right(angle * dir)
        t.backward(branch_length)

def go():
    """'draw' a new random tree"""
    t.reset()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.speed(0)
    t.width(8)
    branch_length = random.randrange(65, 95, 5)
    tree(branch_length, t)



turtle.tracer(False)
turtle.hideturtle()
t = turtle.Turtle()

wn = turtle.Screen()
wn.onkey(go, "Up")
wn.listen()
turtle.update()
turtle.mainloop()
