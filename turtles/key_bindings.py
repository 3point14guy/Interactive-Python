import turtle
import draw_polygon

i = 0
t = turtle.Turtle()
wn = turtle.Screen()
# these will be user inputs
length = 25
x = -320
y = 280

def find_object_dimensions(vertecies):
    global x, y
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for j, coor in enumerate(vertecies):
        if j ==0:
            max_x = coor[0]
            max_y = coor[1]
            min_x = (coor[0])
            min_y = (coor[1])
        else:
            if (coor[0]) > (max_x):
                max_x = coor[0]
            if (coor[1]) > (max_y):
                max_y = coor[1]
            if (coor[0]) < (min_x):
                min_x = coor[0]
            if (coor[1]) < (min_y):
                min_y = coor[1]

    shift_x = abs(max_x - min_x) + 20
    shift_y = abs(max_y - min_y) + 20
    # will probably need to change to account for varying origins
    x = x + shift_x
    y = y - shift_y
    return x, y

def set_pos((x, y)):
    t.up()
    t.goto(x, y)
    t.down()

def do():
    # dreaded globals, how can I get around and still use key-binding that takes no arguements
    global i, length
    side_length = length * (1 + i)
    num_sides = 8
    i += 1

    t.begin_poly()
    draw_polygon.draw_poly(t, num_sides, side_length)
    t.end_poly()
    vertecies = t.get_poly()
    set_pos(find_object_dimensions(vertecies))

set_pos((x, y))
wn.onkey(do, "space")
wn.listen()
turtle.mainloop()
