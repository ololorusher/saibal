
import turtle
n=int(input())
turtle.shape(turtle)
turtle.pendown()
for i in range(101):
    turtle.left(360/100)
    turtle.forward(i*4)
    turtle.goto(0,0)
    for j in range(101):
        turtle.right(360/100)
        turtle.forward(i*4)
    turtle.goto(0,0)
input()