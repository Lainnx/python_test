'''
EJERCICIO 7: POSITIVO, NEGATIVO O CERO
Haz un programa que pida al usuario un número y diga si es positivo, 
negativo o cero
'''
try:
    a = float(input("Introduce un numero: "))
    if a == 0:              #cero
        print("a igual a 0")
    elif a < 0:             #a menor que cero, negativo
        print("a menor que 0")
    else:                   #a mayor que cero, positivo
        print("a mayor que 0")
except ValueError:
    print("tienes que introducir un numero")