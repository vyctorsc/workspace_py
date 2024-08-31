import turtle

ventana = turtle.Screen()
ventana.bgcolor('yellow')
tortuga = turtle.Turtle()
tortuga.speed(2)

for _ in range(5):
    tortuga.forward(200)
    tortuga.right(144)

ventana.exitonclick()