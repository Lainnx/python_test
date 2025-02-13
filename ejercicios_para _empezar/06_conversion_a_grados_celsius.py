'''
EJERCICIO 6: CONVERSIÓN A GRADOS CELSIUS
Haz un programa que pida al usuario la temperatura en grados Fahrenheit
La respuesta del programa será:
"X grados Fahrenheit equivalen a Y grados Celsius" (los valores que sean)
Formúla de conversión : Fahrenheit = (Celsius * 9/5) + 32
'''
try:
    f = float(input("Introduce una temperatura en Fahrenheit: "))
    print(f"{f} grados en Farenheit equivalen a {(f-32)*(5/9)}")
except ValueError:
    print("Tienes que introducir un numero")