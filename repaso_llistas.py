#Repaso Listas

lista = [] #lista vacía

lista.append("Anna")    #lista con 1 elemnto, ["Anna"] (entre comillas)
print(lista)

lista[0]    #las listas son conelecciones de datos indexados, EMPIEZA POR 0

lista_int = range(1,21,2)   #entre el 1 y el 21 de 2 en 2 (pares)
print(lista_int, type(lista_int))   #sin el list() coje el valor como string, hay qu hacer casting a lista

lista_int = list(range(1,21,2))
print(lista_int)

lista_nombres = ["Pol","Nao","Sara","Pepe"]
#Indices:          0     1     2      3
for nombre in lista_nombres:
    indice = lista_nombres.index(nombre)    #en python no se itera sobre un indice sino sobre un valor de la lista, hay que usar una funcion para encontrar el indice
    print(f"{indice}, {nombre}")

for a, b in enumerate(lista_nombres):       #enumerate devuelve para cada elemento el indice y el valor
    print(f"{a}, {b}")                      #a=indice, b=valor

#copia de una lista
nueva_lista1 = lista_nombres.copy() #hace una copia
nueva_lista2 = lista_nombres[:]     #hace un slicing de todo y lo asigna a la lista nueva, (de inicio:a fin:de 1 en 1)
print(f"{nueva_lista1 == nueva_lista2}")

#Mini ejercicio:obtener los numeros pares
lista_numeros = list(range(0,21))

#necesitamos otra lista solo con los numeros pares

lista_pares = lista_numeros[::2]    #de inicio:a fin : de 2 en 2
print(lista_pares)
lista_sq = []
#Necesitamos otra lista con los numeros elevados al cuadrado
lista_numeros2 = list(range(0,11))
print(lista_numeros2)
for i, numero in enumerate(lista_numeros2):
    lista_sq.append(numero * numero)
print(lista_sq)