"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
nombre = input("Cual es tu nombre completo?: ")

print(nombre.lower())#devuelve toda una cadena en minuscula
print(nombre.upper())#devuelve toda una cadena en MAYUSCULA
print(nombre.title())#devuelve la primera letra en mayuscula de cada palabra.