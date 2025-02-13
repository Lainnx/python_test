'''
EJERCICIO 8: CONVERSIÓN DE MONEDAS
Haz un programa que pida al usuario la cantidad de euros que quiere convertir a dólares
La respuesta del programa será:
"X euros equivalen a Y dólares" (los valores que sean)
Formúla de conversión : 1 euro = 1.18 dólares
'''
try:
    a = float(input("Introduce una cantidad en euros: "))
    print(f"{a} euros equivalen a {(a*1.18):.2f} dolares")
except ValueError:
    print("tienes que introducir un numero")