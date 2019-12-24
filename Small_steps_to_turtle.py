import turtle
toon = turtle.Turtle()
toon.speed(10)
toon.forward(60)
toon.left(90)
toon.forward(60)
toon.left(90)
toon.forward(60)
toon.left(90)
toon.forward(60)
toon.right(90)
tin = turtle.Turtle()
tin.speed(10)
tin.setposition(0,0)
tin.right(72)
for i in range(5):
    tin.forward(60)
    tin.right(72)
ton = turtle.Turtle()
ton.speed(10)
ton.penup()
ton.setposition(60,60)
ton.pendown()
length = 20
b = 15
d = ((b-2)*180)/b
c = 180 - d
for i in range(b):
    ton.forward(length)
    ton.left(c)
tak = turtle.Turtle()
length = 70
tak.penup()
tak.setposition(60,0)
tak.pendown()
tak.speed(10)
for i in range(5):
    tak.forward(length)
    tak.left(144)
tell = turtle.Turtle()
tell.pencolor("green")
tell.speed(0)
tell.penup()
tell.setposition(0,60)
tell.pendown()
length = 150
for i in range(40):
  tell.backward(length)
  tell.right(123)
trl = turtle.Turtle()
trl.speed(0)
trl.penup()
trl.setposition(-100,-100)
trl.pencolor("red")
length = 50
thick = 10
width = 6
height = 7
for i in range(height):
    for j in range(width):
        trl.dot()
        trl.forward(length)
    trl.backward(length*width)
    trl.right(90)
    trl.forward(thick)
    trl.left(90)
tkl = turtle.Turtle()
tkl.speed(0)
tkl.pencolor("orange")
tkl.penup()
tkl.setposition(30,30)
tkl.pendown()
for i in range(180):
    tkl.forward(60)
    tkl.right(30)
    tkl.forward(30)
    tkl.left(60)
    tkl.forward(45)
    tkl.right(30)
    tkl.penup()
    tkl.setposition(30,30)
    tkl.pendown()
    tkl.right(2)
    
