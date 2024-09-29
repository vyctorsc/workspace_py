"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
peso = float(input("Cual es su Peso(kg) actual: "))
estatura = float(input("Cual es estatura(mts,cm): "))

masaCorporal = round(peso/estatura**2)

print(f"Tu índice de masa corporal es: {masaCorporal} ")