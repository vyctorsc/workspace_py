"""
Diccionario-->
Un diccionario en Python es una estructura de datos que permite almacenar y organizar elementos en pares clave-valor. 
Los diccionarios son MUTABLES
Aquí tienes algunas características clave de los diccionarios:

Claves únicas: Cada clave en un diccionario es única e inmutable.

Valores modificables: Los valores pueden ser de cualquier tipo y pueden ser modificados.

Desordenados: Aunque los diccionarios mantienen el orden de inserción a partir de Python 3.7, no se debe confiar en el orden ya que puede variar en diferentes versiones

mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero"
}

En este ejemplo, mi_diccionario es un diccionario con tres pares clave-valor: “nombre” con el valor “Juan”, “edad” con el valor 30, y “profesion” con el valor “Ingeniero”.

Operaciones comunes con diccionarios
Acceso a elementos: Para acceder a los valores de un diccionario, se utiliza la clave correspondiente.

print(mi_diccionario["nombre"])  # Resultado: Juan

Modificación de elementos: Para modificar un diccionario, simplemente se asigna un nuevo valor a una clave existente o se agrega una nueva clave-valor.

mi_diccionario["edad"] = 31
mi_diccionario["ciudad"] = "Madrid"


"""


#Declaracion
miDiccionario = {
    'edward': [1.4,4.5,5.0],
    'carla': [2.5,5.0,5.0],
    'jonas': [0.0,3.5,3.0]
}

#Declaracion 2--> Con el metodo dict()
miDiccionario2 = dict(
    edward = [1.4,4.5,5.0],
    carla = [2.5,5.0,5.0],
    jonas = [0.0,3.5,3.0]
)

#Diccionario vacio - Declaracion 3
miDiccionario3 = dict()
miDiccionario3 ['edward'] = [1.4,4.5,5.0]
miDiccionario3 ['carla'] = [2.5,5.0,5.0]
miDiccionario3 ['jonas'] = [0.0,3.5,3.0]

miDiccionario3 ['jonas'] = [2.0,4.5,4.0]#De esta forma esta modificando los datos de la key jonas

#Podemos eliminar un elemento con el codigo del
del miDiccionario3['carla']

print(miDiccionario)
print(miDiccionario2)
print(miDiccionario3)

#Extraer las llaves o keys
print(miDiccionario3.keys())

#Extraer valor - values
print(miDiccionario3.values())

#both
print(miDiccionario3.items())