'''
EJERCICIO 17: SEGUNDO NÚMERO MAYOR
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el segundo número mayor.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
"El segundo número mayor es 6"
'''
try:
    numeros = sorted(input("Introduce una serie de numeros entre el 1 y el 20 separados por comas: ").strip().split(","))

    for n in numeros:
        if float(n) < 1 or float(n) > 20:
            print("Introduce numeros entre el 1 y el 20")
            exit()
        
    print(f"El segundo mayor es {numeros[-2]}")     #coge el 2o empezando por detras, como esta ordenado de menor a mayor este sera el segundo mayor

except ValueError:
    print("tienes que introducir numeros ")