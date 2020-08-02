import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('blue')
t.speed(0)
c=0
d=0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(15)
    c+=1
    if c>=390/15:
        t.forward(50)
        c=0
        d+=1
        if d>=21:
            break
t.hideturtle()
turtle.done()