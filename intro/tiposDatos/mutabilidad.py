"""
Nota: los tipos de datos, los int, float, boolenaos,Strings tuplas, listas
      tienen dos categorias pueden ser MUTABLES E INMUTABLES 

      Si son INMUTABLES quiere decir que no pueden ser cambiados despues que hayan sido creados.
      int,float,boleano,string

      Si son MUTABLES quiere decir que pueden ser cambiados despues que fueron creados, generalmente
      estos tipos de datos son: list, dict, sets. 

      list o Lista 
        En Python, las listas son una estructura de datos que permite almacenar una colección de elementos en un solo objeto. Son mutables, lo que significa que se pueden modificar después de su creación.

        Características de las listas en Python:

        1. Ordenadas: Los elementos se almacenan en un orden específico.
        2. Indexadas: Cada elemento tiene un índice (posición) que comienza en 0.
        3. Mutables: Se pueden agregar, eliminar o modificar elementos.
        4. Dinámicas: Pueden crecer o disminuir en tamaño según se necesite.
        5. Polimórficas: Pueden contener elementos de diferentes tipos (enteros, cadenas, objetos, etc.).

        Operaciones comunes con listas:

        1. Creación: lista = [elemento1, elemento2, ...]
        2. Indexación: lista[índice]
        3. Slicing: lista[inicio:fin]
        4. Agregar elementos: lista.append(elemento)
        5. Eliminar elementos: lista.remove(elemento)
        6. Insertar elementos: lista.insert(índice, elemento)
        7. Ordenar: lista.sort()
        8. Longitud: len(lista)

        Ejemplo:

        # Crear una lista
        frutas = ['manzana', 'banana', 'naranja']

        # Acceder a un elemento
        print(frutas[0])  # Imprime 'manzana'

        # Agregar un elemento
        frutas.append('fresa')
        print(frutas)  # Imprime ['manzana', 'banana', 'naranja', 'fresa']

        # Eliminar un elemento
        frutas.remove('banana')
        print(frutas)  # Imprime ['manzana', 'naranja', 'fresa']

        Las listas son una herramienta fundamental en Python, utilizadas en una amplia variedad de situaciones, como almacenar datos, representar matrices, o implementar algoritmos.

===> Hay que recordar que en python todo es un objeto, por lo tanto, la variable edad es un objeto
     de la clase o tipo int, con atributos id, valor - por ejemplo: edad --> id = 1111, valor = 18

#MUTABLES

pasa por que la lista es mutable, si es mutable puede ser modificada. a diferencia de los objetos inmutables los cuales no pueden cambiar y por eso es que se genera uno nuevo con un ID distinto

    EJEMPLO:
        lista = [1,2,3,4]
    print(lista[0])#Imprime el dato en el indice 0 --> 1

    id(lista)# id --> 3333
    valor --> [1,2,3,4]

    #Agregandole o añadiendole un dato a la lista con el metodo o la funcion append()
    lista.append(5)
    print(lista)#Imprime la lista con el nuevo dato añadido [1,2,3,4,5]

    id(lista) -->out-->id:3333
    valor --> [1,2,3,4,5]
    

"""