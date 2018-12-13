import turtle

def apply_rules(l_side):
    r_side = ""
    if l_side == "F":
        r_side = "FF"
    elif l_side == "X":
        r_side = "--FXF++FXF++FXF--"
    else:
        r_side = l_side
    return r_side

def process_str(old_str):
    new_str = ""
    for char in old_str:
        new_str = new_str + apply_rules(char)
    return new_str

def create_L_system(iters, axiom):
    start_str = axiom
    end_str = ""
    for i in range(iters):
        end_str = process_str(start_str)
        start_str = end_str
    return end_str

def draw_L_system(t, inst, angle, distance):
    for char in inst:
        if char == "F":
            t.forward(distance)
        elif char == "B":
            t.backwards(distance)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.fillcolor("blue")
    wn = turtle.Screen()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    inst = create_L_system(5, "FXF--FF--FF")
    t.begin_fill()
    draw_L_system(t, inst, 60, 5)
    t.end_fill()


    wn.exitonclick()

main()
