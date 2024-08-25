nombre = 'Ingeniero Victor' #String con comillas simples
nombre2 = "Alfonso" #String con comillas dobles
texto = """ Hola, Soy Victor Simarra, Ingeniero de sistemas, developer,Soport TI    
Por lo visto me puedo desempeñar en diversos Roles en el area de la Tecnologia"""

print(len(nombre)) #Con len, sabremos la longitud o tamaño de nuestro string o cadena
#Hay que tener en cuenta los espacios, se contabilizan como caracter o parte de la cadena
print(nombre)

#BONUS

producto1 = "001 - Mango"
producto2 = "Mango2 - 001"

print(producto1.removeprefix('001 -'))
print(producto2.removesuffix(' - 001'))