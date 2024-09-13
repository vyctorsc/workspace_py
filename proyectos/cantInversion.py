"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.
"""
cantidad = float(input("Cantidad a invertir?: "))
interes = float(input("Interés porcentual anual?: "))
anios = int(input("número de años?: "))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** anios, 2)))