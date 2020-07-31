import turtle
import time
screen=turtle.Screen()
screen.setup(420,320)
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
t = turtle.Pen()
t.ht()
for x in range(5):
    t.color(clr[x])
    t.forward(200)
    t.right(144)
turtle.Screen().exitonclick()