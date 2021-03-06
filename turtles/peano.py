import turtle

def apply_rules(l_side):
    r_side = ""
    if l_side == "X":
        r_side = "X+YF++YF-FX--FXFX-YF+"
    elif l_side == "Y":
        r_side = "-FX+YFYF++YF+FX--FX-Y"
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
    for j in range(iters):
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
    wn = turtle.Screen()
    t.speed(0)
    t.width(3)
    t.hideturtle()
    t.penup()
    t.goto(0, 200)
    t.pendown()
    inst = create_L_system(3, "FX")
    draw_L_system(t, inst, 60, 10)
    wn.exitonclick()

if __name__ == "__main__":
    main()
