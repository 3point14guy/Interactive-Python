import turtle
import time

def draw_triangle(points,color,t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()

def get_mid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, iters, t):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    # time.sleep(3)
    draw_triangle(points, colormap[iters], t)
    # base case
    if iters > 0:
        # recursive call
        # iters - 1 changes state getting closer to base case
        sierpinski([points[0],
                        get_mid(points[0], points[1]),
                        get_mid(points[0], points[2])],
                   iters - 1, t)
        sierpinski([points[1],
                        get_mid(points[0], points[1]),
                        get_mid(points[1], points[2])],
                   iters - 1, t)
        sierpinski([points[2],
                        get_mid(points[2], points[1]),
                        get_mid(points[0], points[2])],
                   iters - 1, t)

def main():
   t = turtle.Turtle()
   t.speed(1)
   wn = turtle.Screen()
   # turtle.tracer(False)
   start_points = [[-200,-100], [0,200], [200,-100]]
   sierpinski(start_points, 5, t)
   # turtle.update()
   wn.exitonclick()


main()
