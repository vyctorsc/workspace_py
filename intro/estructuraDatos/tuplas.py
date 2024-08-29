"""
TUPLAS
Es una estructura de datos inmutable, Una tupla en Python es una colección ordenada e inmutable de elementos. Esto significa que, una vez creada, no se pueden modificar, añadir o eliminar sus elementos. Diversidad de tipos: Pueden contener diferentes tipos de datos (enteros, cadenas, flotantes, etc.).

Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas. Aquí tienes un ejemplo básico:


mi_tupla = (1, 'dos', 3.0)


"""
#Para declarar un tupla generalmente utilizamos parentesis, y los elementos separados por como ',' 
#Pero esto no es obligatorio
tupla = (1, False, 'victorsc', 0.55)
print(tupla[3])#0.55

tupla =1, False, 'victorsc', 0.55
print(type(tupla))#imprimira que la variable  es de tipo tupla

#Una de las caracteristica de una tupla es que podemos retornar mas de un elemento en una funcion.
def retornar_estudiante():
    return 'victorsc', 30, 1.80

tupla_estudiante = retornar_estudiante()
print(tupla_estudiante)

#Accediendo a los elementos o valores de la tupla atraves de los indices
nombre_estudiante = tupla_estudiante[0]
edad_estudiante = tupla_estudiante[1]
altura_estudiante = tupla_estudiante[2]

print(nombre_estudiante, edad_estudiante, altura_estudiante)

#Podemos simplificar esto de una mejor forma, deacuerdo al orden que coloquemos
#esto no los permite hacer las tuplas.
nombre_estudiante, edad_estudiante, altura_estudiante = retornar_estudiante()
print(nombre_estudiante)
print(edad_estudiante)
print(altura_estudiante)

#One-line swapping - gracias a esto podemos hacer lo mismo pero en una misma linea de codigo
#Hagamos un intercambio de variables
variable1 = 10
variable2 = 20

variableTemp = variable1
variable1 = variable2
variable2 = variableTemp

print("Variables Intercambiadas ",variable1,variable2)

var1 = 1.0
var2 = 2.0

var1,var2 = (var2, var1) #Asi de sencillo podemos implentar el One-line swapping y intercambiar variables atraves de la tuplas. es Opcinal los parentesis en las tuplas