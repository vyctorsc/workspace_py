#FROZENSET-->son Inmutables, es simplenmente un set que no se puede modificar
        #No son tan utilizado, se utiliza para optimizar el codigo
        #al declararlo podemos pasarle lista,sets, cadenas
        #una vez creado, nose puede modificar
        #
frutas = {'manzana',
          'banano',
          'pera',
          'uva'}#sets

misFrozenSet = frozenset(frutas)
print(misFrozenSet)