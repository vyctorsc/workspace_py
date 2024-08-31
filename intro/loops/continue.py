#CONTINUE --> Esta sentencia, a comparacion de la sentencia break que detenia por completo el flujo, lo que haria esta sentencia es omitir,nos permitira omitir cierta iteracion de nuestro ciclo, como un salto de pagina o una tabulacion por asi decirlo y luego continuara con la sgte iteracion.

listaNumero = [34,10,23,57,19,2,8,3]

for numero in listaNumero:
    if(numero%2 != 0):
        continue
    print(numero)