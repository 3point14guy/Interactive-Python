import turtle

t = turtle.Turtle()
t.tracer(False)
t.hideturtle()
wn = turtle.Screen()

coors = open("labdata.txt", "r")
x_y = []
x_list = []
y_list = []
n = 0

for line in coors:
    x_y = line.split()
    for i in range(len(x_y)):
        x_y[i] = int(x_y[i])
    x_list.append(x_y[0])
    y_list.append(x_y[1])
    n += 1

# x_max = max(x_list)
# x_min = min(x_list)
# y_max = max(y_list)
# y_min = min(y_list)
#
#
# wn.setworldcoordinates(0, 0, x_max + 5, y_max + 5)

x_sum = sum(x_list)
y_sum = sum(y_list)
x_avg = x_sum / n
y_avg = y_sum / n

numerator_constant = n * x_sum * y_sum
denominator_constant = n * x_sum ** 2
numerator_sum = 0
denominator_sum = 0

for i in range(len(x_y)):
    numerator_sum = numerator_sum  + (x_list[i] * y_list[i] - numerator_constant)
    denominator_sum = denominator_sum + (x_list[i] ** 2 - denominator_constant)

m = numerator_sum / denominator_sum
y = 0



for i in range(len(x_list)):
    y = y_sum + m * (x_list[i] - x_sum)
    t.up()
    t.goto(x_list[i], y)
    t.down()
    t.dot(3, "red")
    t.up()
    t.goto(x_list[i], y_list[i])
    t.down()
    t.dot(3, "blue")

x_max = max(x_list)
x_min = min(x_list)
y_max = y_sum + m * (x_max - x_sum)
y_min = y_sum + m * (x_min - x_sum)

t.up()
t.goto(x_min, y_min)
t.down()
t.color("green")
t.goto(x_max, y_max)

wn.update()
wn.exitonclick()
