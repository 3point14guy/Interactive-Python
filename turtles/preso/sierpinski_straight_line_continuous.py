import turtle
# import time

def apply_rules(l_side):
    r_side = ""
    if l_side == "F":
        r_side = "FF"
    elif l_side == "X":
        r_side = "--FXF++FXF++FXF--"
        # # use to show affects of modifying rules
        # r_side = "W--FXF++FXF++FXF--"
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
        print(start_str)
        print("\n")
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
        # # use if customizing rules to include "W"
        # elif char == "W":
        #     t.color("red")
        #     t.stamp()
        #     t.color("black")

def main():

    t = turtle.Turtle()
    t.speed(1)
    t.fillcolor("blue")
    wn = turtle.Screen()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    # t.tracer(9)
    inst = create_L_system(4, "FXF--FF--FF")
    t.begin_fill()
    draw_L_system(t, inst, 60, 8)
    t.end_fill()


    wn.exitonclick()
    # turtle.update()
    # turtle.mainloop()
main()
