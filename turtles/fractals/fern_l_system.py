import turtle

def apply_rules(old_string):
    new_string = ""
    if old_string == "H":
        new_string = "HFX[+H][-H]"
    elif old_string == "X":
        new_string = "X[-FFF][+FFF]FX"
    else:
        new_string = old_string
    return new_string

def process_string(chars):
    new_string = ""
    for char in chars:
        new_string = new_string + apply_rules(char)
    return new_string

def create_L_system(iters, axiom):
    start_string = axiom
    end_string = ""
    for i in range(iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string

def draw_L_system(t, inst, angle, distance):
    position_list = []
    for char in inst:
        if char == "F":
            t.forward(distance)
        if char == "B":
            t.backwards(distance)
        if char == "+":
            t.right(angle)
        if char == "-":
            t.left(angle)
        if char == "[":
            position_list.append([t.heading(), t.xcor(), t.ycor()])
        if char == "]":
            go = position_list.pop()
            t.setheading(go[0])
            t.setposition(go[1], go[2])


def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)
    # inst = create_L_system(5, "H")

    t.up()
    t.goto(-200,0)
    t.down()
    # written as callback
    draw_L_system(t, create_L_system(5, "H"), 25.7, 7)


    wn.exitonclick()

main()
