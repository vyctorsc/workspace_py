#For-->Son usados para iterar sobre una secuencia(Iterable) como las estructuras de datos 
#    listas,tuplas, set o cualquier objeto que este en la capacidad de retornar sus elementos
#    uno a uno una vez se lo esten pidiendo

lista_nombre = ['victor','mary','kendry']
tupla_notas = ('victor',30,4.5)
set_departamentos = {'ventas','compras','redes','Tech'}

#Lista
for nombre in lista_nombre:
    print(nombre)

print("<------------//-------------->")

#Tuplas
for nota in tupla_notas:
    print(nota)

print("<------------//-------------->")

#Set
for departamento in set_departamentos:
    print(departamento)