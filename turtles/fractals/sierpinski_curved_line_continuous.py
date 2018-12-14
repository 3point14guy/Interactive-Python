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
def write(i):
    t.pendown()
    t.write(i, font=("Arial", 16, "bold"))
    t.penup()

def make3():
    t.setheading(0)
    t.penup()
    t.goto(-300, -25)
    write(3)
    t.goto(-280, 0)
    t.pendown()
    t.left(120)
    inst = create_L_system(3, "YF")
    draw_L_system(t, inst, 60, 5)
    turtle.update()

def make4():
    t.setheading(0)
    t.penup()
    t.goto(-225, -25)
    write(4)
    t.goto(-180, 0)
    t.left(180)
    t.pendown()
    inst = create_L_system(4, "YF")
    draw_L_system(t, inst, 60, 5)
    turtle.update()

def make5():
    t.setheading(0)
    t.penup()
    t.goto(-90, -25)
    write(5)
    t.goto(0, 0)
    t.pendown()
    t.left(120)
    inst = create_L_system(5, "YF")
    draw_L_system(t, inst, 60, 5)
    turtle.update()

def make6():
    t.setheading(0)
    t.penup()
    t.goto(180, -25)
    write(6)
    t.goto(330, 0)
    t.pendown()
    t.left(180)
    inst = create_L_system(6, "YF")
    draw_L_system(t, inst, 60, 5)
    turtle.update()

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
turtle.tracer(False)
t.speed(0)
t.penup()
t.width(3)


wn.onkey(make3, "Up")
wn.onkey(make4, "Down")
wn.onkey(make5, "Right")
wn.onkey(make6, "Left")

# wn.exitonclick()
wn.listen()
turtle.update()
turtle.mainloop()
