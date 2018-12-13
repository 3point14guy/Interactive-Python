import turtle
import time

turtle.setup(900, 900)
t = turtle.Turtle()
t.color("yellow")
t.speed(0)
canvas = turtle.Screen()
canvas.bgcolor("black")

# def spiral(t, angle, increment, side, times):
#     # if side > 1000:
#     #     t.color("green")
#     # elif side > 700:
#     #     t.color("red")
#     # elif side > 400:
#     #     t.color("blue")
#
#     if times > 0:
#         t.forward(side)
#         t.right(angle)
#         spiral(angle, increment, (side + increment), (times - 1))

def spiral2(t, angle, increment, side, times):
    reverse_direction = 100
    t.forward(side)

    if side % (reverse_direction * 2) == 0:
        angle = angle + 2
        t.color("yellow")
    elif side % reverse_direction == 0:
        angle = angle - 2
        t.color("orange")

    t.right(angle)
    side = side + increment
    if side < times:
        # time.sleep(1)
        spiral2(t, angle, increment, side, times)

def resume():
    time.sleep(0)

def pause():
    time.sleep(5)

t.penup()
#t.goto(-450, 300)
t.pendown()
t.width(2)
#spiral(t, 121, 2, 10, 200)
# spiral2(t, 119, 2, 0, 600) # # triangle based
#spiral2(t, 80, 1, 0, 600) # # square based
# spiral2(t, 56, 1, 0, 600) # # hexagon based
# spiral2(t, 75, 1, 0, 600) # # pentagon based
t.width(1)

spiral2(t, 150, 2, 0, 300) # # star based
canvas.onkey(pause, "Up")
canvas.onkey(resume, "Down")

canvas.listen()

turtle.mainloop()
