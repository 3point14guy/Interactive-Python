import turtle

def create_L_system(num_iters,axiom):
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string

    return end_string

def process_string(old_str):
    new_str = ""
    for ch in old_str:
        new_str = new_str + apply_rules(ch)

    return new_str

def apply_rules(ch):
    new_str = ""
    if ch == 'F':
        new_str = 'F-F++F-F'   # Rule 1 Kock Curve
        # new_str = 'F+F--F+F'   # Rule 1 Kock Snowflake
    else:
        new_str = ch    # no rules apply so keep the character

    return new_str

def draw_L_system(aTurtle, instructions, angle, distance):
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
    inst = create_L_system(4, "F")   # create the string for the curve
    # inst = create_L_system(3, "+F--F--F")   # create the string for the snowflake
    t = turtle.Turtle()  # create a turtle object
    # setting tracer to false will just generate final picture
    # turtle.tracer(False)
    # creates an environment for the turtle to "live"
    wn = turtle.Screen()


    t.up()
    t.back(200)
    t.down()
    t.speed(0)
    draw_L_system(t, inst, 60, 5)      # draw the picture
                                # angle 60, segment length 5
    # turtle.update()
    wn.exitonclick()

main()
