import turtle


screen = turtle.Screen()
'''
screen.bgcolor("red")
screen.title("Prueba Turtle")

icon = turtle.Turtle()
icon.pencolor("yellow")
icon.fillcolor("green")
icon.pensize(5)
icon.shape("turtle")
icon.shapesize(3,3,3)

icon.speed(10)

icon.penup()
icon.backward(100)
icon.right(90)
icon.forward(100)
icon.left(90)
icon.forward(100)
icon.left(90)
icon.forward(100)

icon.pendown()
icon.goto(100,100)
icon.home()
icon.circle(10)
icon.dot(30)

icon.hideturtle()
icon.speed(1)
icon.circle(50)
icon.stamp()

icon.showturtle()
icon.setx(100)
icon.sety(100)

icon.undo()
icon.clear()
icon.reset()

icon.begin_fill()
icon.color("blue")
icon.circle(50)
icon.end_fill()
'''
screen = turtle.Screen()
icon = turtle.Turtle()

'''
icon.fd(100)
icon.rt(90)
icon.fd(100)
icon.rt(90)
icon.fd(100)
icon.rt(90)
icon.fd(100)
'''

for i in range(4):
    icon.fd(100)
    icon.rt(90)
    
i = 100
while i > 0:
    icon.circle(i)    
    i -= 10
    
#turtle.done() 



