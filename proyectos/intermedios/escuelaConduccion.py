"""
En una escuela de consuccion se tiene un programa que dependiendo de la edad del
usuario debe mostrar el tipo de licencia a la que tienne derecho.
condicion 1: si es menor a 16, entonces no puedes conducir.
condicion 2:si es menor a 18, entince pudes obtener un permiso para conducir.
condicion 3. si es menor a 70, entonce pude obtener una licwencia estandar.
condicion 4: si es manoy a 70, entonces necesita una licencia especial

"""
print("<-------//Escuela de Conduccion Quillami//------->\n")
print("Condiciones para Adquirir su licencia de Conduccion \n")

edad = int(input("Ingrese su edad: "))

if edad <= 16:
    print(f'Tu edad es {edad} años, eres menor de edad, NO puedes conducir')
elif edad > 16 and edad <= 18:
    print(f'Tu edad es {edad} años, Puedes obtener un permiso de Conducir')
elif edad > 18 and edad <= 70:
    print(f'Tu edad es {edad} años, Puedes obtener una licencia estandar')
else:
    print(f'Tu edad es {edad} años, Necesitas un permiso Especial para Conducir')
