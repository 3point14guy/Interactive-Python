import turtle           # t becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("t becomes a traffic light!")
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.tracer(False)
t.hideturtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    t.pensize(3)
    t.color("black", "darkgrey")
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()

def move(t):
    t.up()
    t.forward(70)
    t.down()

def back(t):
    t.up()
    t.back(140)
    t.down()

def draw_circle(t, fill_color):
    t.color("black", fill_color)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def light_change(t, color_list):
    """draw 3 lights"""
    draw_circle(t, color_list[0])
    for i in range(2):
        move(t)
        draw_circle(t, color_list[i + 1])

def folded_comments():
# A traffic light is a kind of state machine with three states,
# Green, Yellow, Red.  We number these states  0, 1, 2
# When the machine changes state, we change t' position and
# her fillcolor.

# This variable holds the current state of the machine
# state_num = 0
#
#
# def advance_state_machine():
#     global state_num
#     if state_num == 0:       # Transition from state 0 to state 1
#         t.forward(70)
#         t.fillcolor("yellow")
#         state_num = 1
#     elif state_num == 1:     # Transition from state 1 to state 2
#         t.forward(70)
#         t.fillcolor("red")
#         state_num = 2
#     else:                    # Transition from state 2 to state 0
#         back(t)
#         t.fillcolor("green")
#         state_num = 0
#
# # Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")
    print("")

def green():
    back(t)
    light_change(t, ["green", "gray", "gray"])
    wn.ontimer(green_yellow, 5000)

# requirement for practice problem
def green_yellow():
    back(t)
    light_change(t, ["green", "yellow", "gray"])
    wn.ontimer(yellow, 1000)

def yellow():
    back(t)
    light_change(t, ["gray", "yellow", "gray"])
    wn.ontimer(red, 1000)

def red():
    back(t)
    light_change(t, ["gray", "gray", "red"])
    wn.ontimer(green, 5000)

draw_housing()

# move to the initial position to draw lights
t.penup()
t.forward(70)
t.left(90)
t.forward(50)
t.down()

light_change(t, ["green", "gray", "gray"])

wn.onkey(green_yellow, "space")
wn.listen()
wn.update()
turtle.mainloop()
