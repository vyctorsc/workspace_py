#Hasheable-->Es cuando un elemento o un objeto va a tener un valor unico que no va a cambiar
#           desde su creacion o declaracion hasta su final
#          ->Si un Objeto es hasheable yo le puedo aplicar una funcion a ese objeto y me va 
        #   a retornar un numero unico para ese objeto
#Sets - los string son inmutables, por lo tanto tienen un valor hash
frutas = {'manzana',
          'banano',
          'pera',
          'uva'}

print(hash('manzana'))#-3911853315586403175

