"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
print("----//Cuenta de Ahorros ScotiaBank//----")
interes  = 0.04
dineroDepositado = int(input("Ingrese la cantidad de dinero a depositar: "))

ahorroPrimer = (dineroDepositado * interes) + dineroDepositado
print(f"El ahorro del primer año es ${ahorroPrimer}")
ahorroSegundo = (ahorroPrimer * interes) + ahorroPrimer
print(f"El ahorro del segundo año es ${ahorroSegundo}")
ahorroTercer = (ahorroSegundo * interes) + ahorroSegundo
print(f"El ahorro del segundo año es ${ahorroTercer}")
