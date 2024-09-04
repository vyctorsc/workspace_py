print("----//Convertir las horas en Segundo en Total//----")

hora = int(input("Digite la hora: "))
minutos = int(input("Digite los minutos: "))
segundos = int(input("Digite los segundos: "))

horas_seg = hora * 3600
minutos_seg = minutos * 60

total = ( horas_seg + minutos_seg + segundos)

print(f"Los segundos totales que hay en la hora ingresada son: {total}seg ")