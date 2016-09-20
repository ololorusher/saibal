import turtle
s = input()
turtle.shape('turtle')
turtle.pendown()
while s != '0':
    if s == 'l': turtle.left(90)
    elif s == 'r': turtle.right(90)
    elif s == 'g': turtle.forward(50)
    s = input()