"""
Indexing: Seria la capacidad de acceder a elementos o 
        caracteres especificos de una cadena de caracteres atraves de un indice.
 
Slicing: Nos permite extraer cadenas mas grandes, de mi cadena principal y no simplemente un caracter
         aplica para LISTAS,TUPLAS o otro tipo de secuencia
"""
#INDEXING -------------------------------------------------------->
cadenaCaracteres = "Hola, Mundo!"
print(cadenaCaracteres[0])# Nos imprime el caracter H

#Atraves de esta formula extraemos el ultimo cararacter de una cadena, en caso tal esta sea muy larga
print(cadenaCaracteres[-1])

#SLICING---------------------------------------------------------->
cadena = "Hola, Mundo!"
print(cadena[0:4])# El Cero 0 nos indica el punto de partida, el cuatro 4 nos indica hasta donde llegar o terminar
#Nos imprimira la cadena Hola --- H->0 o->1 l->2 a->3 -- ,->4 la coma no seria inclusiva

print(cadena[6:11])# El punto de partida seria desde el indice u posicion 6 que seria M siendo inclusiva, 
# y terminaria en la posicion o indice 11 que seria !, pero no nos mostraria ese caracter sino el caracter que se encuentra antes

#SLICING CON SALTOS
print(cadena[::2])#apartir del tercer parametro le estamos indicando los saltos, cada cuanto
# Nos Imprimi HL,Mno

#ejemplo#2

telefono = "4-5-6-7-8-9"
print(telefono[::2]) #Nos imprime el numero de telefono sin lo guiones

telefono = "-4-5-6-7-8-9"
print(telefono[1::2])

