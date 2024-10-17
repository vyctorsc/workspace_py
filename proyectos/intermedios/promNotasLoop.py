#Datos del usuario

nombre = input("Ingrese su nombre: ")
cantidad_materias = int(input("Ingrese cantidad de materias: "))

contador = 1
sumatoria = 0


while contador <= cantidad_materias:
  nombre_materia = input("Ingrese nombre de la materia: ")
  nota = float(input("Ingrese la nota de la materia  de " + nombre_materia + ":"))

  sumatoria = sumatoria + nota
  contador = contador + 1



prom = (sumatoria)/cantidad_materias

print(" ")
print("///<<<>>>RESULTADOS<<<>>>>///")
print(f'El Promedio de las materias ingresadas es: {prom}')