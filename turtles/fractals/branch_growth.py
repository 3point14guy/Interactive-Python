import turtle

def apply_rules(char):
    new_string = ''
    if char == 'F':
        new_string = 'F[-F]F[+F]F'
    else:
        new_string = char
    return new_string

def process_string(chars):
    new_string = ''
    for char in chars:
        new_string = new_string + apply_rules(char)
    return new_string

def create_l_system(iters, axiom):
    start_string = axiom
    end_string = ''
    for i in range(iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string

def draw_l_system(t, inst, angle, distance):
    previous_positions = []
    for char in inst:
        if char == 'F':
            t.color('red')
            t.forward(distance)
        if char == 'B':
            t.color('blue')
            t.backwards(distance)
        if char == '+':
            t.right(angle)
        if char == '-':
            t.left(angle)
        if char == '[':
            previous_positions.append([t.heading(), t.xcor(), t.ycor()])
            # print(previous_positions)
        if char == ']':
            go = previous_positions.pop()
            t.setheading(go[0])
            t.color('blue')
            t.setposition(go[1], go[2])

def main():
    t = turtle.Turtle()
    t.speed(3)
    t.width(3)
    t.setposition(-200, 0)
    wn = turtle.Screen()
    wn.exitonclick()
    inst = create_l_system(4, 'F')

    draw_l_system(t, inst, 25, 15)

main()
