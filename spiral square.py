import turtle
wn = turtle.Screen()
wn.bgcolor("blue")        # set the window background color  

elan = turtle.Turtle()
elan.color("pink")              # make tess blue
elan.pensize(10)

distance = 50
for _ in range(20):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10