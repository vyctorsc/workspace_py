"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
nombre = input("Ingrese su nombre y apellido: ")
horasWork = int(input("Cuantas horas trabajo?: "))
costoHoras = int(input("Cual es el valor por hora?: "))

print("------------------//---------------------")

pago = (horasWork * costoHoras)

print(f"Sr(a) {nombre}")
print(f"Su pago correspondiente por las horas trabajadas son: {pago}")