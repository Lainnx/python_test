"""
EJERCICIO 5 : CONVERSIÓN A KM
Haz un programa que haga lo opuesto a lo anterior,
convertir millas es kilómetros
"""
try:
    d = float(input("Introduce una distancia en millas: "))
    print(f"{d} kilometros equivalen a {d/0.621371} millas")
except ValueError:
    print("tienes que introducir un numero")