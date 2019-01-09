import turtle

i = 1
t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")

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

def go():
    global i
    main(i)
    i += 1

def color_picker(i):
    colors = ["orange", "purple", "yellow", "red", "green", "blue"]
    color = ""
    for j, col in enumerate(colors):
        if i == j + 1:
            color = col
    return color

# show generations stepwise
# def main(i):
#     turtle.tracer(False)
#     t.speed(0)
#     t.width(2)
#     t.hideturtle()
#     t.penup()
#     t.goto(200, 200)
#     t.pendown()
#     inst = create_L_system(i, "FX")
#     t.color(color_picker(i))
#     draw_L_system(t, inst, 60, 5)
#     t.penup()
#     t.goto(200, 200)
#     t.pendown()
#     inst = create_L_system(i-1, "FX")
#     t.color(color_picker(i-1))
#     draw_L_system(t, inst, 60, 5)
#     wn.update()
#     print(inst)
#
# wn.onkey(go, "space")
# wn.listen()


# draw out 3 generations
def main():
    wn = turtle.Screen()
    wn.bgcolor("yellow")
    # t = turtle.Turtle()
    t.speed(0)
    t.width(3)
    t.hideturtle()
    t.penup()
    t.goto(0, 200)
    t.pendown()
    inst = create_L_system(3, "FX")
    draw_L_system(t, inst, 60, 10)
    wn.exitonclick()

main()
wn.exitonclick()
