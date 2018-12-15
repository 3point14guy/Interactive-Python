import turtle
import paneo


t = turtle.Turtle()
t.tracer(False)
t.hideturtle()
wn = turtle.Screen()

def folded_code():
    # # positioning to line up hexagon around paneo curve
    # t.up()
    # t.goto(3, 11)
    # t.down()
    # t.right(149)

    # # draw_poly takes turtle, number of sides, and side length arguements
    # polygon.draw_poly(t, 6, 98)

    # # create_L_system takes number of iterations, and an axiom
    # inst = paneo.create_L_system(3, "FX")
    #
    # t.up()
    # t.home()
    # t.down()
    #
    # # draw_L_system takes turtle, instructions, angle and line length
    # paneo.draw_L_system(t, inst, 60, 8)
    # t.home()
    print("")

def draw_polygon(t, num_sides, side_length):

    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

def max_min_coors(vertecies):
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

    next_x = abs(max_x - min_x) + (vertecies[1][0])
    next_y = abs(max_y - min_y) + (vertecies[1][1])
    # print(next_x, next_y)
    return next_x, next_y

def make_row():
    while t.pos()[0] < (wn.window_width() / 2):
        t.begin_poly()
        draw_polygon(t, 6, 50)
        t.end_poly()
        vertecies = t.get_poly()
        # print(vertecies)
        y = vertecies[1][1]
        next_x, next_y = max_min_coors(vertecies)
        t.up()
        t.goto(next_x, y)
        t.down()
        make_row()
        y = round(vertecies[4][1], 1)
        next_start = vertecies[2]
        return y, next_start


def stack_rows(start_x):
    y, next_start = make_row()
    t.up()
    t.goto(start_x, y)
    t.down()
    while t.pos()[1] < (wn.window_height() / 2):
        stack_rows(start_x)

# def fill_columns():


start_x = -(wn.window_width() / 2)
start_y = -(wn.window_height() / 2)
t.up()
t.goto(start_x, start_y)
t.down()
stack_rows(start_x)

wn.update()
wn.exitonclick()
