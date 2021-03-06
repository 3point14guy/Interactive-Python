import turtle

t = turtle.Turtle()
t.tracer(False)
t.hideturtle()
wn = turtle.Screen()


def draw_polygon(t, num_sides, side_length):
    global q, next_start
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
        if i == 1 and q == 0:
            next_start = t.pos()

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
    return next_x, next_y

def make_row():
    global q
    while t.pos()[0] < (wn.window_width() / 2):
        t.begin_poly()
        draw_polygon(t, 6, 35)
        t.end_poly()
        vertecies = t.get_poly()
        y = vertecies[1][1]
        next_x, next_y = max_min_coors(vertecies)
        t.up()
        t.goto(next_x, y)
        t.down()
        q += 1
        make_row()
        y = round(vertecies[4][1], 1)
        return y


def stack_rows(start_x):
    y = make_row()
    t.up()
    t.goto(start_x, y)
    t.down()
    while t.pos()[1] < (wn.window_height() / 2):
        stack_rows(start_x)




next_start = []
q = 0
start_x = -(wn.window_width() / 2)
start_y = -(wn.window_height() / 2)
t.up()
t.goto(start_x, start_y)
t.down()
stack_rows(start_x)
t.up()
t.goto(next_start)
t.down()
stack_rows(next_start[0])
print(q)
wn.update()
wn.exitonclick()
