import turtle           # green becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("green becomes a traffic light!")
wn.bgcolor("lightgreen")
green = turtle.Turtle()
yellow = turtle.Turtle()
yellow.hideturtle()
red = turtle.Turtle()
red.hideturtle()
# This variable holds the current state of the machine
state_num = 0

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    green.pensize(3)
    green.color("black", "darkgrey")
    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()

def draw_light(t, distance, color):
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(distance)

    t.shape("circle")
    t.shapesize(3)
    t.fillcolor(color)

def advance_state_machine():
    global state_num
    if state_num == 0:    #this combo required for practice problem
        green.showturtle()
        yellow.showturtle()
        red.hideturtle()
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:
        green.hideturtle()
        yellow.showturtle()
        red.hideturtle()
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:
        green.hideturtle()
        yellow.hideturtle()
        red.showturtle()
        state_num = 3
        wn.ontimer(advance_state_machine, 3000)
    else:
        green.showturtle()
        yellow.hideturtle()
        red.hideturtle()
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

draw_housing()
draw_light(green, 50, "green")
draw_light(yellow, 120, "yellow")
draw_light(red, 190, "red")

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
turtle.mainloop()
