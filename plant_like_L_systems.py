import turtle

def apply_rules(old_str):
    new_str = ""
    for char in old_str:
        if char == "F":
            new_str = "F[-F]F[+F]F"
        # if char == "H":
        #     new_str = "HFX[+H][-H]"
        # elif char == "X":
        #     new_str == "X[-FFF][+FFF]FX"
        else:
            new_str = old_str
        return new_str

def process_str(chars):
    new_str = ""
    for char in chars:
        new_str = new_str + apply_rules(char)
    return new_str

def create_L_sys(iters, axiom):
    start_str = axiom
    end_str = ""
    for i in range(iters):
        end_str = process_str(start_str)
        start_str = end_str
    return end_str

def draw_L_sys(t, inst, angle, distance):
    last_positions = []
    for char in inst:
        if char == "F":
            t.forward(distance)
        elif char == "B":
            t.backwards(distance)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            last_positions.append([t.heading(), t.xcor(), t.ycor()])
        elif char == "]":
            old_spot = last_positions.pop()
            # t.up()
            t.goto(old_spot[1], old_spot[2])
            t.setheading(old_spot[0])
            # t.down()

t = turtle.Turtle()
t.tracer(False)
t.up()
t.goto(-200, 0)
t.down()
wn = turtle.Screen()
inst = create_L_sys(7, "F")

draw_L_sys(t, inst, 25, 3)

wn.update()
wn.exitonclick()
