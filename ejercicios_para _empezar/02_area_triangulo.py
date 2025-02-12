"""
EJERCICIO 2 : ÁREA DE UN TRIÁNGULO
Haz un programa que pida al usuario dos números, 
indicando que son la base y la altura de un triángulo
La respuesta del programa será:
"El área de un triángulo de base X y altura Y es Z" (los valores que sean)
"""
try:
    b = float(input("Introduce cuanto es la base del triangulo: "))
    h = float(input("Introduce la altura del triangulo: "))
    print(f"El area de un triangulo de base {b} y altura {h} es {(b*h)/2} u^2")
except(ValueError):
    print("Tienes que introducir numeros.")