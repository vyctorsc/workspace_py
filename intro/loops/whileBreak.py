#break -->El break es una sentencia frecuente en los ciclos while o for, esta sentencia
#permitira parar el ciclo o loops aunque este no haya terminado de iterar

import random

meta = 20

caracol1 = 0
caracol2 = 0

while True: #(caracol1 < 20 and caracol2 < 20):
    avanceCaracol1 = random.randint(1,4)
    avanceCaracol2 = random.randint(1,4)

    caracol1 = caracol1 + avanceCaracol1
    caracol2 = caracol2 + avanceCaracol2

    print(f"El caracol 1 avanza {avanceCaracol1}, para un total de: {caracol1}")
    print(f"El caracol 2 avanza {avanceCaracol2}, para un total de: {caracol2}")
    print("---------------//------------------//----------------")

    if caracol1 >= 20 or caracol2 >= 20:
        break

if caracol1 >= meta:
    print(f"Felicidades caracol 1 <<<GANASTE>>>")
else:
    print(f"Felicidades caracol 2 <<<GANASTE>>>")