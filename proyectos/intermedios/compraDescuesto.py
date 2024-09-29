#Datos del usuario
nombre = input("Ingrese su nombre: ")
compra = float(input("Ingrese el valor de su compra: "))

descuento = 0 

if compra < 80 :
  print(f'{nombre} Su compra es de {compra} USD es menor a 80USD, No hay Descuento')
elif compra >= 80 and compra < 150:
  descuento = compra * 0.10
elif compra >= 150 and compra <= 300:
  descuento = compra * 0.15
elif compra > 300 and compra < 500:
  descuento = compra * 0.20

precio_final = (compra - descuento)

print(f'Compra sin descuento: {compra} USD, Compra con descuento: {precio_final} USD ')