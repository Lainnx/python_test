"""
EJERCICIO 1 : SUMA DE VALORES
Haz un programa que pida al usuario dos números para sumarlos.
La respuesta del programa será:
"La suma de los dos números es XX" (el valor que sea)
"""
try:
    print("Suma de 2 valores")
    a = float(input("Introduce el 1er valor: "))
    b = float(input("Introduce el 2o valor: "))
    print(f"{a} + {b} = {a+b}")
except ValueError:
    print("Tienes que introducir numeros")