#LISTAS []

#Las listas en python equivalen a los Array de otros lenguajes
#Las listas y los sting son ITERABLES, a serapacion de elementos es con ,
#una lista es una coleccion de datos indexada, empieza a contar desde 0

import os
os.system("cls")

lista_numeros = [1,2,3,4,5]
lista = ["a","b","c","d","e","f","g","b"]   #lista de strings
lista_mixta = [1, "hola", 3.5, True]    #lista mixta
lista_de_listas = [[1,2],[3,4],[5,6]]   #lista de listas, array 3x2
"""
for x in lista:
    print(x)
for x in lista_mixta:
    print(x)
    print(type(x))
for x in lista_de_listas:
    print(x)
    print(type(x))
"""
#las listas estan indexadas
#Acceder al primer valor: lista[0]
#Acceder al ultimo valor: lista[-1] | empieza desde atras-1,-2,-3...

#SLICING   - con :
#[inicio:final:paso], inicio por defecto = 0 | final por defecto = -0 (último) | paso por defecto = 1
    #lista[::-1] invierte la lista 
print(lista[1:3])   #[b,c], en el slicing el ultimo valor no esta inlcuido(se empieza por 0)
print(lista[-3:-1]) #[e,f] no incluye el -1, [-3:]incluye al último si no le indicas nada

#Añadir un elemento al final
lista_numeros.append(6) #Añade un 6 al final
print(lista_numeros)

#Quitar un elemento del final   ,se puede guardar el valor que quitas, pop separa el ultimo elemento, si no lo guardas se pierde
ultimo_numero = lista_numeros.pop()
print(ultimo_numero, lista_numeros)

#Poner un elemento en una posicion concreta .insert(posicion, valor)
lista_numeros = [1,2,4,5]
lista_numeros.insert(2,3)
print(lista_numeros)

#Para eliminar por una posicion concreta|| del lista[posicion]
print("del ", lista)
del lista[2]
print("del ",lista)

#.remove("valor"), para eliminar UN elemento por valor en vez de por posicion SOLO UNO, solo elimina el primero que encuentra
print(lista)
num = lista.count("b")
#print(num)
for x in range (num):         #(0,1) de 0 a 1, no cuenta el ultimo || 2 veces
    #print(x)
    lista.remove("b")         #quita todas las "b" de la lista
print(lista)
"""
#Unir 2 listas, 3 metodos
lista1 = [0,1,2]
lista2 = [3,4,5]

lista1.extend(lista2)
lista1 = lista1 + lista2
#lista2.extend(lista1)
lista1 += lista2
print(lista1)
"""

# https://www.w3schools.com/python/python_arrays.asp