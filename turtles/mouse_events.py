import turtle

tess = turtle.Turtle()             # Create two turtles
tess.color("purple")
alex = turtle.Turtle()
alex.color("blue")
alex.forward(100)

wn = turtle.Screen()

def red():
    tess.color("red")

def increase_width():
    width = tess.pensize()
    tess.width(width + 1)

def decrease_width():
    width = tess.pensize()
    tess.width(width - 1)



def h_tess(x, y):
    wn.title("Tess coordinates are {}, {}".format(x, y))
    tess.left(43)
    tess.forward(30)

def h_alex():
    for i in range(10):
        alex.right(80)
        alex.forward(45)

wn.onkey(red, "r")
wn.onkey(increase_width, "plus")
wn.onkey(decrease_width, "minus")

tess.onclick(h_tess)
wn.ontimer(h_alex, 2000)
wn.listen()
turtle.mainloop()
