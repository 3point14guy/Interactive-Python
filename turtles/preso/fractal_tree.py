import turtle

def tree(branch_length, t):
    # base case
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        # recursively call drawing right side branches
        # changing state (branch_length - 15)
        tree(branch_length-15, t)
        t.left(40)
        # recursively call drawing left side branches
        tree(branch_length-15, t)
        t.right(20)
        t.backward(branch_length)


def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.pensize(3)
    t.speed(5)
    tree(75, t)
    wn.exitonclick()

main()
