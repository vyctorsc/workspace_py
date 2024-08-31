import random
import turtle

ventana = turtle.Screen()
ventana.title("---->>Carrera de Caracoles<<----")
ventana.bgcolor('lightblue')
ventana.setup(width=800,height=600)

#CARACOL 1 - TORTUGA 1
caracol1 = turtle.Turtle()
caracol1.shape('turtle')
caracol1.color('red')
caracol1.penup()
caracol1.goto(-300,100)

#CARACOL 2 - TORTUGA 2
caracol2 = turtle.Turtle()
caracol2.shape('turtle')
caracol2.color('blue')
caracol2.penup()
caracol2.goto(-300,-100)

meta = 300

#Dibujar linea de Meta
metaLinea = turtle.Turtle()
metaLinea.penup()
metaLinea.goto(meta, 150)
metaLinea.pendown()
metaLinea.goto(meta, -150)
metaLinea.hideturtle()


while True: #(caracol1 < 20 and caracol2 < 20):
    avanceCaracol1 = random.randint(1,20)
    avanceCaracol2 = random.randint(1,20)

    if avanceCaracol1 % 2 == 0 or avanceCaracol2 %2 == 0:
        continue
    
    caracol1.forward(avanceCaracol1)
    caracol2.forward(avanceCaracol2)

    print(f"El caracol 1 avanza {avanceCaracol1}, para un total de: {caracol1.xcor()}")
    print(f"El caracol 2 avanza {avanceCaracol2}, para un total de: {caracol2.xcor()}")
    print("---------------//------------------//----------------")

    if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
        break

if caracol1.xcor() > caracol2.xcor():
    print(f"Felicidades caracol 1 <<<GANASTE>>>")
elif caracol2.xcor() > caracol1.xcor():
    print(f"Felicidades caracol 2 <<<GANASTE>>>")
else:
    print("Esto es un empate")

ventana.exitonclick()
