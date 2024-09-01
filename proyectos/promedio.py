print("-----//Promedio de Notas//-----")

nota1 = float(input("Ingrese Nota #1: "))
nota2 = float(input("Ingrese Nota #2: "))
nota3 = float(input("Ingrese Nota #3: "))


prom =(nota1 + nota2 + nota3)/3

if prom >= 4.0 and prom <= 5.0:
    print(f'Felicidades, Ganaste la Materia en {prom}')
elif prom >= 3.0 and prom <= 3.9:
    print(f'Felicidades, Ganaste la Materia en {prom}, pero puedes esforzarte mas')
elif prom >= 2.5 and prom <= 2.9:
    print(f'Perdiste la Materia en {prom}, Pero tienes derecho a validacion')
else:
    print(f'Perdiste la Materia en {prom}, Vuelve a intentarlo en el proximo semestre')

