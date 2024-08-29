#sets-->Es una estructura de datos mutables, es una coleccion de datos 
# donde sus elementos NO pueden ser ordenados, los objetos o elementos
# que almacene los sets deben ser Hasheable
# No nos confiemos en cuyo caso la estructura de datos se imprima ordenada, esto puede pasar
# Los sets no permiten datos duplicados o repetidos, esto se debe a que como esta estructura almacena esa info

#Hasheable-->Es cuando un elemento o un objeto va a tener un valor unico que no va a cambiar
#           desde su creacion o declaracion hasta su final
#          ->Si un Objeto es hasheable yo le puedo aplicar una funcion a ese objeto y me va 
        #   a retornar un numero unico para ese objeto
#DECLARACION
miSets = {1,2,3,4,5}
print(miSets)

#Declaracion N°2 de Sets -->Atraves del metodo set()
mi_sets = set()# mi set vacio
mi_sets.add(1)# con el metodo add() agregamos elementos a mi sets
mi_sets.add(2)
mi_sets.add(3)
mi_sets.add(4)
mi_sets.add(2)
print(mi_sets)#{1, 2, 3, 4}
#Aqui podemos evidenciar que aunque agregamos un nuevo elemento al sets, este no se agrego
#debido que el dato se estaria duplicando

print("<-------------------//----------------->")
#Example:
#Declaramos una lista con numeros repetidos
lista_numero = [1,2,4,2,5,1,6,10,2]

ImplentarSet = set(lista_numero)#Atraves de este metodo eliminamos los elementos repetidos de la lists
print(ImplentarSet)#{1, 2, 4, 5, 6, 10}

print("<-------------------//----------------->")
#Set ->Esta estructura de datos tambien es utilizada para busqueda de datos dentro de un conjunto o lista
#Hagamos la sgte operacion booleana, donde buscaremos o verifiquemos si en la lista se encuentra el elemento 5
busqueda = 4 in lista_numero
print(busqueda)#Esto nos retornara o nos imprimira True porque en este caso dentro de la lista si esta el 5

#BONUS: Se recomienda los sets, para este tipo de busqueda ya que por su estructura se encuentra optimizado a comparacion
      # de las listas que busca los elementos por indice, mientras que los sets va al punto inmediatamente