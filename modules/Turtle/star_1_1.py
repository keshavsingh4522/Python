import turtle
import time
screen=turtle.Screen()
screen.setup(420,320)
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
t=turtle.Turtle()
t.pensize(4)
t.penup()
t.setpos(-90,30)
t.pendown()
for x in range(5):
    t.color(clr[x])
    t.forward(200)
    t.right(144)
t.penup()
t.setpos(80,-140)
t.pendown()
t.pencolor('olive')
t.write('Pure Python',font=('Arial',12,'normal'))
t.ht()
turtle.Screen().exitonclick()