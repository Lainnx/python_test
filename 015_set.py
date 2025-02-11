#SET -> conjunto logico
#No pueden tener valores repetidos

lista_numeros = [1,2,2,5,7,5,4,1]   #si quisieraq quiat loos valores repetidos
lista_sin_repeticiones = list(set(lista_numeros))   #pasar lista_numeros a set y despues a lista otra vez (el set eliminara los valores repetidos)
print(lista_numeros, lista_sin_repeticiones, set(lista_numeros))    #set{}, el set por defecto ordena de menor a mayor

