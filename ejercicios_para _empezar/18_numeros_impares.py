'''
EJERCICIO 18: NÚMEROS IMPARES
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar los números impares introducidos
o un mensaje indicando que no hay ninguno.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
5, 3, 9
'''
try:
    numeros = input("Introduce una serie de numeros entre el 1 y el 20 separados por comas: ").strip().split(",")
    # print(numeros, type(numeros))
    for n in numeros:
        if float(n) < 1 or float(n) > 20:
            print("Introduce numeros entre el 1 y el 20")
            exit()
    lista_impares = []
    for n in numeros:
        if float(n) % 2 != 0:
            lista_impares.append(n)
    print((",".join(lista_impares)))
except ValueError:
    print("tienes que introducir numeros")