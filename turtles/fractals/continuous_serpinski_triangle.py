import turtle

def apply_rules(l_side):
    r_side = ""
    if l_side == "X":
        r_side = "YF+XF+Y"
    elif l_side == "Y":
        r_side = "XF-YF-X"
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
    wn = turtle.Screen()
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    for i in range(3, 8):
        t.penup()
        x = -400 + (2 * (i**3))
        t.goto(x, 0)
        t.pendown()
        inst = create_L_system(i, "YF")
        draw_L_system(t, inst, 60, 3)


    wn.exitonclick()

main()
