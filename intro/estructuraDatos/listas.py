"""
En Python, las listas son una estructura de datos que permite almacenar una colección de elementos en un solo objeto. Son mutables, lo que significa que se pueden modificar después de su creación.

accedemos a los datos o los elemento atraves de los indices
"""

listaNum = [1,2,3,4]
listaName= ['Victor','Ismael','Keiner']
listaBool= [True,False,False]

#Convirtiendo una Tupla en una lista, con el metodo list()
listaNumeros = list((1,2,3))
print(type(listaNumeros))

print("<------------------------------//------------------------->")
#Metodos de las listas
listaNumeros1 = [1,2,3]

#append -->Este metodo añade o agrega elementos a la lista, pero al final
listaNumeros1.append(4)
listaNumeros1.append(5)
listaNumeros1.append(5)
print(listaNumeros1)#[1,2,3,4,5,6]

#count -->Este metodo me permite contar cuantos elementos con el mismo valor se encuentran en mi lista
print(listaNumeros1.count(5))

print("<------------------------------//------------------------->")
#extend -->Nos permite extender la lista, con otros elementos que definamos en otra variable
listaExtendida = [100,101]
listaNumeros1.extend(listaExtendida)
print(listaNumeros1)#[1, 2, 3, 4, 5, 5, 100, 101]

print("<------------------------------//------------------------->")
#index -->Nos permite buscar en una lista de elementos, si el elemento existe y nos retonar la posicion o el indice donde se encuentra el elemento.

listaNumeros1.index(101)
print(listaNumeros1)
print(listaNumeros1.index(101))

print("<------------------------------//------------------------->")

#insert -->Este metodo es similar al append, inserta o agrega elemento a la lista en cualquier posicion que nosotros definamos con el indice.
print(listaNumeros1)#[1, 2, 3, 4, 5, 5, 100, 101]
listaNumeros1.insert(1,404)
print(listaNumeros1)#[1, 404, 2, 3, 4, 5, 5, 100, 101]

print("<------------------------------//------------------------->")

#pop -->Nos permite extraer elementos de la lista y los retorna, tenemos que pasarle como parametro el indice o la posicion del elemento que vamos a extraer, en caso tal no definamos el indice, por defecto el metodo extraeria el ultimo elemento de la lista.
print(listaNumeros1)#[1, 2, 3, 4, 5, 5, 100, 101]
print(listaNumeros1.pop())#extrae el ultimo elemento de la lista. -->101
print(listaNumeros1)#[1, 2, 3, 4, 5, 5, 100]

print("<------------------------------//------------------------->")

#remove-->Nos permite remover elementos de nuestra lista, por valor y no por indice
print(listaNumeros1)
listaNumeros1.remove(100)
print(listaNumeros1)

print("<------------------------------//------------------------->")

#reverse -->Nos permite revertir o cambiarle el sentido a la lista
print(listaNumeros1)
listaNumeros1.reverse()
print(listaNumeros1)

print("<------------------------------//------------------------->")

#clear -->Nos permite vaciar o eliminar los elemento de la lista
print(listaNumeros1)
listaNumeros1.clear()
print(listaNumeros1)

print("<------------------------------//------------------------->")

#sort -->Nos permite organizar o ordenar la lista de menor a mayor
listaDesordenada = [55,6,7,8,56,100,404]

print(listaDesordenada)
listaDesordenada.sort()
print(listaDesordenada)






