print("------//Intercambio de Valores//-------")

valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese otro valor: "))

valor1, valor2 = (valor2,valor1)#Las Tuplas nos permite hacer este intercambio de valores sencillamente si variables auxiliares.

print(f'Hubo Intercambio de valores, valor 1:{valor1} & valor 2:{valor2}')