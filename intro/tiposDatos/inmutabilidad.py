"""
Nota: los tipos de datos, los int, float, boolenaos,Strings tuplas, listas
      tienen dos categorias pueden ser MUTABLES E INMUTABLES 

      Si son INMUTABLES quiere decir que no pueden ser cambiados despues que hayan sido creados.
      int,float,string,bool y los numeros son inmutables.

      Si son MUTABLES quiere decir que pueden ser cambiados despues que fueron creados. 

===> Hay que recordar que en python todo es un objeto, por lo tanto, la variable edad es un objeto
     de la clase o tipo int, con atributos id, valor - por ejemplo: edad --> id = 1111, valor = 18

#INMUTABLE
     ya despues cuando declaramos la variable con el mismo nombre pero diferente valor, 
     estamos creando en realidad otro objeto con el mismo nombre pero diferente id y valor
     representando otro objeto como tal - por ejemplo: edad --> id = 2222, valor = 19

edad = 18 --> id:1111,valor:18 <<Objeto>>

edad = 19 --> id:2222,valor:19 <<Objeto>>

Bonus: Aqui en Python, no pasa como en otros lenguajes, NO estamos reasignando valores a la mis variable,
       por lo tanto, cada vez, que declaramos y reasignamos valor a una variable con el mismo nombre pero
       diferente valor, lo que estamos haciendo en realidad es crear y reservando un nuevo espacio en memoria 
       para esa asignacion de la variable.
"""