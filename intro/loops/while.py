#Loop o ciclo while, es como un condicional pero iterable siempre y cuando la condicion sea TRUE
# siempre ejecutar una secuencia de tareas cierto numero de veces en base a una condicion que sea True
nombre = ""
correo = ""
mensaje = ""

condicionSalida = "CONTINUE"

while condicionSalida == "CONTINUE":
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    mensaje = input("Ingrese el mensaje a enviar: ")

    print(f"""
    
        Mensaje enviado a {nombre},
          
        destinatario: {correo}
          
        mensaje a enviar: {mensaje}
    """)

    condicionSalida = input("Si desea continuar - escriba CONTINUE: ")
