"""
+ Desarrollar un Script que pida la edad y altura del usuario
+ Si la persona es mayor de edad puede participar
+ Pero la persona debe medir mas de 1.70
+ Si la persona no mide 1.70 podra participar si es mayor a 25 años
+ Y su altura es mayor a 1.65
"""
nombre = input("Cual es su nombre?: ")
edad = int(input("Digita su edad: "))
altura = float(input("Digite su altura: "))

if edad >= 18:
   if (altura >= 1.70) or (edad >= 25 and altura >= 1.65):
      print(f'Felicitaciones {nombre}, Puedes participar en el equipo de baloncesto')
   else:
      print('No cumples con los requisitos para ser parte del equipo')
else:
   print(f'Lo sentimos, eres menor de edad, No puedes participar')