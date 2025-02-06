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

try:
    n= int(input("escribe un numero entre 0 y 100: "))
    if 0 <= n <= 100:
        for i in range(n+1):        #for i in range(0(desde), i+1(hasta),1(paso) )
            if i == 0:
                print("0")
            elif i % 3 == 0 and i % 5 == 0:           #Empezar por la mas restrictiva
                print(f"{i}-FIZZ-BUZZ")
            elif i % 5 == 0:
                print(f"{i}-BUZZ")
            elif i % 3 == 0:
                print(f"{i}-FIZZ")
            else:
                print(f"{i}")
    else:
        print("el numero es incorrecto")
        exit()                                        #sale del programa

except ValueError:
    print("tienes que escribir un numero")