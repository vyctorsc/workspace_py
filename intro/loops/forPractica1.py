import turtle #libreria para la interfaz grafica

ventana = turtle.Screen()
ventana.bgcolor('blue')
tortuga = turtle.Turtle()
tortuga.speed(3)

"""
#Dibujar Cuadrado
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)

ventana.exitonclick()

"""

print("----------------//-----------------")

for i in range(4):
    tortuga.forward(200)
    tortuga.right(90)
ventana.exitonclick()