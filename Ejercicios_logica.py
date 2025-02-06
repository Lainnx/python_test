#1_El usuario introduce un numero entero, como maximo 100
# ese numero es el limite
# desde 0 hasta el numero introducido[los dos incluidos], vamos a listartodos los numeros
# Pero si el numero es multiple de 3 escribiremos: -FIZZ
# Pero si el numero es multiple de 5 escribiremos: -BUZZ
# SI es multiple de ambos: -FIZZ-BUZZ
# en los demas casos solo el numero
# si el usuario escribe mas de 100 o menos de 0: el numero es incorrecto

import os
os.system("cls")

# try:
#     n= int(input("escribe un numero entre 0 y 100: "))
#     if 0 <= n <= 100:
#         for i in range(n+1):        #for i in range(0(desde), i+1(hasta),1(paso) )
#             if i == 0:
#                 print("0")
#             elif i % 3 == 0 and i % 5 == 0:           #Empezar por la mas restrictiva
#                 print(f"{i}-FIZZ-BUZZ")
#             elif i % 5 == 0:
#                 print(f"{i}-BUZZ")
#             elif i % 3 == 0:
#                 print(f"{i}-FIZZ")
#             else:
#                 print(f"{i}")
#     else:
#         print("el numero es incorrecto")
#         exit()                                        #sale del programa

# except ValueError:
#     print("tienes que escribir un numero")

#2_Vamos a recibir un texto por parte del usuario
# con ese texto vamos a generar otro sin las vocales ni los espacios

""" 
t = input("Escribe un texto: ").lower()
lista =["a","e","i","o","u"," "]

for i in lista:
    print(i)
    t = t.replace(i,"")
# nt=t.replace("a"," ")
# # print(type(t))
# t=nt.replace("e"," ")
# nt=t.replace("i"," ")
# t=nt.replace("i"," ")
# nt=t.replace("o"," ")
# t=nt.replace("u"," ")
# nt = t.split(" ")
# print(type(nt))
# at=nt.split(" ")
# t="".join(at)
print(t)
"""
#3_Pedimos un numero entero, generamos la tabla de multiplicar del 1 al 10

# try:
#     num=int(input("Inroduce un numnero entero "))
#     for i in range(11):
#         print(f"{num} x {i} = {num*i}")
# except ValueError:
#     print("no has introducido un numero entero")

#4_Tenemos esta lista de animales: 
lista =["gato","perro","caballo","paloma","murcielago","leon","mono"]
#Vamos a pedir una letra al uruario y mostraremos los animales que contienen esa letra.
#y si no hay ningunodiremos: "ningun animal contiene esa letra"

cont = 0

letra = input("Introduce una letra: ").lower()
# if len(letra) != 1:
#     print("Introduce SOLO una letra")
#     exit()
if not letra.isalpha():
    print("Introduce una letra")
    exit()

for animal in lista:
    if letra in animal:
        print(animal)
        cont += 1
if cont == 0:
    print("Ningún animal contiene esa letra")
    