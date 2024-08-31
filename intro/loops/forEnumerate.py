"""
lista_elementos = [1,2,3,4,5]
for elemento in lista_elementos:
    print(elemento)

print("<------------//-------------->")

for _ in range(10):
    print("Ingeniero VictorSimarra")#Lo imprimira 10 vece
"""
#ForEnum -->Los usamos en python para extraer los indices de la lista o de la estructura iterable
# Hay dos formas de hacerlo atraves del loop For:

# Forma #1 para acceder a los indice de una lista
listaNombres = ['victorsc','mary','kendry']
for indice in range(3):
    print(indice, listaNombres[indice])
print("<-------------//------------>")
# Forma #2 con el metodo enumerate()
for indice, valor in enumerate(listaNombres):
    print(indice, valor)