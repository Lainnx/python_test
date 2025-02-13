"""
EJERCICIO 4 : CONVERSIÓN A MILLAS
Haz un programa que pida al usuario la distancia a convertir (en km)
Redondea el resultado a dos decimales
La respuesta del programa será:
"X km equivalen a Y millas" (los valores que sean)
Nota: 1 km son 0.621371 millas
"""
try:
    d = float(input("Introduce una distancia en kilometros: "))
    print(f"{d} kilometros equivalen a {d*0.621371} millas")
except ValueError:
    print("tienes que introducir un numero")