'''
EJERCICIO 16: NÚMEROS AL CUADRADO
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el cuadrado de cada uno de los números.

Por ejemplo, si escribe:
2, 5, 3
La respuesta debe ser:
4, 25, 9
'''
try:
    numeros = input("Introduce una serie de numeros entre el 1 y el 20 separados por comas: ").strip().split(",")

    for n in numeros:
        if float(n) < 1 or float(n) > 20:
            print("Introduce numeros entre el 1 y el 20")
            exit()
    # print(numeros, type(numeros))
    lista_sq = []
    for numero in numeros:
        lista_sq.append(str(float(numero) ** 2))
    imp=",".join(lista_sq)
    print(imp)
except ValueError:
    print("tienes que introducir numeros ")